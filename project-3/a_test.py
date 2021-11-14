import random

import agglomerative as ag
import generator as g

random.seed(1000)
c, x, y, label_1x, label_1y, label_2x, label_2y = g.gen_cases(True, 200)
data_set = [(x[i], y[i]) for i in range(len(x))]
node = ag.agglomerative(data_set)
node.print_tree()

