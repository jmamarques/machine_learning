import util
import math


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
