import typing as tp


def find_mnk_odds(X: tp.List[float], Y: tp.List[float]) -> tp.Tuple[float, float]:
    x_sum = 0.0
    y_sum = 0.0

    for x in X:
        x_sum += x
    for y in Y:
        y_sum += y

    X_mean = x_sum / len(X)
    Y_mean = y_sum / len(Y)

    numerator = 0.0
    denominator = 0.0
    for counter in range(len(X)):
        numerator += (X[counter] - X_mean) * Y[counter]
        denominator += (X[counter] - X_mean) ** 2

    A = numerator / denominator
    C = Y_mean - A * X_mean

    return A, C
