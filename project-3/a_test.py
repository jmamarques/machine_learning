import generator as g
import random
import clustering as clu
import util
import const
import matplotlib.pyplot as plt
import agglomerative as ag

random.seed(1000)
c, x, y, label_1x, label_1y, label_2x, label_2y = g.gen_cases(True, 50)
data_set = [(x[i], y[i]) for i in range(len(x))]
node = ag.agglomerative(data_set)
print(node)
