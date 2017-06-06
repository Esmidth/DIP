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


def draw_lines(img, coord, color='r'):
    """

    :param color: str -> determinate the color of polygon
    :param img: np.ndarray
    :param coord: list -> coordinate points
    :return objects: list -> coordinate points divided into segments
    """
    objects = []
    c = [255, 255, 255]
    if color == 'r':
        c = [255, 0, 0]
    elif color == 'g':
        c = [0, 255, 0]
    else:
        pass
    for o in coord:
        seg = o.split(',')
        points = [[int(seg[0]), int(seg[1])], [int(seg[2]), int(seg[3])], [int(seg[4]), int(seg[5])],
                  [int(seg[6]), int(seg[7])]]
        objects.append(points)
    for seg in objects:
        x = []
        y = []
        for point in seg:
            x.append(point[0])
            y.append(point[1])
        x = np.array(x)
        y = np.array(y)
        rr, cc = draw.polygon_perimeter(y, x)
        img[rr, cc] = c
    '''
    for i, seg in enumerate(objects):
        for j, points in enumerate(seg):
            seg[j] = int(points)
    for seg in objects:
        points = [[int(seg[0]), int(seg[1])], [int(seg[2]), int(seg[3])], [int(seg[4]), int(seg[5])],
                  [int(seg[6]), int(seg[7])]]
        objects_points.append(points)
    '''

    '''
    for seg in objects:  # Draw Polygon as mask on the location
        x = np.array([seg[0], seg[2], seg[4], seg[6]])
        y = np.array([seg[1], seg[3], seg[5], seg[7]])
        rr, cc = draw.polygon_perimeter(y, x)
        img[rr, cc] = c
    '''
    '''
    for o in objects:
        img[o[1], o[0]] = [255, 0, 0]
        img[o[3], o[2]] = [255, 0, 0]
        img[o[5], o[4]] = [255, 0, 0]
        img[o[7], o[6]] = [255, 0, 0]
    '''

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


def two_parp(seps):  # Divide seps into locations & values
    coord = []
    value = []
    for i, sep in enumerate(seps):
        if i % 2 == 0:
            coord.append(sep)
        else:
            value.append(sep)
    return coord, value


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

    strr = load_txt(txt)
    seps = split_str(strr)
    coord, value = two_parp(seps)
    objects_new = draw_lines(f, coord=coord)
    for seg in objects_new:
        for points in seg:
            print(points)
        print('\n')
    io.imshow(f)
    io.show()
    # print(odd)
    # print(draw_lines(odd))
    # draw_lines(image, odd)


def test_compute():
    pass


if __name__ == '__main__':
    test_draw()
