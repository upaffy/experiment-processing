import typing as tp

from bottle import redirect, request, route, run, template, post, get

# количество строк в таблице измерений
row_numbers = 8
# количество таблиц
table_numbers = 5

@get('/')
def main_page():
    colours = ["red", "orange", "yellow", "olive", "green", "teal"]
    rows = list(range(1, row_numbers+1))
    tables = list(range(1, table_numbers+1))
    return template("index_page.tpl", rows=rows, tables=tables, colours=colours)


@post('/')
def send_form():
    username = request.forms.get('username')
    password = request.forms.get('password')
    print(username, password)
    return "<p>Your login information was correct.</p>"


if __name__ == "__main__":
    run(host="localhost", port=8080)
