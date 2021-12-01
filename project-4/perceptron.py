import random
import statistics as s
import matplotlib.pyplot as plt


def calculation(w0, w1, w2, x1, x2):
    return w0 + w1 * x1 + w2 * x2


def f(function, x1, x2):
    value = function(x1, x2)
    return 1 if value > 0 else 0


def ex_1():
    vector = [[0, 0], [0, 1], [1, 0], [1, 1]]
    or_expected_results = [0, 1, 1, 1]
    w0, w1, w2 = 0, 0.3, 0.3
    calculation_f = lambda x1, x2: calculation(w0, w1, w2, x1, x2)
    results = []
    for list in vector:
        results.append(f(calculation_f, list[0], list[1]))
    print(f'W0:{w0} W1:{w1} W2:{w2}')
    for i in range(len(results)):
        print(f'X1:{vector[i][0]} X2:{vector[i][1]} OR:{or_expected_results[i]} Result:{results[i]}')
    return results, vector


def ex_2():
    vector = [[0, 0], [0, 1], [1, 0], [1, 1]]
    or_expected_results = [0, 1, 1, 1]
    w0, w1, w2 = random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)
    calculation_f = lambda x1, x2: calculation(w0, w1, w2, x1, x2)
    results = []
    for list in vector:
        results.append(f(calculation_f, list[0], list[1]))
    print(f'W0:{w0} W1:{w1} W2:{w2}')
    for i in range(len(results)):
        print(f'X1:{vector[i][0]} X2:{vector[i][1]} OR:{or_expected_results[i]} Result:{results[i]}')
    return results, vector


def ex_3(w0=random.uniform(0, 1), w1=random.uniform(0, 1), w2=random.uniform(0, 1)):
    vector = [[0, 0], [0, 1], [1, 0], [1, 1]]
    or_expected_results = [0, 1, 1, 1]
    calculation_f = lambda x1, x2: calculation(w0, w1, w2, x1, x2)
    results = []
    for list in vector:
        results.append(f(calculation_f, list[0], list[1]))
    print(f'W0:{w0} W1:{w1} W2:{w2}')
    differences = []
    for i in range(len(results)):
        differences.append(or_expected_results[i] - results[i])
        print(f'X1:{vector[i][0]} X2:{vector[i][1]} OR:{or_expected_results[i]} Result:{results[i]} '
              f'Difference:{differences[i]}')
    return differences


def ex_4(w0=random.uniform(0, 1), w1=random.uniform(0, 1), w2=random.uniform(0, 1)):
    x = 10e-4
    vector = [[0, 0], [0, 1], [1, 0], [1, 1]]
    or_expected_results = [0, 1, 1, 1]
    calculation_f = lambda x1, x2: calculation(w0, w1, w2, x1, x2)
    results = []
    for list in vector:
        results.append(f(calculation_f, list[0], list[1]))
    print(f'W0:{w0} W1:{w1} W2:{w2}')
    differences = []
    res = []
    for i in range(len(results)):
        differences.append(or_expected_results[i] - results[i])
        res.append(
            (w0 + x * differences[i], w1 + x * vector[i][0] * differences[i], w2 + x * vector[i][1] * differences[i]))
        print(f'X1:{vector[i][0]} X2:{vector[i][1]} OR:{or_expected_results[i]} Result:{results[i]} '
              f'∆w0:{res[i][0]} ∆w1:{res[i][1]} ∆w2:{res[i][2]}')
    return res


def ex_5(w0=random.uniform(0, 1), w1=random.uniform(0, 1), w2=random.uniform(0, 1), index=0, x=10e-4):
    if index == 0:
        print(f'Initial: W0:{w0} W1:{w1} W2:{w2}')
    vector = [[0, 0], [0, 1], [1, 0], [1, 1]]
    or_expected_results = [0, 1, 1, 1]
    calculation_f = lambda x1, x2: calculation(w0, w1, w2, x1, x2)
    results = []
    for list in vector:
        results.append(f(calculation_f, list[0], list[1]))
    differences = []
    res = []
    last_w0, last_w1, last_w2 = 0, 0, 0
    finished = False
    for i in range(len(results)):
        differences.append(or_expected_results[i] - results[i])
        res.append(
            (w0 + x * differences[i], w1 + x * vector[i][0] * differences[i], w2 + x * vector[i][1] * differences[i]))
        first = finished
        finished = finished or w0 != res[i][0] or w1 != res[i][1] or w2 != res[i][2]
        if not first and finished:
            last_w0, last_w1, last_w2 = res[i][0], res[i][1], res[i][2]

    if finished:
        new_index = index + 1
        return ex_5(last_w0, last_w1, last_w2, new_index, x)
    else:
        print(f'Final: W0:{w0} W1:{w1} W2:{w2}')
        for i in range(len(results)):
            print(f'X1:{vector[i][0]} X2:{vector[i][1]} OR:{or_expected_results[i]} Result:{results[i]} '
                  f'∆w0:{res[i][0]} ∆w1:{res[i][1]} ∆w2:{res[i][2]}')

    return index


def ex_5a(x=10e-4):
    res = []
    for i in range(30):
        print(f'Attempt {i + 1}:')
        val = ex_5(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), 0, x)
        res.append(val)
        print(f'Result {val}')

    print(f'Statistics:')
    standard_deviation: float = s.stdev(res)
    average = s.mean(res)
    print(f"Average : {average}\n"
          f"Standard-deviation: {standard_deviation}\n")
    return average, standard_deviation, res


def ex_5b():
    iterations = list(range(1, 31))
    res = list()
    x_values = [10e-4, 10e-3, 10e-2, 10e-1]
    for x in x_values:
        res.append(ex_5a(x)[2])
    i=1
    for r in res:
        plt.boxplot(r)
        plt.title(f'Attempt {i} x={float(x_values[i-1])}')
        plt.show()
        i += 1
