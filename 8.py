from skimage import data, exposure, img_as_float
import matplotlib.pyplot as plt
import numpy as np


def ex1():
    image = img_as_float(data.moon())
    gam1 = exposure.adjust_gamma(image, 2)
    gam2 = exposure.adjust_gamma(image, 0.5)
    plt.figure('adjust_gamma', figsize=(8, 8))

    plt.subplot(131)
    plt.title('origin image')
    plt.imshow(image, plt.cm.gray)
    plt.axis('off')

    plt.subplot(132)
    plt.title('gamma=2')
    plt.imshow(gam1, plt.cm.gray)
    plt.axis('off')

    plt.subplot(133)
    plt.title('gamma=0.5')
    plt.imshow(gam2, plt.cm.gray)
    plt.axis('off')

    plt.show()


def ex2():
    image = img_as_float(data.moon())
    gaml = exposure.adjust_log(image)
    plt.figure('adjust_gamma', figsize=(8, 8))

    plt.subplot(121)
    plt.title('origin')
    plt.imshow(image, plt.cm.gray)
    plt.axis('off')

    plt.subplot(122)
    plt.title('log')
    plt.imshow(gaml, plt.cm.gray)
    plt.axis('off')

    plt.show()


def ex3():
    image = data.moon()
    result = exposure.is_low_contrast(image)
    print(result)


def ex4():
    image = np.array([51, 102, 153], dtype=np.uint8)
    mat = exposure.rescale_intensity(image)
    print(mat)


if __name__ == '__main__':
    ex4()
