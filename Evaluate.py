from skimage import io, data
import matplotlib.pyplot as plt
import os
import sys
import codecs


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


def draw_lines(data):
    pass


def split_str(str):
    seps = str.split('\r\n')
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
            even.append(sep)
        else:
            odd.append(sep)
    return odd, even


def test():
    path = '/Users/esmidth/Github/DIP/train'
    image_path = path + '/' + 'Train_BJ_001.jpg'
    image = load_image(image_path)
    plt.imshow(image)
    plt.show()


def test_split():
    path = '/Users/esmidth/Github/DIP/train'
    file = path + '/' + 'Train_BJ_004.txt'
    str = load_txt(file)
    a = []
    a.append(str)
    print(a)


if __name__ == '__main__':
    test_split()
