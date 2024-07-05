import numpy as np
import matplotlib.pyplot as pl

# Параметры нормального распределения
mean = 0 # Среднее значение
std_dev = 1 # Стандартное отклонение
num_samples = 1000 # Количество образцов

data = np.random.normal(mean, std_dev, num_samples)


pl.hist(data, bins=4)

pl.xlabel("x ось")
pl.ylabel("y ось")
pl.title("Тестовая гистограмма")

pl.show()

random_array1 = np.random.rand(5)
print(random_array1)
random_array2 = np.random.rand(5)
print(random_array2)

pl.scatter(random_array1, random_array2)
pl.xlabel("x ось")
pl.ylabel("y ось")
pl.title("Тестовая диаграмма рассеяния")

pl.show()
