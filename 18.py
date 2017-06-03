import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from skimage import data, color, morphology, feature, measure, filters, segmentation
import numpy as np
import scipy.ndimage as ndi


def ex_1():  # convex 凸包
    img = color.rgb2grey(data.horse())
    img = (img < 0.5) * 1

    chull = morphology.convex_hull_image(img)

    fig, axes = plt.subplots(1, 2)
    ax0, ax1 = axes.ravel()
    ax0.imshow(img, plt.cm.gray)
    ax0.set_title('origin')

    ax1.imshow(chull, plt.cm.gray)
    ax1.set_title('convex_hull image')
    plt.show()


def ex_2():  # similar to ex_1()
    img = color.rgb2grey(data.coins())
    edges = feature.canny(img, sigma=3, low_threshold=10, high_threshold=50)

    chull = morphology.convex_hull_object(edges)

    fig, axes = plt.subplots(1, 2)
    ax0, ax1 = axes.ravel()
    ax0.imshow(edges, plt.cm.gray)
    ax0.set_title('many')

    ax1.imshow(chull, plt.cm.gray)
    ax1.set_title('convex_hull image')
    plt.show()


def ex_3():  # label different connectivity regions
    def micro_structure(l=256):
        n = 5
        # x, y = np.ogrid[0:l, 0:l]
        mask = np.zeros((l, l))
        generator = np.random.RandomState(1)
        points = l * generator.rand(2, n ** 2)
        mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
        mask = ndi.gaussian_filter(mask, sigma=l / (4. * n))
        return mask > mask.mean()

    local_data = micro_structure(l=128) * 1
    labels = measure.label(local_data, connectivity=2)
    # connectivity 1 == 4 neighbours, 2 == 8 neighbours
    dst = color.label2rgb(labels)
    print('regions number:', labels.max() + 1)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(local_data, plt.cm.gray, interpolation='nearest')
    ax1.axis('off')
    ax2.imshow(dst, interpolation='nearest')
    ax2.axis('off')

    fig.tight_layout()
    plt.show()


def ex_4():  # delete small objects
    def micro_structure(l=256):
        n = 5
        # x, y = np.ogrid[0:l, 0:l]
        mask = np.zeros((l, l))
        generator = np.random.RandomState(1)
        points = l * generator.rand(2, n ** 2)
        mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
        mask = ndi.gaussian_filter(mask, sigma=l / (4. * n))
        return mask > mask.mean()

    data = micro_structure(l=128)
    dst = morphology.remove_small_objects(data, min_size=300, connectivity=1)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(data, plt.cm.gray, interpolation='nearest')
    ax2.imshow(dst, plt.cm.gray, interpolation='nearest')

    fig.tight_layout()
    plt.show()


def ex_5():
    image = data.coins()[50:-50, 50:-50]

    thresh = filters.threshold_otsu(image)
    bw = morphology.closing(image > thresh, morphology.square(3))

    cleared = bw.copy()


if __name__ == '__main__':
    ex_4()
