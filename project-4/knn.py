import numpy as np
from collections import Counter
import util


def vote(distances, index):
    counter_vote = None
    dictionary = dict()
    for value in distances:
        dictionary[value[1][index]] = 0
    keys: list = list(dictionary.keys())
    values = []
    for i in range(len(keys)):
        values.append(0)
    for value in distances:
        indexx = keys.index(value[1][index])
        values[indexx] = values[indexx] + 1

    return keys[np.argmax(values)]


def ex_2():
    res = dict()
    k_test = [3, 7, 11]
    dataset = util.get_file('iris.data')
    for k in k_test:
        res[k] = []
        for i in range(10):
            train_dataset, test_dataset = util.split(util.apply_shuffle(dataset))
            current_knn = KNN(test_dataset)
            res[k].append(current_knn.estimate_label(train_dataset, k))


class KNN:
    def __init__(self, dataset):
        self.dataset = dataset.copy(deep=True)

    def estimate_label(self, train_dataset, k):
        res = []

        for test_value in self.dataset.values.tolist():
            distances = []
            for rssi_vector in train_dataset.values.tolist():
                current_distance = 0
                # without label
                for col in range(len(rssi_vector) - 1):
                    current_distance += (rssi_vector[col] - test_value[col]) ** 2
                distances.append((np.sqrt(current_distance), rssi_vector))

            distances = sorted(distances)
            # avg the k closest neighbours
            distances = distances[:k]
            # vote
            label = vote(distances, len(test_value) - 1)
            # prediction, real value
            res.append((label, test_value[len(test_value) - 1]))

        return res


ex_2()
