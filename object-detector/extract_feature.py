# extract
from .config1 import *
from skimage.feature import local_binary_pattern
from skimage.feature import hog
from skimage.io import imread
import Evaluate as eva
import Preprocess as pre
import Const
import argparse as ap
import glob
import os

# train
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib


def calculate_desciptors_pos(im):
    fd = hog(im, orientations, pixels_per_cell, cells_per_block, visualize, normalize)
    return fd


def train():
    fds = []
    labels = []
    clf_type = 'LIN_SVM'
    clf = LinearSVC()
    clf.fit(fds, labels)
    joblib.dump(clf, model_path)


if __name__ == '__main__':
    src_img = eva.load_image(Const.image1)
    calculate_desciptors_pos(src_img)
