from bottle import get, post, redirect, request, route, run, template

from handlers import InputError, post_data_handler

# количество строк в таблице измерений
ROWS_NUMBER = 8
# количество таблиц
TABLES_NUMBER = 4

colours = ["red", "orange", "yellow", "olive", "green", "teal"]
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
    return template(
        "templates/calculation_results.tpl", tables=tables, rows=rows, colours=colours, data=data
    )


if __name__ == "__main__":
    run(host="localhost", port=8080)
