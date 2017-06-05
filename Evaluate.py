from skimage import io, data, draw
import matplotlib.pyplot as plt
import os
import sys
import codecs
import numpy as np


def load_image(file):
    """

    :param file: str -> image path
    :return: numpy.ndarray -> image color buffer in r,g,b channel
    """
    return io.imread(file)


def load_txt(file):
    """

    :param file: str
    :return: str
    """
    in_enc = 'UTF-8'
    f = codecs.open(file, 'r', in_enc)
    content = f.read()
    return content


def draw_lines(img, odd):
    """

    :param image: np.ndarray
    :param odd:
    :return:
    """
    coord_s = []
    objects = []
    for o in odd:
        coord_s = o.split(',')
        objects.append(coord_s)

    for o in objects:
        img[int(o[1]), int(o[0])] = [255, 0, 0]
        img[int(o[3]), int(o[2])] = [255, 0, 0]
        img[int(o[5]), int(o[4])] = [255, 0, 0]
        img[int(o[7]), int(o[6])] = [255, 0, 0]

    return objects


def split_str(str):
    """

    :param str: str
    :return: list-> odd as coordinate location, even as value
    """
    seps = str.split('\n')
    for j in range(3):
        for i, sep in enumerate(seps):
            if '\r' in sep:
                seps[i] = sep[:-1]
            if sep == '':
                del seps[i]
    return seps


def two_parp(seps):
    odd = []
    even = []
    for i, sep in enumerate(seps):
        if i % 2 == 0:
            odd.append(sep)
        else:
            even.append(sep)
    return odd, even


def test():
    path = '/Users/esmidth/Github/DIP/train'
    image_path = path + '/' + 'Train_BJ_001.jpg'
    image = load_image(image_path)
    plt.imshow(image)
    plt.show()


def test_split():
    path = '/Users/esmidth/Github/DIP/train'
    file = path + '/' + 'Train_BJ_002.txt'
    str = load_txt(file)
    seps = split_str(str)
    odd, even = two_parp(seps)
    a = []
    a.append(str)
    # print(odd)
    print(seps)
    print(a)


def test_draw():
    number = 1
    path = '/Users/esmidth/Github/DIP/train' + '/' + 'Train_BJ_00' + number.__str__()
    txt = path + '.txt'
    image = path + '.jpg'
    # print(type(io.imread(image)))
    f = io.imread(image)

    str = load_txt(txt)
    seps = split_str(str)
    odd, even = two_parp(seps)
    draw_lines(f, odd=odd)
    io.imshow(f)
    io.show()
    # print(odd)
    # print(draw_lines(odd))
    # draw_lines(image, odd)


if __name__ == '__main__':
    test_draw()
