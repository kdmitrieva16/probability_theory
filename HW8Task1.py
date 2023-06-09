# Даны значения величины заработной платы заемщиков банка (zp) и значения их
# поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с
# помощью функции cov из numpy
# Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и
# среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# plt.scatter(zp,ks)
# plt.xlabel('Величина заработной платы "ZP"')
# plt.ylabel('Поведенческий кредитный скоринг "KS"', rotation=90)
# plt.show()

# Ковариация с помощью элементарных действий,
cov_zp_ks = np.mean(zp * ks) - np.mean(zp) * np.mean(ks)
print(cov_zp_ks)

# Функция cov из numpy
cov_zp_ks1 = np.cov(zp, ks, ddof=0)[0, 1]
print(cov_zp_ks1)

# коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков:
corr_pirson = cov_zp_ks / (np.std(zp) * np.std(ks))
print(corr_pirson)

corr_pirson1 = cov_zp_ks / (np.std(zp, ddof=0) * np.std(ks, ddof=0))
print(corr_pirson1)

# Numpy
corr_numpy = np.corrcoef(zp, ks)[0][1]
print(corr_numpy)

# Pandas
corr_pandas = pd.Series(zp).corr(pd.Series(ks), method='pearson')
print(corr_pandas)
