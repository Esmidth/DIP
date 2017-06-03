import skimage.io as io
from skimage import data_dir, color, transform
import numpy as np


def ex_1():
    str = data_dir + "/*.png"
    coll = io.ImageCollection(str)
    print(len(coll))
    io.imshow(coll[5])
    io.imshow(coll[4])
    io.show()


def ex_2():  # import all train jpgs
    str123 = '/Users/esmidth/Github/DIP/train/*.jpg'
    coll = io.ImageCollection(str123)
    fuck = coll[0]
    print(len(coll))
    print(coll[0].shape)


def convert_gray(f):
    rgb = io.imread(f)
    return color.rgb2gray(rgb)


def convert_gray2(file):
    rgb = io.imread(file)
    gray = color.rgb2gray(rgb)
    dst = transform.resize(gray, (256, 256))
    return dst


def ex_3():
    str123 = '/Users/esmidth/Github/DIP/train/*.jpg'
    coll = io.ImageCollection(str123, load_func=convert_gray)
    io.imshow(coll[10])
    io.show()


def ex_4():
    path = '/Users/esmidth/Github/DIP/train/*.jpg'
    coll = io.ImageCollection(path, load_func=convert_gray2)
    for i in range(len(coll)):
        io.imsave('/Users/esmidth/Github/DIP/train1/' + np.str(i) + '.jpg', coll[i])


if __name__ == "__main__":
    ex_2()
