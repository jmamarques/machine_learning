import numpy as np


def manhattan_distance(p1, p2):
    p1 = np.array(p1)
    p2 = np.array(p2)
    return np.sum(np.absolute(p1 - p2))


def euclidean_distance(p1, p2):
    p1 = np.array(p1)
    p2 = np.array(p2)
    sum_sq = np.sum(np.square(p1 - p2))
    return np.sqrt(sum_sq)


class KNN:
    def __init__(self, dataset, features):
        self.dataset = dataset.copy(deep=True)
        self.dataset.drop(['date'], axis=1, inplace=True, errors='ignore')
        self.features = features

    def estimate_position(self, vector, k, dist_func=manhattan_distance):
        distances = []
        for rssi_vector in self.dataset.values.tolist():
            x = rssi_vector[1]
            y = rssi_vector[2]
            distances += [(dist_func(rssi_vector[3:], vector), x, y)]

        distances = sorted(distances)

        # avg the k closest neighbours
        distances = distances[:k]
        sum_x = 0
        sum_y = 0
        for pos in distances:
            sum_x += pos[1]
            sum_y += pos[2]
        sum_x = sum_x / k
        sum_y = sum_y / k
        return sum_x, sum_y