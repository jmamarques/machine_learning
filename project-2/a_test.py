
import algorithm as alg
import random
import master_mind as mm
import statistics_base as base_s
import const

# guardar todos os padrões para estudar/analisar futuramente
goals = []
for case in const.CASES_2:
    random.seed(1000)
    goals.append(alg.RandomAlgorithm.random_bit_pattern(case))

reports = []
for goal in goals:
    mm_play = lambda: mm.MasterMind().play_genetic_algorithm_crossover(goal)
    statistics_play = base_s.BaseStatistics(False)
    statistics_play.base_statistics(mm_play, 30)
    reports.append(statistics_play)

attempts = []
times = []
for i in range(len(reports)):
    print(f"Number of bits in pattern: {const.CASES_2[i]}")
    print(reports[i])
    attempts.append(reports[i].attempts_average)
    times.append(reports[i].time_average)
base_s.BaseStatistics.linear_plot_dev(const.CASES_2, attempts, 'the number of bits in the pattern ',
                                      'the evolution of attempts',
                                      'the evolution of attempts vs the number of bits in the pattern')
base_s.BaseStatistics.linear_plot_dev(const.CASES_2, times, 'the number of bits in the pattern ', 'the evolution of time',
                                      'the evolution of time vs the number of bits in the pattern')