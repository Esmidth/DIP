import Const
from skimage import color, exposure, filters, morphology, io, segmentation, measure
import Evaluate as eva
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


def rgb2hsv1(rgb_img):
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
    hsv_img[:, :, 2] = hsv_img[:, :, 2] * 255  # v[0,255]
    hsv_img[:, :, 0] *= 360  # h[0,360]
    # print('fuck', hsv_img[0, 0, 2], max(rgb_img[0, 0, :]))
    return hsv_img


def hsv2rgb(img):
    rgb_img = color.convert_colorspace(img, 'HSV', 'RGB')
    return rgb_img


def normalization(src_img):
    pass


def thresholding(src_img):
    rr = 90
    hl = 200
    hh = 280
    rows, cols, dims = src_img.shape
    img1 = np.zeros([rows, cols])  # thresholding by R channel
    img2 = np.zeros([rows, cols])
    img3 = np.zeros([rows, cols])
    img4 = np.zeros([rows, cols])
    # print(src_img.shape, img1.shape)

    img1_points = src_img[:, :, 0] < rr
    img1[img1_points] = 255
    hsv_img = rgb2hsv(src_img)
    '''
    for i in range(rows):
        for j in range(cols):
            h = hsv_img[i, j, 0]
            s = hsv_img[i, j, 1]
            if hl <= h <= hh and s >= 0.55:
                img2[i, j] = 255
            else:
                img2[i, j] = 0
    # this block is comparable slower than np.logical_and()
    '''
    img2_points = np.logical_and(hsv_img[:, :, 0] >= hl, hsv_img[:, :, 0] <= hh)
    img2_points = np.logical_and(hsv_img[:, :, 1] >= 0.55, img2_points)
    img2[img2_points] = 255

    gray_img = np.zeros([rows, cols])
    gray_img[:, :] = (src_img[:, :, 0] - src_img[:, :, 2])
    thresh = filters.threshold_otsu(gray_img)
    img3 = (gray_img <= thresh) * 255
    img3[:, :] = 255

    img_points = np.logical_and(img1_points, img2_points)
    img4_points = np.logical_and(img_points, img3[:, :] == 255)

    img4[img4_points] = 255
    return img4
    # return img1, img2, img3, img4


def morphology_c(gray_img):
    # gray_img = morphology.closing(gray_img, morphology.square(3))
    for i in range(1):
        gray_img = morphology.erosion(gray_img, morphology.square(3))
    for i in range(1):
        gray_img = morphology.dilation(gray_img, morphology.square(3))
        '''
    for i in range(1):
        gray_img = morphology.dilation(gray_img, morphology.square(5))
    for i in range(1):
        gray_img = morphology.erosion(gray_img, morphology.square(5))
        '''
    return gray_img


def connect_component_labeling(src_img):
    cleared = src_img.copy()
    segmentation.clear_border(cleared)
    label_image = measure.label(cleared)
    borders = np.logical_xor(src_img, cleared)
    label_image[borders] = -1
    return label_image


def divide_seg(label_image):
    objects = []
    for region in measure.regionprops(label_image):
        if region.area < 100:
            continue
        else:
            minr, minc, maxr, maxc = region.bbox
            r_margin = 2
            c_margin = 2
            minr -= r_margin
            minc -= c_margin
            maxr += r_margin
            maxc += c_margin
            seg = [[minc, minr], [maxc, minr], [maxc, maxr], [minc, maxr]]
            objects.append(seg)
    return objects


def correct_range(objects, img_shape):
    rows, cols, dim = img_shape
    for seg in objects:
        for point in seg:
            if point[0] < 0:
                point[0] = 0
            if point[1] < 0:
                point[1] = 0
    return objects


def preprocess(src_img):
    # Todo: Add Output Function to Judge The Preprocess Quality
    """

    :param src_img:
    :return: img
    """
    # hsv_img = rgb2hsv(src_img)
    gray_img = thresholding(src_img)
    img1 = morphology_c(gray_img)
    label_image = connect_component_labeling(img1)
    image_label_overlay = color.label2rgb(label_image, image=src_img)
    objects = divide_seg(label_image=label_image)
    objects = correct_range(objects, src_img.shape)
    # eva.draw_lines(src_img, objects, color='r')

    # fig, (ax0, ax1) = plt.subplots(1, 2)
    # ax0.imshow(image_label_overlay, plt.cm.gray)
    # ax1.imshow(src_img)
    # plt.show()
    return objects
    '''

    plt.subplot(221)
    plt.title('origin')
    io.imshow(src_img)

    plt.subplot(222)
    plt.title('morphology_c')
    io.imshow(img1)

    plt.subplot(223)
    plt.title('label_image')
    io.imshow(label_image)

    plt.subplot(224)
    plt.title('label_overlay')
    io.imshow(image_label_overlay)

    io.show()
    '''


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
    for i in range(1, 9):
        src_img = eva.load_image(Const.image + i.__str__() + '.jpg')
        preprocess(src_img)


def test_thresholding():
    img = eva.load_image(Const.image + '7.jpg')
    # display(img)
    fuck1, fuck2, fuck3, fuck4 = thresholding(src_img=img)
    fuck1 = color.rgb2grey(fuck1)
    fuck2 = color.rgb2grey(fuck2)
    fuck3 = color.rgb2grey(fuck3)
    fuck4 = color.rgb2grey(fuck4)

    plt.figure('Thresholding', figsize=(10, 10))
    plt.subplot(321)
    plt.title('origin')
    io.imshow(img)

    plt.subplot(322)
    plt.title('R')
    io.imshow(fuck1)

    plt.subplot(323)
    plt.title('H')
    io.imshow(fuck2)

    plt.subplot(324)
    plt.title('Otsu')
    io.imshow(fuck3)

    plt.subplot(325)
    plt.title('AND')
    io.imshow(fuck4)
    io.show()


def test_morphology_c():
    src_img = eva.load_image(Const.image1)
    gray_img = thresholding(src_img)
    img1 = morphology_c(gray_img)
    img2 = abs(gray_img - img1)

    plt.subplot(221)
    plt.title('origin')
    io.imshow(src_img)

    plt.subplot(222)
    plt.title('gray_img')
    io.imshow(gray_img)

    plt.subplot(223)
    plt.title('morphology')
    io.imshow(img1)

    plt.subplot(224)
    plt.title('diff')
    io.imshow(img2)

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


def test_divide_seg():
    for i in range(1, 9):
        src_img = eva.load_image(Const.image + i.__str__() + '.jpg')
        preprocess(src_img)
    gray_img = thresholding(src_img)
    img1 = morphology_c(gray_img)
    label_image = connect_component_labeling(img1)
    image_label_overlay = color.label2rgb(label_image, image=src_img)
    fig, (ax0, ax1) = plt.subplots(1, 2)
    ax0.imshow(image_label_overlay, plt.cm.gray)
    objects = divide_seg(label_image=label_image)
    # rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr, fill=False, edgecolor='red', linewidth=2)
    # ax1.add_patch(rect)

    eva.draw_lines(src_img, objects, color='r')
    ax1.imshow(src_img)
    plt.show()


if __name__ == '__main__':
    # test_preprocess()
    # test_display()
    # test_thresholding()
    # test_1d_image()
    # test_morphology_c()
    test_divide_seg()
