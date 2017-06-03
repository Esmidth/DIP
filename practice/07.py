from skimage import transform, data
import matplotlib.pyplot as plt
import numpy as np


def ex_1():  # resize image to target size
    img = data.camera()
    dst = transform.resize(img, (80, 60))
    plt.figure('resize')

    plt.subplot(121)
    plt.title('origin')
    plt.imshow(img, plt.cm.gray)

    plt.subplot(122)
    plt.title('after')
    plt.imshow(dst, plt.cm.gray)

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
    ex_4()
