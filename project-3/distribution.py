import random
import util

#######################
# STATICS
####################


def init_rule(dataset_x, dataset_y, r1_value=None, r2_value=None):
    if r1_value is None and r2_value is None:
        r2 = random.randint(0, len(dataset_x) - 1)
        r1 = random.randint(0, len(dataset_x) - 1)
        r1_value = (dataset_x[r1], dataset_y[1])
        r2_value = (dataset_x[r2], dataset_y[r2])
    r1_values_data = []
    r2_values_data = []
    r1_values_data.append(r1_value)
    r2_values_data.append(r2_value)
    return r1_value, r1_values_data, r2_value, r2_values_data

#######################
# CLASS
####################


class Distribution:
    alpha: float
    d: float

    def __init__(self, alpha=10E-5) -> None:
        super().__init__()
        self.alpha = alpha
        self.d = 0.0

    def process(self, dataset_x, dataset_y, r1_value=None, r2_value=None):
        if len(dataset_x) != len(dataset_y):
            raise ValueError("invalid dataset - do not have the same size")
        # random 2 points
        if r1_value is None and r2_value is None:
            r1 = random.randint(0, len(dataset_x) - 1)
            r2 = random.randint(0, len(dataset_x) - 1)
            r1_value = (dataset_x[r1], dataset_y[r1])
            r2_value = (dataset_x[r2], dataset_y[r2])

        for i in range(len(dataset_y)):
            d_x_r1 = util.distance(r1_value, (dataset_x[i], dataset_y[i]))
            d_x_r2 = util.distance(r2_value, (dataset_x[i], dataset_y[i]))
            if d_x_r1 < d_x_r2:
                r1_value = (self.__calc(r1_value[0], dataset_x[i]), self.__calc(r1_value[1], dataset_y[i]))
            elif d_x_r2 < d_x_r1:
                r2_value = (self.__calc(r2_value[0], dataset_x[i]), self.__calc(r2_value[1], dataset_y[i]))
        return r1_value, r2_value, dataset_x, dataset_y

    #######################
    # CALC
    ####################

    def __calc(self, r, x):
        return (1 - self.alpha) * r + self.alpha * x

    def __calc2(self, r, x, n, update):
        res = r + (self.alpha / n) * self.d
        if update:
            self.d = self.d + (x - r)
        return res

    #######################
    # PROCESS
    ####################

    def process_1_a(self, dataset_x, dataset_y, r1_value=None, r2_value=None):
        r1_value, r1_values_data, r2_value, r2_values_data = init_rule(dataset_x, dataset_y, r1_value, r2_value)

        self.rule_1x(dataset_x, dataset_y, r1_value, r1_values_data, r2_value, r2_values_data)

        return r1_values_data, r2_values_data

    def process_1_b(self, dataset_x, dataset_y, r1_value=None, r2_value=None):
        r1_value, r1_values_data, r2_value, r2_values_data = init_rule(dataset_x, dataset_y, r1_value, r2_value)
        for _ in range(10):
            self.rule_1x(dataset_x, dataset_y, r1_value, r1_values_data, r2_value, r2_values_data)

        return r1_values_data, r2_values_data

    def process_2_a(self, dataset_x, dataset_y, r1_value=None, r2_value=None):
        r1_value, r1_values_data, r2_value, r2_values_data = init_rule(dataset_x, dataset_y, r1_value, r2_value)
        for i in range(10):
            self.rule_2x(dataset_x, dataset_y, r1_value, r1_values_data, r2_value, r2_values_data, i)

        return r1_values_data, r2_values_data

    #######################
    # RULES
    ####################

    def rule_1x(self, dataset_x, dataset_y, r1_value, r1_values_data, r2_value, r2_values_data):
        for i in range(len(dataset_y)):
            d_x_r1 = util.distance(r1_value, (dataset_x[i], dataset_y[i]))
            d_x_r2 = util.distance(r2_value, (dataset_x[i], dataset_y[i]))
            if d_x_r1 < d_x_r2:
                r1_value = (self.__calc(r1_value[0], dataset_x[i]), self.__calc(r1_value[1], dataset_y[i]))
                r1_values_data.append(r1_value)
            elif d_x_r2 < d_x_r1:
                r2_value = (self.__calc(r2_value[0], dataset_x[i]), self.__calc(r2_value[1], dataset_y[i]))
                r2_values_data.append(r2_value)

    def rule_2x(self, dataset_x, dataset_y, r1_value, r1_values_data, r2_value, r2_values_data, i=0):
        for i in range(len(dataset_y)):
            d_x_r1 = util.distance(r1_value, (dataset_x[i], dataset_y[i]))
            d_x_r2 = util.distance(r2_value, (dataset_x[i], dataset_y[i]))
            if d_x_r1 < d_x_r2:
                r1_value = (self.__calc2(r1_value[0], dataset_x[i], len(dataset_y), i != 0),
                            self.__calc2(r1_value[1], dataset_y[i], len(dataset_y), i != 0))
                r1_values_data.append(r1_value)
            elif d_x_r2 < d_x_r1:
                r2_value = (self.__calc2(r2_value[0], dataset_x[i], len(dataset_y), i != 0),
                            self.__calc2(r2_value[1], dataset_y[i], len(dataset_y), i != 0))
                r2_values_data.append(r2_value)
