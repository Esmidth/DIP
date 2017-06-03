from skimage import data, io, img_as_float, color
import numpy as np


def ex1():
    img = data.chelsea()
    print(img.dtype.name)
    dst = img_as_float(img)
    print(dst.dtype.name)


def ex2():  # RGB 2 Gray
    img = data.chelsea()
    gray = color.rgb2gray(img)
    io.imshow(gray)
    io.show()


def ex3():
    img = data.chelsea()
    hsv = color.convert_colorspace(img, 'RGB', 'HSV')
    io.imshow(hsv)
    io.show()


def ex4():
    img = data.chelsea()
    gray = color.rgb2gray(img)
    rows, cols = gray.shape
    labels = np.zeros([rows, cols])
    for i in range(rows):
        for j in range(cols):
            if gray[i, j] < 0.4:
                labels[i, j] = 0
            elif gray[i, j] < 0.75:
                labels[i, j] = 1
            else:
                labels[i, j] = 2
    dst = color.label2rgb(labels)
    io.imshow(dst)
    io.show()


if __name__ == "__main__":
    ex4()
