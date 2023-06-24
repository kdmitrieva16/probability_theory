# Задача 1 Даны значения величины заработной платы заемщиков банка (zp) и значения их
# поведенческого кредитного скоринга (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. Используя математические
# операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату
# (то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая
# переменная). Произвести расчет как с использованием intercept, так и без.


import numpy as np
import matplotlib.pyplot as plt

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
cor = np.corrcoef(zp, ks)[0][1]
print(cor ** 2)
plt.scatter(zp, ks)
plt.xlabel('Заработая плата заемщиков')
plt.ylabel('Поведенческий кредитный скоринг', rotation=90)
plt.show()

b1 = (np.mean(zp * ks) - np.mean(zp) * np.mean(ks)) / (
        np.mean(zp ** 2) - np.mean(zp) ** 2)
b0 = np.mean(ks) - b1 * np.mean(zp)
print(b0, b1) # 444.1773573243596 2.620538882402765
ks_pred = b0 + b1 * zp
print(ks_pred)
mse = ((ks - ks_pred) ** 2).sum() / 10
print(mse) #6470.414201176658
plt.scatter(zp, ks)
plt.plot(zp, b0 + b1 * zp, c='r')
plt.xlabel('Заработая плата заемщиков')
plt.ylabel('Поведенческий кредитный скоринг', rotation=90)
plt.show()