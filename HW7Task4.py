#  Даны 3 группы учеников плавания. Не соблюдается условие нормальности.
# В 1 группе время на дистанцию 50 м составляют:
# 56, 60, 62, 55, 71, 67, 59, 58, 64, 67
# Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
# Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54
# Есть
# ли статистически значимые различия между группами?


# 3  независимые выборки - Критерий Крускала-Уоллиса

import numpy as np
from scipy import stats

alpha = 0.05
a = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
b = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
c = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

d = stats.kruskal(a, b, c)
print(d)
s, p = stats.kruskal(a, b, c)
if p > alpha:
    print(
        'Статистически значимых различий нет, нулевая гипотеза не отвергается,'
        'время на дистанцию одинаковое.')
else:
    print(
        'Статистически значимые различия присутствуют, нулевую гипотезу '
        'отвергаем, время на дистанцию не одинаковое.')


# KruskalResult(statistic=5.465564058257224, pvalue=0.06503809985904942)
# Cтатистически значимых различий нет, нулевая гипотеза не отвергается,
# время на дистанцию одинаковое.