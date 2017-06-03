from skimage import draw, data
import matplotlib.pyplot as plt
import numpy as np


def ex_1():  # draw a line
    img = data.chelsea()
    rows, cols, dim = img.shape
    print(img.shape)
    rr, cc = draw.line(0, 0, rows - 1, cols - 1)
    img[rr, cc] = [255, 0, 0]
    plt.imshow(img, plt.cm.gray)
    plt.show()


def ex_2():  # draw circle
    img = data.chelsea()
    # rr, cc = draw.circle(150, 150, 50) # 实心圆
    rr, cc = draw.circle_perimeter(150, 150, 50)  # 空心圆
    img[rr, cc] = [255, 0, 0]
    plt.imshow(img, plt.cm.gray)
    plt.show()


def ex_3():  # draw polygon
    img = data.chelsea()
    y = np.array([10, 10, 60, 60])
    x = np.array([200, 400, 400, 200])
    rr, cc = draw.polygon(y, x)
    img[rr, cc] = [255, 0, 0]
    plt.imshow(img, plt.cm.gray)
    plt.show()


def ex_4():  # draw ellipse
    img = data.chelsea()
    # rr, cc = draw.ellipse_perimeter(150, 150, 30, 80)
    rr, cc = draw.ellipse(150, 150, 30, 80)
    draw.set_color(img, [rr, cc], [255, 0, 0])
    plt.imshow(img, plt.cm.gray)
    plt.show()


def ex_5():  # draw bezier_curve
    img = data.chelsea()
    rr, cc = draw.bezier_curve(150, 50, 50, 280, 260, 400, 2)
    img[rr, cc] = [0, 255, 0]
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    ex_5()
