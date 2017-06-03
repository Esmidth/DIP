import numpy as np
from skimage import exposure, data
import matplotlib.pyplot as plt


def ex_1():
    image = data.camera() * 1.0
    hist1 = np.histogram(image, bins=2)
    hist2 = exposure.histogram(image, nbins=2)
    print(hist1)
    print(hist2)


def ex_2():  # single channel histogram
    img = data.camera()
    plt.figure('hist')
    arr = img.flatten()
    n, bins, patches = plt.hist(arr, bins=256, normed=1, edgecolor='None', facecolor='red')
    plt.show()


def ex_3():
    img = data.chelsea()
    ar = img[:, :, 0].flatten()
    plt.hist(ar, bins=256, normed=1, facecolor='r', edgecolor='r', hold=1)
    ag = img[:, :, 1].flatten()
    plt.hist(ag, bins=256, normed=1, facecolor='g', edgecolor='g', hold=1)
    ab = img[:, :, 2].flatten()
    plt.hist(ab, bins=256, normed=1, facecolor='b', edgecolor='b')
    plt.show()


def ex_4():  # Histogram Equalization
    img = data.moon()
    plt.figure('hist', figsize=(8, 8))

    arr = img.flatten()
    plt.subplot(221)
    plt.imshow(img, plt.cm.gray)
    plt.subplot(222)
    plt.hist(arr, bins=256, normed=1, edgecolor='None', facecolor='red')

    img1 = exposure.equalize_hist(img)  # Key Function
    arr1 = img1.flatten()
    plt.subplot(223)
    plt.imshow(img1, plt.cm.gray)
    plt.subplot(224)
    plt.hist(arr1, bins=256, normed=1, edgecolor='None', facecolor='red')

    plt.show()


if __name__ == "__main__":
    ex_4()
