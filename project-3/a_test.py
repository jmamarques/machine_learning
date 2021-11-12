import generator as g
import random
import util
import distribution as d
import matplotlib.pyplot as plt

random.seed(1000)
c, x, y, label_1x, label_1y, label_2x, label_2y = g.gen_cases(False)
r1 = random.randint(0, len(x) - 1)
r2 = random.randint(0, len(x) - 1)
r1_value = (x[r1], y[r1])
r2_value = (x[r2], y[r2])
print("2 b)")
for i in range(3):
    print("Initial: r1 and r2")
    print(r1_value)
    print(r2_value)
    dist = d.Distribution(alpha=0.0001)
    r1_values_data, r2_values_data = dist.process_2_a(x, y, r1_value, r2_value)
    r1_x, r1_y = util.convert_tuple(r1_values_data)
    r2_x, r2_y = util.convert_tuple(r2_values_data)
    print("Final: r1 and r2")
    r1_t = (r1_x[len(r1_x) - 1], r1_y[len(r1_x) - 1])
    r2_t = (r2_x[len(r2_x) - 1], r2_y[len(r2_x) - 1])
    print(r1_t)
    print(r2_t)
    color_1_x, color_1_y = util.convert_tuple(util.closer_list(r1_t, r2_t, label_1x, label_1y))
    color_2_x, color_2_y = util.convert_tuple(util.closer_list(r1_t, r2_t, label_2x, label_2y))
    color_3_x, color_3_y = util.convert_tuple(util.closer_list(r1_t, r2_t, label_1x, label_1y, False))
    color_4_x, color_4_y = util.convert_tuple(util.closer_list(r1_t, r2_t, label_2x, label_2y, False))
    plt.plot(
        color_1_x, color_1_y, 'rx',
        color_2_x, color_2_y, 'gx',
        color_3_x, color_3_y, 'yx',
        color_4_x, color_4_y, 'bx',
        [r1_t[0]], [r1_t[1]], '+',
        [r2_t[0]], [r2_t[1]], '+')
    plt.axis('equal')
    plt.show()
    r1_value = r1_t
    r2_value = r2_t
