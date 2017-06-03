from skimage import morphology, draw, color, data, feature, filters
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
from scipy import ndimage as ndi


def ex_1():  # 骨架提取 morphology.skeletonize()
    image = np.zeros((400, 400))
    image[10:-10, 10:100] = 1
    image[-100:-10, 10:-10] = 1
    image[10:-10, -100:-10] = 1

    rs, cs = draw.line(250, 150, 10, 280)
    for i in range(10):
        image[rs + i, cs] = 1
    rs, cs = draw.line(10, 150, 250, 280)
    for i in range(20):
        image[rs + i, cs] = 1

    ir, ic = np.indices(image.shape)
    circle1 = (ic - 135) ** 2 + (ir - 150) ** 2 < 30 ** 2
    circle2 = (ic - 135) ** 2 + (ir - 150) ** 2 < 20 ** 2
    image[circle1] = 1
    image[circle2] = 0

    skeleton = morphology.skeletonize(image)

    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.imshow(image, cmap=plt.cm.gray)
    ax1.axis('off')
    ax1.set_title('original')

    ax2.imshow(skeleton, plt.cm.gray)
    ax2.axis('off')
    ax2.set_title('skeleton')

    fig.tight_layout()
    plt.show()


def ex_2():  # 骨架提取2  morphology.skeletonize()
    image = color.rgb2grey(data.horse())
    image = 1 - image

    skeleton = morphology.skeletonize(image)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(image, plt.cm.gray)
    ax1.axis('off')
    ax1.set_title('origin')

    ax2.imshow(skeleton, plt.cm.gray)
    ax2.axis('off')
    ax1.set_title('skeleton')

    fig.tight_layout()
    plt.show()


def ex_3():  # 骨架提取3 morphology.medial_axis()
    def micro_structure(l=256):
        n = 5
        # x, y = np.ogrid[0:l, 0:l]
        mask = np.zeros((l, l))
        generator = np.random.RandomState(1)
        points = l * generator.rand(2, n ** 2)
        mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
        mask = ndi.gaussian_filter(mask, sigma=l / (4. * n))
        return mask > mask.mean()

    data = micro_structure(l=64)
    skel, distance = morphology.medial_axis(data, return_distance=True)

    dist_on_skel = distance * skel

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(data, plt.cm.gray, interpolation='nearest')
    ax2.imshow(dist_on_skel, plt.cm.spectral, interpolation='nearest')
    ax2.contour(data, [0.5], colors='w')

    fig.tight_layout()
    plt.show()


def ex_4():  # 分水岭算法,基于距离变换 feature.peak_local_max() & morphology.watershed()
    """
    分水岭在地理学上就是指一个山脊，水通常会沿着山脊的两边流向不同的“汇水盆”。
    分水岭算法是一种用于图像分割的经典算法，是基于拓扑理论的数学形态学的分割方法。
    如果图像中的目标物体是连在一起的，则分割起来会更困难，分水岭算法经常用于处理这类问题，通常会取得比较好的效果。
    分水岭算法可以和距离变换结合，寻找“汇水盆地”和“分水岭界限”，从而对图像进行分割。
    二值图像的距离变换就是每一个像素点到最近非零值像素点的距离，我们可以使用scipy包来计算距离变换。
    在下面的例子中，需要将两个重叠的圆分开。
    我们先计算圆上的这些白色像素点到黑色背景像素点的距离变换，
    选出距离变换中的最大值作为初始标记点（如果是反色的话，则是取最小值），
    从这些标记点开始的两个汇水盆越集越大，
    最后相交于分山岭。从分山岭处断开，我们就得到了两个分离的圆。
    """
    x, y = np.indices((80, 80))
    x1, y1, x2, y2 = 28, 28, 44, 52
    r1, r2 = 16, 20
    mask_circle1 = (x - x1) ** 2 + (y - y1) ** 2 < r1 ** 2
    mask_circle2 = (x - x2) ** 2 + (y - y2) ** 2 < r2 ** 2
    image = np.logical_or(mask_circle1, mask_circle2)

    distance = ndi.distance_transform_edt(image)
    local_maxi = feature.peak_local_max(distance, indices=False, footprint=np.ones((3, 3)), labels=image)
    markers = ndi.label(local_maxi)[0]
    labels = morphology.watershed(-distance, markers, mask=image)

    fig, axes = plt.subplots(2, 2)
    axes = axes.ravel()
    ax0, ax1, ax2, ax3 = axes

    ax0.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
    ax0.set_title("Original")
    ax1.imshow(-distance, cmap=plt.cm.jet, interpolation='nearest')
    ax1.set_title("Distance")
    ax2.imshow(markers, cmap=plt.cm.spectral, interpolation='nearest')
    ax2.set_title("Markers")
    ax3.imshow(labels, cmap=plt.cm.spectral, interpolation='nearest')
    ax3.set_title("Segmented")

    for ax in axes:
        ax.axis("off")

    fig.tight_layout()

    plt.show()


def ex_5():  # 分水岭算法，基于梯度
    image = color.rgb2gray(data.camera())
    denoised = filters.rank.median(image, morphology.disk(2))

    markers = filters.rank.gradient(denoised, morphology.disk(5)) < 10
    markers = ndi.label(markers)[0]

    gradient = filters.rank.gradient(denoised, morphology.disk(2))
    labels = morphology.watershed(gradient, markers, mask=image)

    fig, axes = plt.subplots(2, 2)
    axes = axes.ravel()
    ax0, ax1, ax2, ax3 = axes

    ax0.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
    ax0.set_title("Original")
    ax1.imshow(gradient, cmap=plt.cm.spectral, interpolation='nearest')
    ax1.set_title("Distance")
    ax2.imshow(markers, cmap=plt.cm.spectral, interpolation='nearest')
    ax2.set_title("Markers")
    ax3.imshow(labels, cmap=plt.cm.spectral, interpolation='nearest')
    ax3.set_title("Segmented")

    for ax in axes:
        ax.axis('off')

    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    ex_5()
