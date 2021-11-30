import math
import matplotlib.pyplot as plt


def distance(p1: tuple, p2: tuple) -> float:
    return math.dist(p1, p2)


def convert_tuple(tup):
    return [x for x, _ in tup], [y for _, y in tup]


def linear_plot_dev(val_x, val_y, title_x, title_y, title):
    plt.plot(val_x, val_y)
    plt.title(title)
    plt.xlabel(title_x)
    plt.ylabel(title_y)
    plt.show()


def symbol_plot_dev(val_x, val_y, symbol='x'):
    plt.plot(val_x, val_y, symbol)
    plt.axis('equal')
    plt.show()


def symbol_plot_dev_2(val_x1, val_y1, val_x2, val_y2, symbol1='rx', symbol2='gx'):
    plt.plot(val_x1, val_y1, symbol1, val_x2, val_y2, symbol2)
    plt.axis('equal')
    plt.show()


def symbol_plot_dev_3(val_x1, val_y1, val_x2, val_y2, val_x3, val_y3, val_x4, val_y4, symbol1='rx', symbol2='gx',
                      symbol3='y+', symbol4='b+'):
    plt.plot(val_x1, val_y1, symbol1, val_x2, val_y2, symbol2, val_x3, val_y3, symbol3, val_x4, val_y4, symbol4)
    plt.axis('equal')
    plt.show()


def closer_list(r1_value, r2_value, dataset_x, dataset_y, section=True):
    res = []
    for i in range(len(dataset_y)):
        d_x_r1 = distance(r1_value, (dataset_x[i], dataset_y[i]))
        d_x_r2 = distance(r2_value, (dataset_x[i], dataset_y[i]))
        if d_x_r1 < d_x_r2:
            if section:
                res.append((dataset_x[i], dataset_y[i]))
        else:
            if not section:
                res.append((dataset_x[i], dataset_y[i]))
    return res


def avg_points(p1, p2):
    return (p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0


def avg_points_node(p1, p2):
    pp1 = p1 if type(p1) == tuple else p1.data
    pp2 = p2 if type(p2) == tuple else p2.data
    return avg_points(pp1, pp2)


def distance_node(p1, p2):
    pp1 = p1 if type(p1) == tuple else p1.data
    pp2 = p2 if type(p2) == tuple else p2.data
    return distance(pp1, pp2)
