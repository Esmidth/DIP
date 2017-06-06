from skimage import io, data, draw
import matplotlib.pyplot as plt
import os
import sys
import codecs
import numpy as np
import Const


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


def draw_lines(img, objects, color='r', content=[]):
    """
    :param color: str -> determinate the color of polygon
    :param img: np.ndarray
    :param objects: list -> coordinate points divided into segments
    """
    c = [255, 255, 255]
    if color == 'r':
        c = [255, 0, 0]
    elif color == 'g':
        c = [0, 255, 0]
    else:
        pass
    for i, seg in enumerate(objects):
        if content == [] or content[i] == '0':  # 用于粗检测
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

    # return objects


def split_str(str):
    """

    :param str: str
    :return: list-> odd as coordinate location, even as value
    """
    seps = str.split('\n')
    repeat = 3
    for j in range(repeat):
        for i, sep in enumerate(seps):
            if '\r' in sep:
                seps[i] = sep[:-1]
            if sep == '':
                del seps[i]
    return seps


def divide_para(seps):  # Divide seps into locations & values
    coord = []
    contents = []
    objects = []
    for i, sep in enumerate(seps):
        if i % 2 == 0:
            coord.append(sep)
        else:
            contents.append(sep)
    for o in coord:
        seg = o.split(',')
        points = [[int(seg[0]), int(seg[1])], [int(seg[2]), int(seg[3])], [int(seg[4]), int(seg[5])],
                  [int(seg[6]), int(seg[7])]]
        objects.append(points)
    return objects, contents


def is_number(strr):
    if '0' <= strr[0] <= '9':
        return True
    else:
        return False


def compute_rju(seg1, seg2):
    area1 = (seg1[1][0] - seg1[0][0]) * (seg1[2][1] - seg1[1][1])
    area2 = (seg2[1][0] - seg2[0][0]) * (seg2[2][1] - seg2[1][1])
    p1 = [max(seg1[0][0], seg2[0][0]), max(seg1[0][1], seg2[0][1])]
    p2 = [min(seg1[2][0], seg2[2][0]), min(seg1[2][1], seg2[2][1])]
    area_join = 0
    if p2[0] > p1[0] and p2[1] > p1[1]:
        area_join = (p2[0] - p1[0]) * (p2[1] - p1[1])
    area_union = (area1 + area2 - area_join)
    if area_union > 0:
        return area_join / area_union
    else:
        return 0


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
    odd, even = divide_para(seps)
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
    objects, contents = divide_para(seps)
    draw_lines(f, objects=objects, content=contents)
    for i, seg in enumerate(objects):
        for points in seg:
            print(points)
        print(contents[i])
        print('No: ' + i.__str__() + '\n')
    io.imshow(f)
    io.show()
    # print(odd)
    # print(draw_lines(odd))
    # draw_lines(image, odd)


def test_compute():
    image1 = Const.image1
    txt1 = Const.txt1
    f = load_image(image1)
    seps = split_str(load_txt(txt1))
    objects, contents = divide_para(seps)
    for i, seg in enumerate(objects):
        print(str(compute_rju(objects[0], objects[i]) * 100) + '%')


if __name__ == '__main__':
    # test_draw()
    test_compute()
