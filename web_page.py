from bottle import (get, post, redirect, request, route, run, static_file,
                    template)

from calculations.indirect_measurements import find_gas_pressure
from calculations.mnk import find_mnk_odds
from graphs.K_from_temperature import build_K_from_t
from graphs.pressure_from_temperature import build_p_from_t
from graphs.t_zero_from_opposite_v import build_t_zero_from_v
from graphs.volume_from_pressure import build_vol_from_pres
from handlers import ROWS_NUMBER, TABLES_NUMBER, InputError, post_data_handler

colours = ["orange", "yellow", "olive", "green", "teal", "blue"]
rows = list(range(1, ROWS_NUMBER + 1))
tables = list(range(1, TABLES_NUMBER + 1))


@get("/")
def main_page() -> str:
    return template("templates/index_page.tpl", rows=rows, tables=tables, colours=colours)


@post("/")
def send_form() -> str:
    data = dict(request.forms.allitems())
    # заменить в дробных числах запятую на точку, чтобы это не влияло на работоспособность программмы
    for key, value in data.items():
        data[key] = value.replace(",", ".")

    response = post_data_handler(data)
    if isinstance(response, InputError):
        if response.temperature_error:
            return template(
                "templates/temperature_error_page.tpl",
                tables=tables,
                rows=rows,
                colours=colours,
                type=response.type,
                inc_table=response.table,
                data=response.data,
            )
        elif response.p0_error:
            return template(
                "templates/p0_error_page",
                tables=tables,
                rows=rows,
                colours=colours,
                type=response.type,
                data=response.data,
            )
        else:
            return template(
                "templates/p_error_page.tpl",
                tables=tables,
                rows=rows,
                colours=colours,
                inc_table=response.table,
                inc_column=response.column,
                inc_row=response.row,
                type=response.type,
                data=response.data,
            )

    t, p1, p2, p0 = response

    p = find_gas_pressure(p0, p1, p2)
    V = [50, 60, 70, 80, 90, 100, 110, 120]

    graph_1, graph_1_A = build_vol_from_pres(p, V)
    K = graph_1_A

    graph_2_A, graph_2_C = find_mnk_odds(t, K)
    graph_2_A = round(graph_2_A, 2)
    graph_2_C = round(graph_2_C, 2)
    abs_zero_1 = round(-graph_2_C / graph_2_A, 3)

    graph_2 = build_K_from_t(K, t, graph_2_A, graph_2_C)

    opposite_V = [round(1 / value, 3) for value in V]
    p_list = [[element[0] for element in table] for table in p]
    p_trans_list = list(map(list, zip(*p_list)))

    t_zero_list = []
    for row in range(ROWS_NUMBER):
        a, c = find_mnk_odds(t, p_trans_list[row])
        t_zero_list.append(round(-c / a, 3))

    graph_3 = build_p_from_t(t, p_trans_list)

    graph_4_A, graph_4_C = find_mnk_odds(opposite_V, t_zero_list)
    graph_4_A = round(graph_4_A, 2)
    graph_4_C = round(graph_4_C, 2)

    graph_4 = build_t_zero_from_v(opposite_V, t_zero_list, graph_4_A, graph_4_C)

    return template(
        "templates/calculation_results.tpl",
        tables=tables,
        rows=rows,
        colours=colours,
        data=data,
        p=p,
        graph_1=graph_1,
        t=t,
        K=K,
        graph_2_A=graph_2_A,
        graph_2_C=graph_2_C,
        graph_2=graph_2,
        abs_zero_1=abs_zero_1,
        opposite_V=opposite_V,
        t_zero_list=t_zero_list,
        graph_3=graph_3,
        graph_4_A=graph_4_A,
        graph_4_C=graph_4_C,
        graph_4=graph_4,
    )


@route("/static/<filename>")
def serve_pictures(filename):
    return static_file(filename, root="./graphs")


if __name__ == "__main__":
    run(host="localhost", port=8080)
