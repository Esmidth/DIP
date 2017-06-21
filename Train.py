import Const
import Evaluate as eva
import matplotlib.pyplot as plt
from skimage import io, data, color, exposure
from skimage.feature import hog
import Preprocess as pre
import numpy as np


def cut_image(image, seg):
    return image[seg[0][1]:seg[3][1], seg[0][0]:seg[1][0]]


def compute_hog(image=data.astronaut()):
    image = color.rgb2grey(image)
    fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualise=True)

    hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 0.02))
    return hog_image_rescaled


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
        cute_hog = compute_hog(cute_image)
        plt.subplot(131)
        plt.imshow(cute_hog, plt.cm.gray)
        plt.subplot(132)
        plt.imshow(cute_image, plt.cm.gray)
        plt.subplot(133)
        n, bins, patches = plt.hist(cute_hog.flatten(), bins=180, normed=1, edgecolor='None', facecolor='red')
        plt.show()


if __name__ == '__main__':
    # test_cut_image()
    test_hog()
