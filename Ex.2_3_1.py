import numpy as np


def polar_to_decart(r, alpha):
    x = r * np.cos(np.radians(alpha))
    y = r * np.sin(np.radians(alpha))
    return(x, y)


r = float(input("Введите значение радиальной координаты: "))
alpha = float(input("Введите значение угловой координаты в градусах: "))
print(f"Радиальной координате {r} и угловой координате {alpha} градусов соответствуют декартовы координаты {polar_to_decart(r, alpha)}")
