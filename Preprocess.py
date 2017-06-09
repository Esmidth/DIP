import Const
from skimage import color, exposure, filters, morphology, io, img_as_ubyte
import Evaluate as eva
import matplotlib.pyplot as plt
import numpy as np


def rgb2hsv1(rgb_img):
    # Todo: Customize RGB2HSV function
    # hsv_img = color.convert_colorspace(rgb_img, 'RGB', 'HSV')
    # hsv_img = img_as_ubyte(hsv_img)
    hsv_img = np.zeros(rgb_img.shape)
    rows, cols, dims = rgb_img.shape
    for i in range(rows):
        for j in range(cols):
            p_max = max(rgb_img[i, j])
            p_min = min(rgb_img[i, j])
            r = rgb_img[i, j, 0] * 1.000
            g = rgb_img[i, j, 1] * 1.000
            b = rgb_img[i, j, 2] * 1.000
            if p_max == p_min:
                h = 0
            elif p_max == r and g >= b:
                h = 60 * (g - b) / (p_max - p_min)
            elif p_max == r and g < b:
                h = (60 * (g - b) / (p_max - p_min)) + 360
            elif p_max == g:
                h = (60 * (b - r) / (p_max - p_min)) + 120
            elif p_max == b:
                h = (60 * (r - g) / (p_max - p_min)) + 240
            if p_max == 0:
                s = 0
            else:
                s = 1 - p_min / p_max
            v = p_max
            hsv_img[i, j] = [h, s, v]
            if i == 0 and j == 88:
                print(h, s, v)
    return hsv_img


def rgb2hsv(rgb_img):
    hsv_img = color.convert_colorspace(rgb_img, 'RGB', 'HSV')
    hsv_img[:, :, 2] = hsv_img[:, :, 2] * 255
    hsv_img[:, :, 0] *= 360

    # print('fuck', hsv_img[0, 0, 2], max(rgb_img[0, 0, :]))
    return hsv_img


def hsv2rgb(img):
    rgb_img = color.convert_colorspace(img, 'HSV', 'RGB')
    return rgb_img


def normalization(src_img):
    pass


def thresholding(src_img):
    # Todo: modify gray_image to be returned be a 1-D array
    Rr = 90
    Hl = 190
    Hh = 245
    rows, cols, dims = src_img.shape
    img1 = np.zeros([rows, cols, dims])  # thresholding by R channel
    img2 = np.zeros([rows, cols])
    img3 = np.zeros([rows, cols])
    # print(src_img.shape, img1.shape)
    '''
    for i in range(rows):
        for j in range(cols):
            if src_img[i, j, 0] < Rr:
                img1[i, j, 0] = 255
                # reddish = img[:, :, 0] > 170
                # img[reddish] = [0, 255, 0]
                '''
    img_points = src_img[:, :, 0] < Rr
    img1[img_points] = [255, 255, 255]
    hsv_img = rgb2hsv1(src_img)
    # img_points = np.logical_and(hsv_img[:, :, 0] > Hl, hsv_img[:, :, 0] < Hh)
    # img_points1 = hsv_img[:, :, 0] > Hl
    # img_points2 = hsv_img[:, :, 0] < Hh

    for i in range(rows):
        for j in range(cols):
            h = hsv_img[i, j, 0]
            s = hsv_img[i, j, 1]
            if 200 <= h <= 280 and s >= 0.55:
                img2[i, j] = 255
            else:
                img2[i, j] = 0

    # print(hsv_img[0, 0, 0])
    # img2[img_points] = [255, 255, 255]
    hsv2 = rgb2hsv(src_img)
    for i in range(rows):
        for j in range(cols):
            h = hsv2[i, j, 0]
            s = hsv2[i, j, 1]
            if 200 <= h <= 280 and s >= 0.55:
                img3[i, j] = 255
            else:
                img3[i, j] = 0
    img3 = img2 - img3
    notzero = img3[:, :] != 0
    img3[notzero] = 255
    return img1, img2, img3


def preprocess(src_img):
    """

    :param src_img:
    :return: img
    """
    # hsv_img = rgb2hsv(src_img)
    thresh_s = 1
    thresh_i = 1
    thresh_j = 1
    gray_img = color.rgb2grey(src_img)
    thresh = filters.threshold_otsu(gray_img)
    bw = morphology.closing(gray_img > thresh, morphology.square(1))

    plt.imshow(bw, plt.cm.gray)
    plt.show()


def display(img, color_type='rgb'):
    if color_type == 'rgb':
        pass
    else:
        img = color.convert_colorspace(img, color_type, 'RGB')
    # plt.imshow(img)
    io.imshow(img)
    plt.show()


def test_display():
    img = Const.image1
    img = eva.load_image(img)
    display(img)


def test_preprocess():
    src_img = eva.load_image(Const.image1)
    preprocess(src_img)


def test_thresholding():
    img = eva.load_image(Const.image1)
    # display(img)
    fuck1, fuck2, fuck3 = thresholding(src_img=img)
    fuck1 = color.rgb2grey(fuck1)
    fuck2 = color.rgb2grey(fuck2)
    fuck3 = color.rgb2grey(fuck3)
    plt.subplot(221)
    plt.title('origin')
    io.imshow(img)
    plt.subplot(222)
    plt.title('R')
    io.imshow(fuck1)
    plt.subplot(223)
    plt.title('H')
    io.imshow(fuck2)
    plt.subplot(224)
    plt.title('Diff')
    io.imshow(fuck3)
    # plt.show()
    # io.imshow(fuck)
    io.show()


def test_1d_image():
    img = eva.load_image(Const.image1)
    r = img[:, :, 0]
    rr = r[:, :] > 100
    cc = r[:, :] <= 100
    img1 = r.copy()
    r[:, :] = 200
    plt.subplot(121)
    plt.title('img1')
    img1[rr] = 255
    img1[cc] = 0
    io.imshow(img1)
    plt.subplot(122)
    io.imshow(r)
    plt.title('fuck')
    plt.show()


if __name__ == '__main__':
    # test_preprocess()
    # test_display()
    test_thresholding()
    # test_1d_image()
