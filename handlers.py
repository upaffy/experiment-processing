import typing as tp
from dataclasses import dataclass, field

TABLES_NUMBER = 4


@dataclass
class InputError:
    p0_error: bool = False
    temperature_error: bool = False
    table: int = 0
    column: int = 0
    row: int = 0
    type: str = ""
    data: tp.Dict[str, str] = field(default_factory=dict)


response = tp.Tuple[tp.List[float], tp.List[tp.List[float]], tp.List[tp.List[float]], float]


def post_data_handler(data: tp.Dict[str, str]) -> tp.Union[response, InputError]:
    t = []
    p0 = 0.0
    p1: tp.List[tp.List[float]] = [[] * i for i in range(TABLES_NUMBER)]
    p2: tp.List[tp.List[float]] = [[] * i for i in range(TABLES_NUMBER)]

    for key, value in data.items():
        # если значение поля заполнено, то продолжить, иначе InputError
        if value:
            # разделение на значения, которые показывают температуру
            if key[0] == "t":
                # значение ключа имеет вид: t<номер таблицы>
                table = int(key[1])
                # если нельзя привести значение к типу float, вернуть InputError
                try:
                    temp = float(value)
                    t.append(temp)
                except ValueError:
                    return InputError(
                        temperature_error=True, table=table, type="incorrect type", data=data
                    )

            # разделение на значения, которые показывают давление
            elif key[0] == "p" and len(key) > 2:
                # значение ключа имеет вид: p<номер колонки - 2><номер таблицы><номер строки>
                table = int(key[2])
                column = int(key[1]) + 2
                row = int(key[3])

                try:
                    p = float(value)
                    if key[:2] == "p1":
                        p1[table - 1].append(p)
                    elif key[:2] == "p2":
                        p2[table - 1].append(p)
                except ValueError:
                    return InputError(
                        table=table, column=column, row=row, type="incorrect type", data=data
                    )

            # находит значение, которое показывает давление в лаборатории p0
            elif key[:2] == "p0":
                try:
                    p0 = float(value)
                except ValueError:
                    return InputError(p0_error=True, type="incorrect type", data=data)
        else:
            if key[0] == "t":
                table = int(key[1])
                return InputError(
                    temperature_error=True, table=table, type="empty value", data=data
                )
            elif key[0] == "p" and len(key) > 2:
                table = int(key[2])
                column = int(key[1]) + 2
                row = int(key[3])
                return InputError(
                    table=table, column=column, row=row, type="empty value", data=data
                )
            elif key[:2] == "p0":
                return InputError(p0_error=True, type="empty value", data=data)

    return t, p1, p2, p0
