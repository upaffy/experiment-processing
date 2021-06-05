import typing as tp

import matplotlib.pyplot as plt
import numpy as np
from calculations.mnk import find_mnk_odds


def build_vol_from_pres(
    p: tp.List[tp.List[tp.Tuple[float, float]]], V: tp.List[float]
) -> tp.Tuple[str, tp.List[float]]:
    opposite_p = [[element[1] for element in table] for table in p]

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

    # ищем максимальное значение 1/p, чтобы задать ширину графика больше последнего
    max_width = -1.0
    for table in opposite_p:
        for element in table:
            if element > max_width:
                max_width = element
    max_width += 0.001

    # то же самое для высоты
    max_height = max(V)

    # длина графика по осям
    plt.ylim(0, max_height)
    plt.xlim(0, max_width)

    list_A = []

    for counter in range(len(opposite_p)):
        plot_fn(ax, colours[counter % len(colours)], opposite_p[counter], V, counter)
        A, C = find_mnk_odds(opposite_p[counter], V)

        list_A.append(round(A, 2))

        x = np.arange(0, 10, 1)
        y = find_y(x, A, C)
        plt.plot(x, y, colours[counter % len(colours)])

    ax.legend()
    ax.set_xlabel("1/p, 1/кПа")
    ax.set_ylabel("Vц, л")
    name = "volume_from_pressure.png"
    plt.savefig(f"graphs/{name}", transparent=True, bbox_inches="tight")

    return name, list_A


# построить точки на графике
def plot_fn(ax, color: str, xpoints=None, ypoints=None, number=0):
    ax.plot(xpoints, ypoints, color + "o", label=f"Экспериментальные данные для t{number+1}")


def find_y(x, A, C):
    return A * x + C
