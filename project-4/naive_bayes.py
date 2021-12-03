import math

import matplotlib.pyplot as plt
import numpy as np

import util


def gain(dataset, d_entropy, dataset_spl_mean_1, dm1_entropy, dataset_spl_mean_2, dm2_entropy):
    return d_entropy - (dm1_entropy * dataset_spl_mean_1.shape[0] + dm2_entropy * dataset_spl_mean_2.shape[0]) / \
           dataset.shape[0]


def ex_3():
    dataset = util.get_file('iris.data')
    dataset_spl_mean_1, dataset_spl_mean_2 = util.index_dataframe(dataset)
    features = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    for feature in features:
        print(f'Feature: {feature}')
        d_entropy = entropy(dataset, feature)
        print(f'Entropy Dataset: {d_entropy}')
        dm1_entropy = entropy(dataset_spl_mean_1, feature)
        print(f'Entropy Sub_Dataset_1: {dm1_entropy}')
        dm2_entropy = entropy(dataset_spl_mean_2, feature)
        print(f'Entropy Sub_Dataset_2: {dm2_entropy}')
        gain_all = gain(dataset, d_entropy, dataset_spl_mean_1, dm1_entropy, dataset_spl_mean_2, dm2_entropy)
        print(f'Gain: {gain_all}')


def entropy(dataset, feature):
    d_p_plus, d_p_minus = util.split_dataframe_IRIS(dataset, feature)
    p_plus = d_p_plus.shape[0]
    p_minus = d_p_minus.shape[0]
    if p_plus == 0 and p_minus == 0:
        return 0
    elif p_plus == 0:
        return - p_minus * math.log2(p_minus)
    elif p_minus == 0:
        return - p_plus * math.log2(p_plus)
    else:
        return -1 * p_plus * math.log2(p_plus) - p_minus * math.log2(p_minus)


def ex_4():
    res = []
    dataset = util.get_file('iris.data')
    for i in range(10):
        train_dataset, test_dataset = util.split(util.apply_shuffle(dataset))
        current_nb = NB(train_dataset)
        df_label = test_dataset.iloc[:, -1].to_numpy()
        res.append((current_nb.estimate(test_dataset), df_label))
    matches = 0
    mismatch = 0
    for vv in res:
        for i in range(len(vv[0])):
            if vv[0][i] == vv[1][i]:
                matches += 1
            else:
                mismatch += 1
    mismatch = mismatch / len(res)
    matches = matches / len(res)
    # plot
    width = 0.35  # the width of the bars: can also be len(x) sequence
    # Matches
    fig, ax = plt.subplots()
    labels = ['naive bayes']
    ax.bar(labels, [matches], width)
    ax.set_ylabel('Number of times')
    ax.set_title('Matches')
    plt.show()
    # Mismatch
    fig, ax = plt.subplots()
    ax.bar(labels, [mismatch], width)
    ax.set_ylabel('Number of times')
    ax.set_title('Mismatches')
    plt.show()


class NB:
    def __init__(self, dataset):
        self.dataset = dataset.iloc[:, :-1]
        self.label = dataset.iloc[:, -1]
        self.unique_labels = np.unique(self.label)
        # auxiliary variables
        self.size_data, self.columns = self.dataset.shape
        self.number_labels = len(self.unique_labels)
        # statistics
        self.mean = np.zeros((self.number_labels, self.columns))
        self.variance = np.zeros((self.number_labels, self.columns))
        self.statistics = np.zeros((self.number_labels, self.columns))

        for column in range(self.columns):
            i = 0
            for current_label in self.unique_labels:
                df, _ = util.split_dataframe_IRIS(dataset, value=current_label)
                df = df.iloc[:, :-1]
                df = df[column]
                self.mean[i, column] = df.mean(axis=0)
                self.variance[i, column] = df.var(axis=0)
                self.statistics[i, column] = df.shape[0] / float(self.size_data)
                i += 1
        pass

    def estimate(self, dataset):
        df = dataset.iloc[:, :-1]
        return [self._estimate(value) for value in df.to_numpy()]

    def _estimate(self, value):
        statistics = []
        index = 0
        for _ in self.unique_labels:
            statistic = np.log(self.statistics[index])
            label_conditional = np.sum(np.log(self.gaussian_density(index, value)))
            statistics.append(statistic + label_conditional)
            index += 1
        return self.unique_labels[int(np.argmax(statistics) / self.columns)]

    def gaussian_density(self, class_idx, x):
        mean = self.mean[class_idx]
        var = self.variance[class_idx]
        numerator = np.exp((-1 / 2) * ((x - mean) ** 2) / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        prob = numerator / denominator
        return prob
