from skimage import data, io
import numpy as np
import cv2


def ex_1():
    img = data.chelsea()
    rows, cols, dims = img.shape
    for i in range(5000):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        img[x, y, :] = 255
    io.imshow(img)
    io.show()


def ex_2():
    img = data.chelsea()
    pixel = img[20, 30, 1]
    print(pixel)


def ex_3():
    img = data.chelsea()
    r = img[:, :, 1]
    io.imshow(r)
    io.show()


def ex_4():
    img = data.chelsea()
    roi = img[80:180, 100:200, :]
    io.imshow(roi)
    io.show()


def ex_5():
    img = data.chelsea()
    img[80:180, 100:200, 2] = 255
    io.imshow(img)
    io.show()


def ex_6():
    img = data.chelsea()
    reddish = img[:, :, 0] > 170
    img[reddish] = [0, 255, 0]
    io.imshow(img)
    io.show()


def ex_61():
    img = data.chelsea()
    rows, cols, dims = img.shape
    for x in range(0, rows):
        for y in range(0, cols):
            if img[x, y, 0] > 170:
                img[x, y, :] = [0, 255, 0]

    io.imshow(img)
    io.show()


if __name__ == "__main__":
    ex_61()
