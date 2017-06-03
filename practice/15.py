import skimage.transform as st
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, feature


def ex_1():  # Hough Transform
    image = np.zeros((100, 100))
    idx = np.arange(25, 75)
    image[idx[::-1], idx] = 255
    image[idx, idx] = 255

    h, theta, d = st.hough_line(image)
    fig, (ax0, ax1) = plt.subplots(1, 2)
    plt.tight_layout()

    ax0.imshow(image, plt.cm.gray)
    ax0.set_title('input')
    ax0.set_axis_off()

    ax1.imshow(np.log(1 + h))
    ax1.set_title('Hough')
    ax1.set_xlabel('Angles (degrees)')
    ax1.set_ylabel('Distance (pixels)')
    ax1.axis('image')

    plt.show()


def ex_2():  # Hough Transform Line Detection
    image = np.zeros((100, 100))
    idx = np.arange(25, 75)
    image[idx[::-1], idx] = 255
    image[idx, idx] = 255

    h, theta, d = st.hough_line(image)

    fig, (ax0, ax1, ax2) = plt.subplots(1, 3)
    plt.tight_layout()

    ax0.imshow(image, plt.cm.gray)
    ax0.set_title('input image')
    ax0.set_axis_off()

    ax1.imshow(np.log(1 + h))
    ax1.set_title('Hough transform')
    ax1.set_xlabel('Angles (degrees)')
    ax1.set_ylabel('Distance (pixels)')
    ax1.axis('image')

    ax2.imshow(image, plt.cm.gray)
    row1, col1 = image.shape
    for _, angle, dist in zip(*st.hough_line_peaks(h, theta, d)):
        y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
        y1 = (dist - col1 * np.cos(angle)) / np.sin(angle)
        ax2.plot((0, col1), (y0, y1), '-r')
    ax2.axis((0, col1, row1, 0))
    ax2.set_title('Detected')
    ax2.set_axis_off()

    plt.show()


def ex_3():  # Probabilistic Hough Transform
    image = data.camera()
    edges = feature.canny(image, sigma=2, low_threshold=1, high_threshold=25)
    lines = st.probabilistic_hough_line(edges, threshold=10, line_length=5, line_gap=3)

    fig, (ax0, ax1, ax2) = plt.subplots(1, 3)
    plt.tight_layout()

    ax0.imshow(image, plt.cm.gray)
    ax0.set_title('input')
    ax0.set_axis_off()

    ax1.imshow(edges, plt.cm.gray)
    ax1.set_title('canny edges')
    ax1.set_axis_off()

    ax2.imshow(edges * 0)
    for line in lines:
        p0, p1 = line
        ax2.plot((p0[0], p1[0]), (p0[1], p1[1]))
    row2, col2 = image.shape
    ax2.axis((0, col2, row2, 0))
    ax2.set_title('probabilistic')
    ax2.set_axis_off()

    plt.show()


if __name__ == '__main__':
    ex_3()
