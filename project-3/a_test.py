import generator as g
import random
import clustering as clu
import util
import const
import matplotlib.pyplot as plt

random.seed(1000)
c, x, y, label_1x, label_1y, label_2x, label_2y = g.gen_cases(True)
data_set = [(x[i], y[i]) for i in range(len(x))]
va = clu.Cluster(0.5)
va.fit(data_set)
vx, vy = util.convert_tuple(va.without_cluster)
plt.plot(vx, vy, '+')
for i in range(len(va.cluster)):
    vx, vy = util.convert_tuple(va.cluster[i])
    plt.plot(vx, vy, const.COLORS[i])
plt.axis('equal')
plt.show()
print(va.cluster)
print(len(va.cluster))
