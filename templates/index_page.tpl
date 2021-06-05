<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.12/semantic.min.css"></link>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.12/semantic.min.js"></script>

        <title>Physics 2.01</title>
    </head>
    <body>
        <div class="ui text container">
            <h1 class="ui dividing header">Usage</h1>

            <h3 class="first">Для чего?</h3>
            <p>
                <div class="ui list">
                    <div class="item">Для обработки экспериментальных данных к лабораторной работе №2.01!</div>
                    <div class="item">Введите данные в соответсвующие поля, нажмите кнопку <b>Submit</b> и наслаждайтесь!</div>
                </div>
            </p>

            <h3 class="first">Как вводить?</h3>
            <p>
                <div class="ui bulleted list">
                    <div class="item">Внутри поля для ввода необходимо указывать численные значения (без букв и специальных символов);</div>
                    <div class="item">При вводе дробных значений можно использовать как точку, так и запятую;</div>
                    <div class="item">Для корректной работы алгоритма также необходимо заполнить все поля.</div>
                </div>
            </p>
        </div>
        <form action="/" method="post">
            <div class="ui segment">
              <h3 class="ui center aligned header">
                Таблица 0
              </h3>
            </div>
            <div class="ui container" style="padding-top: 10px;">
                <table class="ui {{ colours[0] }} celled table">
                    <thead>
                      <tr>
                        <th>
                            <div class="ui form">
                              <div class="ui fluid labeled input">
                                <div class="ui label">
                                    кПа
                                </div>
                                <input type="text" name="p0" placeholder="Введите значение давления в лаборатории (p0)">
                              </div>
                            </div>
                        </th>
                      </tr>
                    </thead>
                </table>
            </div>

            %for table in tables:
                <div class="ui segment">
                  <h3 class="ui center aligned header">
                    Таблица {{ table }}
                  </h3>
                </div>
                <div class="ui container" style="padding-top: 10px;">
                    <table class="ui {{ colours[table] }} celled table">
                        <thead>
                          <tr>
                            <th colspan="4">
                                <div class="ui form">
                                  <div class="ui fluid labeled input">
                                    <div class="ui label">
                                        °С
                                    </div>
                                    <input type="text" name="t{{ table }}" placeholder="Введите значение температуры, для которой берутся измерения">
                                  </div>
                                </div>
                            </th>
                          </tr>
                        </thead>
                        <thead>
                            <th>№ п.п.</th>
                            <th>Vц, мл</th>
                            <th>Δp1, кПа</th>
                            <th>Δp2, кПа</th>
                        </thead>
                        <tbody>
                            %for row in rows:
                            <tr>
                                <td>{{ row }}</a></td>
                                <td>{{ row * 10 + 40 }}</td>
                                <td>
                                    <div class="ui form">
                                      <div class="field">
                                        <input name="p1{{ table }}{{ row }}" type="text">
                                      </div>
                                    </div>
                                </td>
                                <td>
                                    <div class="ui form">
                                      <div class="field">
                                        <input name="p2{{ table }}{{ row }}" type="text">
                                      </div>
                                    </div>
                                </td>
                            </tr>
                            %end
                        </tbody>
                    </table>
                </div>
            %end
            <button class="massive fluid green ui button" type="submit">
                Submit
            </button>
        </form>
        <style type="text/css">
            code {
              background-color: #E0E0E0;
              padding: 0.25em 0.3em;
              font-family: 'Lato';
              font-weight: bold;
            }
            .container {
              padding: 5em 0em;
            }
            .ui.dividing.header,
            .first {
              margin-top: 5em;
            }

            .ui.dividing.header:first-child {
              margin-top: 0em;
            }

            h1,
            h3 {
              margin-top: 10em;
            }
        </style>
    </body>
</html>