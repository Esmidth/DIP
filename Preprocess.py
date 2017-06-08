import Const
from skimage import color, exposure, filters, morphology
import Evaluate as eva
import matplotlib.pyplot as plt


def rgb2hsv(img):
    return color.convert_colorspace(img, 'RGB', 'HSV')


def hsv2rgb(img):
    return color.convert_colorspace(img, 'HSV', 'RGB')


def normalization(src_img):
    pass


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
    plt.imshow(img)
    plt.show()


def test_display():
    img = Const.image1
    img = eva.load_image(img)
    display(img)


def test_preprocess():
    src_img = eva.load_image(Const.image1)
    preprocess(src_img)


if __name__ == '__main__':
    test_preprocess()
    # test_display()
