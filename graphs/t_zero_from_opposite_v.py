import typing as tp

import matplotlib.pyplot as plt
import numpy as np


def build_t_zero_from_v(
    opposite_V: tp.List[float], t_zero: tp.List[float], A: float, C: float
) -> str:
    fig = plt.figure()
    ax = fig.add_subplot(2, 1, 1)

    # возможные цвета графиков
    colours = ["g", "b", "m", "c", "y"]

    # основные и дополнительные линии в системе координат (помимо Ox и Oy)
    ax.minorticks_on()
    ax.grid(which="major", color="k", linewidth="0.5")
    ax.grid(which="minor", color="k", linewidth="0.1")

    # размеры отображаемой на рисунке системы координат
    fig.set_figheight(10)
    fig.set_figwidth(10)

    # ищем максимальное значение opposite_V, чтобы задать ширину графика больше последнего
    max_width = max(opposite_V) + 0.005

    # то же самое для высоты
    max_height = max(t_zero) + 150
    min_height = min(t_zero) - 20

    # длина графика по осям
    plt.ylim(min_height, max_height)
    plt.xlim(0, max_width)

    plot_fn(ax, colours[1], opposite_V, t_zero)

    x = np.arange(0, max_width + 5, 1)
    y = find_y(x, A, C)
    plt.plot(x, y, colours[0], label="МНК")

    ax.legend()
    ax.set_xlabel("1/Vц, 1/мл")
    ax.set_ylabel("t∗, °С")
    name = "t_zero_from_opposite_V.png"
    plt.savefig(f"graphs/{name}", transparent=True, bbox_inches="tight")

    return name


# построить точки на графике
def plot_fn(ax, color: str, xpoints=None, ypoints=None):
    ax.plot(xpoints, ypoints, color + "o", label=f"Экспериментальные данные")


def find_y(x, A, C):
    return A * x + C
