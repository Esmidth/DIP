import matplotlib.pyplot as plt
import Evaluate as eva
import Preprocess as pp
import Const

from skimage.feature import hog
from skimage import data, color, exposure


def compute_hog(image=data.astronaut()):
    image = color.rgb2grey(image)
    # image = color.rgb2grey(data.astronaut())
    fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualise=True)
    fig, (ax1, ax2) = plt.subplots(1, 2, sharex='all', sharey='all')

    ax1.axis('off')
    ax1.imshow(image, cmap=plt.cm.gray)
    ax1.set_title('input')
    ax1.set_adjustable('box-forced')

    hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 0.02))

    ax2.axis('off')
    ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
    ax2.set_title('Histogram of Oriented Gradients')
    ax2.set_adjustable('box-forced')

    plt.show()


def test_compute_hog():
    img = eva.load_image(Const.image + '2.jpg')
    compute_hog(img)


if __name__ == '__main__':
    test_compute_hog()
