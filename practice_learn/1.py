from sklearn import datasets
from sklearn import svm
import numpy as np
from sklearn import random_projection
import matplotlib.pyplot as plt


def ex1():  # loading an example dataset
    iris = datasets.load_iris()
    digits = datasets.load_digits()
    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(digits.data[:-1], digits.target[:-1])


def ex2():  # Conventions: dtype
    rng = np.random.RandomState(0)
    X = rng.rand(10, 2000)
    X = np.array(X, dtype='float32')
    transformer = random_projection.GaussianRandomProjection()
    X_new = transformer.fit_transform(X)


def ex3():
    iris = datasets.load_iris()
    iris_X = iris.data
    iris_Y = iris.target
    np.unique(iris_Y)


def ex4():
    iris = datasets.load_iris()
    x = iris.data[:, :2]
    y = iris.target

    h = .02
    C = 1.0  # SVM regularization parameter
    svc = svm.SVC(kernel='linear', C=C).fit(x, y)
    rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(x, y)
    poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(x, y)
    lin_svc = svm.LinearSVC(C=C).fit(x, y)

    x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
    y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    titles = ['SVC with linear kernel', 'LinearSVC (linear kernel)', 'SVC with RBF kernel',
              'SVC with polynomial (degree 3) kernel']

    for i, clf in enumerate((svc, lin_svc, rbf_svc, poly_svc)):
        plt.subplot(2, 2, i + 1)
        plt.subplots_adjust(wspace=0.4, hspace=0.4)

        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)

        plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.coolwarm)
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.xticks(())
        plt.yticks(())
        plt.title(titles[i])
    plt.show()


if __name__ == '__main__':
    ex4()
