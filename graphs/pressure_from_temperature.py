import typing as tp

import matplotlib.pyplot as plt
import numpy as np
from calculations.mnk import find_mnk_odds


def build_p_from_t(t: tp.List[float], p: tp.List[tp.List[float]]) -> str:

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

    # ищем максимальное значение p, чтобы задать высоту графика больше последнего и меньше первого
    max_height = -1.0
    min_height = 1000.0
    for table in p:
        for element in table:
            if element > max_height:
                max_height = element
            if element < min_height:
                min_height = element
    max_height += 20
    min_height -= 150

    # то же самое для ширины
    max_width = max(t) + 5

    # длина графика по осям
    plt.ylim(min_height, max_height)
    plt.xlim(0, max_width)

    for counter in range(len(p)):
        plot_fn(ax, colours[counter % len(colours)], t, p[counter], counter)
        A, C = find_mnk_odds(t, p[counter])

        x = np.arange(0, max_width + 10, 1)
        y = find_y(x, A, C)
        plt.plot(x, y, colours[counter % len(colours)])

    ax.legend()
    ax.set_xlabel("t, °С")
    ax.set_ylabel("p, кПа")
    name = "pressure_from_temperature.png"
    plt.savefig(f"graphs/{name}", transparent=True, bbox_inches="tight")

    return name


# построить точки на графике
def plot_fn(ax, color: str, xpoints=None, ypoints=None, number=0):
    ax.plot(
        xpoints, ypoints, color + "o", label=f"Экспериментальные данные для V = {50 + number*10}"
    )


def find_y(x, A, C):
    return A * x + C
