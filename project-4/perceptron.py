import random


def calculation(w0, w1, w2, x1, x2):
    return w0 + w1 * x1 + w2 * x2


def f(function, x1, x2):
    value = function(x1, x2)
    return 1 if value > 0 else 0


def ex_1():
    vector = [[0, 0], [0, 1], [1, 0], [1, 1]]
    w0, w1, w2 = 0, 0.3, 0.3
    calculation_f = lambda x1, x2: calculation(w0, w1, w2, x1, x2)
    results = []
    for list in vector:
        results.append(f(calculation_f, list[0], list[1]))
    print(f'W0:{w0} W1:{w1} W2:{w2}')
    for i in range(len(results)):
        print(f'X1:{vector[i][0]} X2:{vector[i][1]} Result:{results[i]}')
    return results, vector


def ex_2():
    vector = [[0, 0], [0, 1], [1, 0], [1, 1]]
    w0, w1, w2 = random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)
    calculation_f = lambda x1, x2: calculation(w0, w1, w2, x1, x2)
    results = []
    for list in vector:
        results.append(f(calculation_f, list[0], list[1]))
    print(f'W0:{w0} W1:{w1} W2:{w2}')
    for i in range(len(results)):
        print(f'X1:{vector[i][0]} X2:{vector[i][1]} Result:{results[i]}')
    return results, vector


ex_1()
ex_2()
