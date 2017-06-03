from skimage import data, filters, feature
from skimage.morphology import disk

import matplotlib.pyplot as plt


def ex_1():  # sobel,roberts,scharr,prewitt,canny operator
    img = data.camera()
    edges = filters.sobel(img)
    edges1 = filters.roberts(img)
    edges2 = filters.scharr(img)
    edges3 = filters.prewitt(img)
    # edges4 = feature.canny(img,sigma=3)
    edges4 = feature.canny(img)

    plt.subplot(231)
    plt.imshow(edges, plt.cm.gray)
    plt.title('sobel')

    plt.subplot(232)
    plt.imshow(edges1, plt.cm.gray)
    plt.title('robert')

    plt.subplot(233)
    plt.imshow(edges2, plt.cm.gray)
    plt.title('scharr')

    plt.subplot(234)
    plt.imshow(edges3, plt.cm.gray)
    plt.title('prewitt')

    plt.subplot(235)
    plt.imshow(edges4, plt.cm.gray)
    plt.title('canny')

    plt.show()


def ex_2():  # gabor filter
    img = data.camera()
    filt_real, filt_imag = filters.gabor_filter(img, frequency=0.6)

    plt.figure('gabor', figsize=(8, 8))

    plt.subplot(121)
    plt.title('filt_real')
    plt.imshow(filt_real, plt.cm.gray)

    plt.subplot(122)
    plt.title('filt_imag')
    plt.imshow(filt_imag, plt.cm.gray)

    plt.show()


def ex_3():  # gaussian filter
    img = data.astronaut()
    edges1 = filters.gaussian_filter(img, sigma=0.4)
    edges2 = filters.gaussian_filter(img, sigma=5)

    plt.figure('gaussian', figsize=(8, 8))

    plt.subplot(121)
    plt.imshow(edges1, plt.cm.gray)
    plt.title('sigma = 0.4')

    plt.subplot(122)
    plt.imshow(edges2, plt.cm.gray)
    plt.title('sigma = 5')

    plt.show()


def ex_4():  # median filter
    img = data.camera()
    edges1 = filters.median(img, disk(5))
    edges2 = filters.median(img, disk(9))

    plt.figure('median')

    plt.subplot(121)
    plt.imshow(edges1, plt.cm.gray)

    plt.subplot(122)
    plt.imshow(edges2, plt.cm.gray)

    plt.show()


def ex_5():  # Sobel vertical & horizontal operator
    img = data.camera()
    edges = filters.sobel(img)
    edges1 = filters.sobel_h(img)
    edges2 = filters.sobel_v(img)

    plt.figure('sobel_v_h')

    plt.subplot(131)
    plt.title('sobel_h')
    plt.imshow(edges1, plt.cm.gray)

    plt.subplot(132)
    plt.title('sobel_v')
    plt.imshow(edges2, plt.cm.gray)

    plt.subplot(133)
    plt.title('sobel')
    plt.imshow(edges, plt.cm.gray)

    plt.show()


def ex_6():  # Roberts 交叉边缘检测
    """
    core
    0   1
    -1  0
    """
    img = data.camera()
    dst = filters.roberts_neg_diag(img)

    plt.figure('filters')

    plt.subplot(121)
    plt.title('origin image')
    plt.imshow(img, plt.cm.gray)

    plt.subplot(122)
    plt.title('filtered image')
    plt.imshow(dst, plt.cm.gray)

    plt.show()


def ex_7():  # Roberts 交叉边缘检测
    """
    core
    1   0
    0  -1
    """
    img = data.camera()
    dst = filters.roberts_pos_diag(img)

    plt.figure('filters')
    plt.subplot(121)
    plt.title('origin image')
    plt.imshow(img, plt.cm.gray)

    plt.subplot(122)
    plt.title('filtered image')
    plt.imshow(dst, plt.cm.gray)
    plt.show()


if __name__ == '__main__':
    ex_7()
