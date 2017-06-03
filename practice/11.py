from skimage import data, filters
import matplotlib.pyplot as plt


def ex_1():  # threshold_otsu
    image = data.camera()
    thresh = filters.threshold_otsu(image)
    dst = (image <= thresh) * 1.0

    plt.figure('otsu')

    plt.subplot(121)
    plt.title('origin')
    plt.imshow(image, plt.cm.gray)

    plt.subplot(122)
    plt.title('binary')
    plt.imshow(dst, plt.cm.gray)

    plt.show()


def ex_2():
    image = data.camera()
    #    thresh = filters.threshold_yen(image)
    thresh = filters.threshold_li(image)
    print(thresh)
    dst = (image <= thresh) * 1.0

    plt.figure('yen')

    plt.subplot(121)
    plt.title('origin')
    plt.imshow(image, plt.cm.gray)

    plt.subplot(122)
    plt.title('binary')
    plt.imshow(dst, plt.cm.gray)

    plt.show()


if __name__ == "__main__":
    ex_2()
