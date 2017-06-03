import numpy as np
import matplotlib.pyplot as plt
from skimage import draw, transform, feature, color, util, data


def ex_1():  # Detect circle in img & draw them in images
    img = np.zeros((250, 250, 3), dtype=np.uint8)
    rr, cc = draw.circle_perimeter(60, 60, 50)
    rr1, cc1 = draw.circle_perimeter(150, 150, 60)
    img[cc, rr, :] = 255
    img[cc1, rr1, :] = 255

    fig, (ax0, ax1) = plt.subplots(1, 2)

    ax0.imshow(img)
    ax0.set_title('origin')

    hough_radii = np.arange(50, 80, 5)
    hough_res = transform.hough_circle(img[:, :, 0], hough_radii)

    centers = []
    accums = []
    radii = []

    for radius, h in zip(hough_radii, hough_res):
        num_peaks = 2
        peaks = feature.peak_local_max(h, num_peaks=num_peaks)
        centers.extend(peaks)
        accums.extend(h[peaks[:, 0], peaks[:, 1]])
        radii.extend([radius] * num_peaks)

    image = np.copy(img)
    for idx in np.argsort(accums)[::-1][:2]:
        center_x, center_y = centers[idx]
        radius = radii[idx]
        cx, cy = draw.circle_perimeter(center_y, center_x, radius)
        image[cy, cx] = (255, 0, 0)
    ax1.imshow(image)
    ax1.set_title('detected image')

    plt.show()


def ex_2():
    image = util.img_as_ubyte(data.coins()[0:95, 70:370])
    edges = feature.canny(image, sigma=3, low_threshold=10, high_threshold=50)

    fig, (ax0, ax1) = plt.subplots(1, 2)

    ax0.imshow(edges, cmap=plt.cm.gray)
    ax0.set_title('origin')

    hough_radii = np.arange(15, 30, 2)
    hough_res = transform.hough_circle(edges, hough_radii)

    centers = []
    accums = []
    radii = []

    for radius, h in zip(hough_radii, hough_res):
        num_peaks = 2
        peaks = feature.peak_local_max(h, num_peaks=num_peaks)
        centers.extend(peaks)
        accums.extend(h[peaks[:, 0], peaks[:, 1]])
        radii.extend([radius] * num_peaks)

    image = color.gray2rgb(image)
    for idx in np.argsort(accums)[::-1][:5]:
        center_x, center_y = centers[idx]
        radius = radii[idx]
        cx, cy = draw.circle_perimeter(center_y, center_x, radius)
        image[cy, cx] = (255, 0, 0)
    ax1.imshow(image)
    ax1.set_title('detected image')

    plt.show()


def ex_3():
    image_rgb = data.coffee()[0:220, 160:420]
    image_gray = color.rgb2grey(image_rgb)
    edges = feature.canny(image_gray, sigma=2.0, low_threshold=0.55, high_threshold=0.8)

    result = transform.hough_ellipse(edges, accuracy=20, threshold=250, min_size=100, max_size=120)
    result.sort(order='accumulator')

    best = list(result[-1])
    yc, xc, a, b = [int(round(x)) for x in best[1:5]]
    orientation = best[5]

    cy, cx = draw.ellipse_perimeter(yc, xc, a, b, orientation)
    image_rgb[cy, cx] = (0, 0, 255)

    edges = color.gray2rgb(edges)
    edges[cy, cx] = (250, 0, 0)

    fig2, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(8, 4))
    ax1.set_title('Origin')
    ax1.imshow(image_rgb)

    ax2.set_title('Edge (white) and result (red)')
    ax2.imshow(edges)

    plt.show()


if __name__ == "__main__":
    ex_3()
