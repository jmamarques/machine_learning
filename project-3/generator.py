import matplotlib.pyplot as plt
import numpy as np
import random


def gen_cases(show_plot=False):
    mean = [3, 3]
    cov = [[1, 0], [0, 1]]
    a = np.random.multivariate_normal(mean, cov, 500).T
    mean = [-3, -3]
    cov = [[2, 0], [0, 5]]
    b = np.random.multivariate_normal(mean, cov, 500).T
    c = np.concatenate((a, b), axis=1)
    c = c.T
    np.random.shuffle(c)
    c = c.T
    x = c[0]
    y = c[1]
    if show_plot:
        plt.plot(x, y, 'x')
        plt.axis('equal')
        plt.show()
    label_1x = []
    label_1y = []
    label_2x = []
    label_2y = []
    for i in range(len(x)):
        if x[i] > 0 and y[i] > 0:
            label_1x.append(x[i])
            label_1y.append(y[i])
        else:
            label_2x.append(x[i])
            label_2y.append(y[i])

    return c, x, y, label_1x, label_1y, label_2x, label_2y
