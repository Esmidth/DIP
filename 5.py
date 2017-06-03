from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import io, data
from skimage.viewer import ImageViewer


def ex_1():
    img = np.array(Image.open('fuck.jpg').convert('L'))

    plt.figure('lena')
    arr = img.flatten()
    n, bins, patches = plt.hist(arr, bins=256, normed=1, facecolor='green', alpha=0.75)
    plt.show()


def ex_2():
    src = Image.open('fuck.jpg')
    r, g, b = src.split()
    plt.figure('fuck')
    ar = np.array(r).flatten()
    plt.hist(ar, bins=256, normed=1, facecolor='r', edgecolor='r', hold=1)
    ag = np.array(g).flatten()
    plt.hist(ag, bins=256, normed=1, facecolor='g', edgecolor='g', hold=1)
    ab = np.array(b).flatten()
    plt.hist(ab, bins=256, normed=1, facecolor='b', edgecolor='b', hold=1)
    plt.show()


def ex_3():
    src = cv2.imread('fuck.jpg')
    b, g, r = cv2.split(src)  # cv2 read image channels in the sequence b,g,r while plt in the sequence r,g,b
    plt.figure('fuck')
    ar = np.array(r).flatten()
    plt.hist(ar, bins=256, normed=1, facecolor='r', edgecolor='r', hold=1)
    ag = np.array(g).flatten()
    plt.hist(ag, bins=256, normed=1, facecolor='g', edgecolor='g', hold=1)
    ab = np.array(b).flatten()
    plt.hist(ab, bins=256, normed=1, facecolor='b', edgecolor='b', hold=1)
    plt.show()


def ex_4():  # using plt to output
    img = data.astronaut()
    plt.figure(num='astronaut & RGB', figsize=(8, 8))

    #    plt.subplot(2, 2, 1)
    plt.subplot(221)
    plt.title('origin image')
    plt.imshow(img)

    plt.subplot(2, 2, 2)
    plt.title('R channel')
    plt.imshow(img[:, :, 0], plt.cm.gray)
    #    plt.imshow(img[:, :, 0])
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.title('G channel')
    plt.imshow(img[:, :, 1], plt.cm.gray)
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.title('B channel')
    plt.imshow(img[:, :, 2], plt.cm.gray)
    plt.axis('off')

    plt.show()


def ex_5():  # Fail on OSX 10.12.5
    img = data.astronaut()
    viewer = ImageViewer(img)
    viewer.show()


if __name__ == '__main__':
    ex_4()
