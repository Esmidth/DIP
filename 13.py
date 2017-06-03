from skimage import data, color
import skimage.morphology as sm
import matplotlib.pyplot as plt


def ex_1():  # dilation
    img = data.checkerboard()
    img = color.rgb2gray(img)
    dst1 = sm.dilation(img, sm.square(5))
    dst2 = sm.dilation(img, sm.square(15))
    # sm.square & disk & ball & cube & diamond & rectangle & star & octagon & octahedron

    # if img is a binary image, use sm.binary_dilation(image,selem=None)

    plt.figure('morphology')
    plt.subplot(221)
    plt.title('origin')
    plt.imshow(img, plt.cm.gray)

    plt.subplot(222)
    plt.title('square = 5')
    plt.imshow(dst1, plt.cm.gray)

    plt.subplot(223)
    plt.title('square = 15')
    plt.imshow(dst2, plt.cm.gray)

    dif = dst1 - dst2
    plt.subplot(224)
    plt.title('diff')
    plt.imshow(dif, plt.cm.gray)
    plt.show()


def ex_2():  # erosion
    img = data.checkerboard()
    dst1 = sm.erosion(img, sm.square(5))
    dst2 = sm.erosion(img, sm.square(25))

    plt.figure('morphology')
    plt.subplot(131)
    plt.title('origin')
    plt.imshow(img, plt.cm.gray)

    plt.subplot(132)
    plt.title('sm = 5')
    plt.imshow(dst1, plt.cm.gray)

    plt.subplot(133)
    plt.title('sm = 25')
    plt.imshow(dst2, plt.cm.gray)

    plt.show()


def ex_3():  # opening operation
    img = color.rgb2gray(data.checkerboard())
    dst = sm.opening(img, sm.disk(9))

    plt.figure('morphology')
    plt.subplot(121)
    plt.title('origin')
    plt.imshow(img, plt.cm.gray)
    plt.axis('off')

    plt.subplot(122)
    plt.title('sm.disk = 9')
    plt.imshow(dst, plt.cm.gray)
    plt.axis('off')

    plt.show()


def ex_4():  # closing operation
    img = color.rgb2gray(data.checkerboard())
    dst = sm.closing(img, sm.disk(9))

    plt.figure('fuck')
    plt.subplot(121)
    plt.title('origin')
    plt.imshow(img, plt.cm.gray)
    plt.axis('off')

    plt.subplot(122)
    plt.title('sm.disk = 9')
    plt.imshow(dst, plt.cm.gray)
    plt.axis('off')

    plt.show()


def ex_5():  # white top hat
    img = color.rgb2gray(data.checkerboard())
    dst = sm.white_tophat(img, sm.square(21))

    plt.figure('fuck')
    plt.subplot(121)
    plt.title('origin')
    plt.imshow(img, plt.cm.gray)
    plt.axis('off')

    plt.subplot(122)
    plt.title('sm.square = 21')
    plt.imshow(dst, plt.cm.gray)
    plt.axis('off')

    plt.show()


def ex_6():  # black top hat
    img = color.rgb2gray(data.checkerboard())
    dst = sm.black_tophat(img, sm.square(21))

    plt.figure('fuck')
    plt.subplot(121)
    plt.title('origin')
    plt.imshow(img, plt.cm.gray)
    plt.axis('off')

    plt.subplot(122)
    plt.title('sm.square = 21')
    plt.imshow(dst, plt.cm.gray)
    plt.axis('off')

    plt.show()


if __name__ == "__main__":
    ex_6()
