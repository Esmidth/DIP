import Const
import Evaluate as eva
import matplotlib.pyplot as plt
from skimage import io, data, color, exposure
from skimage.feature import hog
import Preprocess as pre
import numpy as np
from sklearn.externals import joblib
import os


def cut_image(image, seg):
    return image[seg[0][1]:seg[3][1], seg[0][0]:seg[1][0]]


def compute_hog(image=data.astronaut()):
    image = color.rgb2grey(image)
    fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualise=True,
                        transform_sqrt=True)

    hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 0.02))
    return fd, hog_image_rescaled


def extract_feature(jpg, txt, svm_path=Const.svm_path):
    image = eva.load_image(jpg)
    strr = eva.load_txt(txt)
    l_objects, l_contents = eva.divide_para1(strr)
    objects = []
    for i, l_c in enumerate(l_contents):
        if l_c == '0':
            objects.append(l_objects[i])
    image_collection = []
    for j, i in enumerate(objects):
        image_collection.append(cut_image(image, i))
        seg_image = cut_image(image, i)
        fd_s, hog_image_s = compute_hog(seg_image)
        fd_s_name = os.path.split(jpg)[1].split('.')[0] + '_' + j.__str__() + '.feat'
        fd_s_path = os.path.join(svm_path[0], fd_s_name)
        print(fd_s_path)


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

    image = eva.load_image(jpgs[1])
    strr = eva.load_txt(txts[1])
    l_objects, l_contents = eva.divide_para1(strr)
    objects = []
    for i, l_c in enumerate(l_contents):
        if l_c == '0':
            objects.append(l_objects[i])
    image_collection = []
    for j, i in enumerate(objects):
        image_collection.append(cut_image(image, i))
        seg_image = cut_image(image, i)
        fd_s, hog_image_s = compute_hog(seg_image)
        fd_s_name = os.path.split(jpgs[1])[1].split('.')[0] + '_' + j.__str__() + '.feat'
        fd_s_path = os.path.join(svm_path[0], fd_s_name)
        print(fd_s_path)
        # joblib.dump(fd_s,fd_s_name)


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


def test_train_svm():
    extract_features(Const.src_path, Const.svm_path)


if __name__ == '__main__':
    # test_cut_image()
    # test_hog()
    test_train_svm()
