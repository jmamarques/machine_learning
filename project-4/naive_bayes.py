import util
import math
import matplotlib.pyplot as plt


def gain(dataset, d_entropy, dataset_spl_mean_1, dm1_entropy, dataset_spl_mean_2, dm2_entropy):
    return d_entropy - (dm1_entropy * dataset_spl_mean_1.shape[0] + dm2_entropy * dataset_spl_mean_2.shape[0]) / dataset.shape[0]


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


def ex_2():
    res = []
    dataset = util.get_file('iris.data')
    for i in range(10):
        train_dataset, test_dataset = util.split(util.apply_shuffle(dataset))
        current_nb = NB(test_dataset)
        res.append(current_nb.estimate_label(train_dataset))
    matches = 0
    mismatch = 0
    for vv in res:
        if vv[0] == vv[1]:
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
        self.dataset = dataset.copy(deep=True)

    def estimate_label(self, train_dataset):
        pass
