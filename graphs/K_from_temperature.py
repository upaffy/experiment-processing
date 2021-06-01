import typing as tp

import matplotlib.pyplot as plt
import numpy as np


def build_K_from_t(K: tp.List[float], t: tp.List[float], A: float, C: float) -> str:
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

    # ищем максимальное значение t, чтобы задать ширину графика больше последнего
    max_width = max(t) + 5

    # то же самое для высоты
    max_height = max(K) + 200
    min_height = min(K) - 200

    # длина графика по осям
    plt.ylim(min_height, max_height)
    plt.xlim(0, max_width)

    plot_fn(ax, colours[1], t, K)

    x = np.arange(0, max_width + 5, 1)
    y = find_y(x, A, C)
    plt.plot(x, y, colours[0], label="МНК")

    ax.legend()
    ax.set_xlabel("t, °С")
    ax.set_ylabel("K, Дж")
    name = "k_from_t.png"
    plt.savefig(f"graphs/{name}", transparent=True, bbox_inches="tight")

    return name


# построить точки на графике
def plot_fn(ax, color: str, xpoints=None, ypoints=None):
    ax.plot(xpoints, ypoints, color + "o", label=f"Экспериментальные данные")


def find_y(x, A, C):
    return A * x + C
