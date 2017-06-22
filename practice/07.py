from skimage import transform, data
import matplotlib.pyplot as plt
import numpy as np
import Train
import Evaluate as eva
import Preprocess as pre


def ex_1():  # resize image to target size
    img = data.camera()
    size1 = transform.resize(img, (200, 200))
    fd1, hog1 = Train.compute_hog(size1)
    size2 = transform.resize(size1, (1024, 1024))
    fd2, hog2 = Train.compute_hog(size2)
    plt.figure('resize')

    plt.subplot(231)
    plt.title('origin')
    plt.imshow(size1, plt.cm.gray)

    plt.subplot(234)
    plt.title('after')
    plt.imshow(size2, plt.cm.gray)

    plt.subplot(232)
    plt.title('hog1')
    plt.imshow(hog1, plt.cm.gray)

    plt.subplot(235)
    plt.title('hog2')
    plt.imshow(hog2, plt.cm.gray)

    plt.subplot(233)
    plt.title('hog1')
    n, bins, patches = plt.hist(hog1.flatten(), bins=180, normed=1, edgecolor='None', facecolor='red')

    plt.subplot(236)
    plt.title('hog2')
    n, bins, patches = plt.hist(hog2.flatten(), bins=180, normed=1, edgecolor='None', facecolor='red')

    plt.show()


def ex_2():  # resize image to target scale
    img = data.camera()
    print(img.shape)
    print(transform.rescale(img, 0.1).shape)
    print(transform.rescale(img, [0.5, 0.25]).shape)
    print(transform.rescale(img, 2).shape)


def ex_3():  # rotating image would
    img = data.camera()
    print(img.shape)
    img1 = transform.rotate(img, 60)
    print(img1.shape)
    img2 = transform.rotate(img, 30, resize=True)
    print(img2.shape)

    plt.figure('resize')

    plt.subplot(1, 2, 1)
    plt.title('rotate 60')
    plt.imshow(img1, plt.cm.gray)

    plt.subplot(122)
    plt.title('rotate 30')
    plt.imshow(img2, plt.cm.gray)

    plt.show()


def ex_4():
    image = data.astronaut()  # 载入宇航员图片
    rows, cols, dim = image.shape  # 获取图片的行数，列数和通道数
    pyramid = tuple(transform.pyramid_gaussian(image, downscale=2))  # 产生高斯金字塔图像

    composite_image = np.ones((rows, cols + cols / 2, 3), dtype=np.double)  # 生成背景

    composite_image[:rows, :cols, :] = pyramid[0]  # 融合原始图像

    i_row = 0
    for p in pyramid[1:]:
        n_rows, n_cols = p.shape[:2]
        composite_image[i_row:i_row + n_rows, cols:cols + n_cols] = p  # 循环融合9幅金字塔图像
        i_row += n_rows

    plt.imshow(composite_image)
    plt.show()


if __name__ == "__main__":
    ex_1()
