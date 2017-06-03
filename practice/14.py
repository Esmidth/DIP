from skimage import data, color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr


def ex_1():  # 拉伸灰度像素的直方图，以覆盖整个像素值范围
    img = color.rgb2gray(data.chelsea())
    auto = sfr.autolevel(img, disk(5))

    plt.figure('fuck')
    plt.subplot(121)
    plt.title('origin')
    plt.imshow(img, plt.cm.gray)

    plt.subplot(122)
    plt.title('filtered image')
    plt.imshow(auto, plt.cm.gray)
    plt.show()


def ex_2():
    """
    bottomhat: 先闭运算，再用原图像减去运算的结果
    tophat: 先开运算，再用原图像减去运算结果
    """
    img = color.rgb2gray(data.chelsea())
    auto = sfr.bottomhat(img, disk(5))

    plt.figure('filters')
    plt.subplot(121)
    plt.title('origin')
    plt.imshow(img, plt.cm.gray)

    plt.subplot(122)
    plt.title('filtered image')
    plt.imshow(auto, plt.cm.gray)

    plt.show()


def ex_3():  # enhance contrast
    img = color.rgb2gray(data.chelsea())
    auto = sfr.enhance_contrast(img, disk(5))

    plt.figure('filters')
    plt.subplot(121)
    plt.title('origin')
    plt.imshow(img, plt.cm.gray)

    plt.subplot(122)
    plt.title('filtered image')
    plt.imshow(auto, plt.cm.gray)

    plt.show()


def ex_4():  # entropy 求局部熵
    img = color.rgb2gray(data.chelsea())
    dst = sfr.entropy(img, disk(5))

    plt.figure('filters')
    plt.subplot(121)
    plt.title('origin')
    plt.imshow(img, plt.cm.gray)

    plt.subplot(122)
    plt.title('filtered image')
    plt.imshow(dst, plt.cm.gray)

    plt.show()


def ex_5():  # equalize 均值化滤波
    img = color.rgb2gray(data.chelsea())
    dst = sfr.equalize(img, disk(5))

    plt.figure('filters')
    plt.subplot(121)
    plt.title('origin')
    plt.imshow(img, plt.cm.gray)

    plt.subplot(122)
    plt.title('filtered')
    plt.imshow(dst, plt.cm.gray)

    plt.show()


def ex_6():  # gradient 返回局部梯度值
    img = color.rgb2gray(data.chelsea())
    dst = sfr.gradient(img, disk(5))

    plt.figure('filters')
    plt.subplot(121)
    plt.title('origin')
    plt.imshow(img, plt.cm.gray)

    plt.subplot(122)
    plt.title('filtered')
    plt.imshow(dst, plt.cm.gray)

    plt.show()


if __name__ == "__main__":
    ex_6()
