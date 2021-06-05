import typing as tp


def find_mnk_odds(X: tp.List[float], Y: tp.List[float]) -> tp.Tuple[float, float]:
    X_mean = sum(X) / len(X)
    Y_mean = sum(Y) / len(Y)

    numerator = 0.0
    denominator = 0.0
    for counter in range(len(X)):
        numerator += (X[counter] - X_mean) * Y[counter]
        denominator += (X[counter] - X_mean) ** 2

    A = numerator / denominator
    C = Y_mean - A * X_mean

    return A, C
