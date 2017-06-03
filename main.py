import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import io


def opencv_opt(src):
    cv2.imshow("FUCK", src)
    cv2.waitKey(0)


def plt_opt(src):
    plt.imshow(src, cmap="gray", interpolation='bicubic')
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == "__main__":
    print("FUCK")
    #    img1 = cv2.imread('./train/Train_BJ_001.jpg')
    img = io.imread('./train/Train_BJ_001.jpg')
    cv2.line(img, (0, 0), (511, 511), (0, 225, 0), 3)
    opencv_opt(img)
