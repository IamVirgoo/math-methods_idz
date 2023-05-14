import math
import matplotlib.pyplot as plt


def draw_picture(x_list, y_list, node, name):
    plt.title(f"newton-{name}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x_list, y_list, color="red")
    for i in range(len(x_list)):
        plt.scatter(x_list[i], y_list[i], color="purple", linewidths=2)
    plt.scatter(node[0], node[1], color="blue", linewidth=2)
    plt.show()


def divided_diff(x, y):
    """
    Возвращает список разделенных разностей по узлам x и соответствующим значениям функции y.
    """
    n = len(x)
    table = [[0] * n for i in range(n)]
    for i in range(n):
        table[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])
    return table[0]


def newton_stirling(x, y, z):
    """
    Возвращает приближенное значение функции f(x) для значения аргумента z,
    используя интерполяционную формулу Ньютона-Стирлинга с узлами x и значениями функции y.
    """
    n = len(x)
    coeffs = divided_diff(x, y)
    result = coeffs[n - 1]
    for i in range(n - 2, -1, -1):
        result = result * (z - x[i]) + coeffs[i]
    return result


def newton_bessel_interpolation(x, y, xi):
    """
    Возвращает приближенное значение функции f(x) для значения аргумента z,
    используя интерполяционную формулу Ньютона-Бесселя с узлами x и значениями функции y.
    """
    number = len(x)
    coeffs = divided_diff(x, y)
    result = coeffs[number - 1]
    for i in range(number - 2, -1, -1):
        result = coeffs[i] + (xi - x[i]) * result
    return result


def func(x):
    return math.log(x)


if __name__ == '__main__':
    x = 0.54

    x_1 = [0.4, 0.5, 0.6, 0.7, 0.8]
    y_1 = [func(i) for i in x_1]

    print("Список разделённых значений по узлам: {}".format(divided_diff(x_1, y_1)))
    newton = newton_stirling(x_1, y_1, x)
    bessel = newton_bessel_interpolation(x_1, y_1, x)
    print("Истинное значени для y = log(x): {}".format(func(x)))
    print("Интерполяция Ньютона-Стирлинга: {}".format(newton))
    print("Интерполяция Ньютона-Бесселя: {}".format(bessel))

    draw_picture(x_1, y_1, (x, newton), "stirling")
    draw_picture(x_1, y_1, (x, bessel), "bessel")
