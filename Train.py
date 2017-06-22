import Const
import Evaluate as eva
import matplotlib.pyplot as plt
from skimage import io, data, color, exposure, transform
from skimage.feature import hog
import Preprocess as pre
import numpy as np

from sklearn.externals import joblib
from sklearn import svm
import os

from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression


def cut_image(image, seg):
    return image[seg[0][1]:seg[3][1], seg[0][0]:seg[1][0]]


def compute_hog(image=data.astronaut()):
    image = color.rgb2grey(image)
    # image = exposure.adjust_gamma(image, 0.5)
    fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualise=True,
                        transform_sqrt=True)

    hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 0.02))
    return fd, hog_image_rescaled


def extract_feature(jpg, txt, feat_path=Const.feature_path):
    image = eva.load_image(jpg)
    # image = exposure.adjust_gamma(image, 0.5)
    strr = eva.load_txt(txt)
    l_objects, l_contents = eva.divide_para1(strr)
    pos_objects = []
    neg_objects = []
    for i, l_c in enumerate(l_contents):
        if l_c == '0':
            pos_objects.append(l_objects[i])
        else:
            neg_objects.append(l_objects[i])

    # extract pos hog feature
    for j, i in enumerate(pos_objects):
        seg_image = cut_image(image, i)
        seg_image = transform.resize(seg_image, Const.normal_size)
        # pre.display(seg_image)
        fd_s, hog_image_s = compute_hog(seg_image)
        fd_s_name = os.path.split(jpg)[1].split('.')[0] + '_' + j.__str__() + '.feat'
        fd_s_path = os.path.join(feat_path[0], fd_s_name)
        joblib.dump(fd_s, fd_s_path)
        # print(fd_s_path)

        # TODO: add negative hog features in txts


'''
    # extract neg hog feature
    for j, i in enumerate(neg_objects):
        seg_image = cut_image(image, i)
        pre.display(seg_image)
        fd_s, hog_image_s = compute_hog(seg_image)
        fd_s_name = os.path.split(jpg)[1].split('.')[0] + '_' + j.__str__() + '.feat'
        fd_s_path = os.path.join(svm_path[1], fd_s_name)
        print(fd_s_path)
        '''


def extract_features(src_path, svm_path):
    list_dirs = os.walk(src_path)
    jpgs = []
    txts = []
    for root, dirs, files in list_dirs:
        for f in files:
            if 'jpg' in f:
                path = os.path.join(root, f)
                jpgs.append(path)
            elif 'txt' in f:
                path = os.path.join(root, f)
                txts.append(path)
    #
    # extract_feature(jpgs[0], txts[0], svm_path)
    for i, jpg in enumerate(jpgs):
        extract_feature(jpg, txts[i], svm_path)


def train_classifier(feat_path=Const.feature_path, model_path=Const.model_path):
    # Train positive features
    pos_list_dirs = os.walk(feat_path[0])
    neg_list_dirs = os.walk(feat_path[1])
    fds = []
    labels = []
    for root, dirs, files in pos_list_dirs:
        for f in files:
            path = os.path.join(root, f)
            fd = joblib.load(path)
            fds.append(fd)
            labels.append(1)
    for root, dirs, files in neg_list_dirs:
        for f in files:
            path = os.path.join(root, f)
            fd = joblib.load(path)
            fds.append(fd)
            labels.append(0)

    # train classifier as LIN_SVM
    # clf = LinearSVC()
    clf = svm.SVC()
    clf.fit(fds, labels)
    date = 20170623
    joblib.dump(clf, model_path + date.__str__() + '.clf')


def test_cut_image():
    image = eva.load_image(Const.image1)
    txt = eva.load_txt(Const.txt1)
    seps = eva.split_str(txt)
    objects, contents = eva.divide_para(seps)
    cute_image = cut_image(image, objects[0])

    plt.figure('fuck')
    plt.subplot(121)
    plt.imshow(image)
    plt.subplot(122)
    plt.imshow(cute_image)
    plt.show()


def test_hog():
    i = 1
    image = eva.load_image(Const.image + i.__str__() + '.jpg')
    # txt = eva.load_txt(Const.txt1)
    # seps = eva.split_str(txt)
    # objects, contents = eva.divide_para(seps)
    objects = pre.preprocess(image)
    # eva.draw_lines(image,objects)
    for seg in objects:
        cute_image = cut_image(image, seg)
        fd, cute_hog = compute_hog(cute_image)
        plt.subplot(131)
        plt.imshow(cute_hog, plt.cm.gray)
        plt.subplot(132)
        plt.imshow(cute_image, plt.cm.gray)
        plt.subplot(133)
        n, bins, patches = plt.hist(cute_hog.flatten(), bins=180, normed=1, edgecolor='None', facecolor='red')
        plt.show()


def test_extract_features():
    extract_features(Const.src_path, Const.feature_path)


def test_train_classifier():
    train_classifier()


def compute_size():
    list_dirs = os.walk(Const.src_path)
    x_sizes = []
    y_sizes = []
    ratio = []
    jpgs = []
    txts = []
    for root, dirs, files in list_dirs:
        for f in files:
            if 'jpg' in f:
                path = os.path.join(root, f)
                jpgs.append(path)
            elif 'txt' in f:
                path = os.path.join(root, f)
                txts.append(path)
    for i, jpg in enumerate(jpgs):
        image = eva.load_image(jpg)
        strr = eva.load_txt(txts[i])
        l_objects, l_contents = eva.divide_para1(strr)
        for i, l_c in enumerate(l_contents):
            if l_c == '0':
                seg_image = cut_image(image, l_objects[i])
                x_sizes.append(seg_image.shape[0])
                y_sizes.append(seg_image.shape[1])
                ratio.append(seg_image.shape[1] / seg_image.shape[0])

    ratio.sort()
    x_sizes.sort()
    y_sizes.sort()
    plt.subplot(131)
    plt.title('x')
    n, bins, patches = plt.hist(x_sizes, bins=180, normed=1, edgecolor='None', facecolor='red')
    plt.subplot(132)
    plt.title('y')
    n, bins, patches = plt.hist(y_sizes, bins=180, normed=1, edgecolor='None', facecolor='red')
    plt.subplot(133)
    plt.title('ratio')
    n, bins, patches = plt.hist(ratio, bins=180, normed=1, edgecolor='None', facecolor='red')
    plt.show()


if __name__ == '__main__':
    # test_cut_image()
    # test_hog()
    # test_extract_features()
    test_train_classifier()
    # compute_size()
