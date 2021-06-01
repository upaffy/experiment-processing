import typing as tp

from handlers import ROWS_NUMBER, TABLES_NUMBER


def find_gas_pressure(
    p0: float, p1: tp.List[tp.List[float]], p2: tp.List[tp.List[float]]
) -> tp.List[tp.List[tp.Tuple[float, float]]]:
    p: tp.List[tp.List[tp.Tuple[float, float]]] = [[] * i for i in range(TABLES_NUMBER)]

    for table in range(TABLES_NUMBER):
        for row in range(ROWS_NUMBER):
            p_value = p0 + (p1[table][row] + p2[table][row]) / 2
            p[table].append((p_value, round(1 / p_value, 4)))

    return p
