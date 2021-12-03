import numpy as np
import matplotlib.pyplot as plt
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
    statistic = dict()
    k_test = [3, 7, 11]
    dataset = util.get_file('iris.data')
    for k in k_test:
        res[k] = []
        for i in range(10):
            train_dataset, test_dataset = util.split(util.apply_shuffle(dataset))
            current_knn = KNN(test_dataset)
            res[k].append(current_knn.estimate_label(train_dataset, k))
        values = res[k]
        matches = 0
        mismatch = 0
        for v in values:
            for vv in v:
                if vv[0] == vv[1]:
                    matches += 1
                else:
                    mismatch += 1
        statistic[k] = (matches / len(values), mismatch / len(values))
    # prepare data for plot
    matches_list = []
    mismatch_list = []
    for k in k_test:
        matches, mismatch = statistic[k]
        matches_list.append(matches)
        mismatch_list.append(mismatch)

    width = 0.35  # the width of the bars: can also be len(x) sequence
    # Matches
    fig, ax = plt.subplots()
    labels = ['k=3', 'k=7', 'k=11']
    ax.bar(labels, matches_list, width)
    ax.set_ylabel('Number of times')
    ax.set_title('Matches')
    plt.show()
    # Mismatch
    fig, ax = plt.subplots()
    labels = ['k=3', 'k=7', 'k=11']
    ax.bar(labels, mismatch_list, width)
    ax.set_ylabel('Number of times')
    ax.set_title('Mismatches')
    plt.show()


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
