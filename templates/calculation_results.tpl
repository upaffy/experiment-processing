<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.12/semantic.min.css"></link>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.12/semantic.min.js"></script>
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

        <title>Physics 2.01</title>
    </head>
    <body>
        <div class="ui text container">
            <h1 class="ui dividing header">Perfect!</h1>

            <p>
                <div class="ignored ui info message">
                    <p>Вы ввели все значения корректно! Если захотите что-то поменять, форму можно подкорректировать и отправить заново.
                    Именно для этого она висит снизу. Если же вас все устраивает, еще чуть ниже можно увидеть результат обработки введенных данных
                    </p>
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
                                <input type="text" name="p0" placeholder="Введите значение давления в лаборатории (p0)", value = {{ data["p0"] }}>
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
                                    <input type="text" name="t{{ table }}" placeholder="Введите значение температуры, для которой берутся измерения" value = {{ data[f"t{table}"] }}>
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
                                        <input name="p1{{ table }}{{ row }}" type="text" value={{ data[f"p1{table}{row}"] }}>
                                      </div>
                                    </div>
                                </td>
                                <td>
                                    <div class="ui form">
                                      <div class="field">
                                        <input name="p2{{ table }}{{ row }}" type="text" value={{ data[f"p2{table}{row}"] }}>
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

        <div class="ui text container">
            <h1 class="ui dividing header">Рассчет результатов косвенных измерений</h1>

            <p>
                Для каждой из таблиц рассчитаем давление газа (p) по формуле:
                $$ {p = p_{0} + \frac{\Delta p_1 + \Delta p_2}{2}} $$
                и обратное давление газа (1/p). Результаты занесем в следующие таблицы:
            </p>
        </div>
        %for table in tables:
            <button class="accordion">Таблица {{ table }}</button>
            <div class="panel">
                <div class="ui container" style="padding-top: 10px;">
                    <table class="ui {{ colours[table] }} celled table">
                        <thead>
                          <tr>
                            <th colspan="6">
                                t = {{ data[f"t{table}"] }}°С
                            </th>
                          </tr>
                        </thead>
                        <thead>
                            <th>№ п.п.</th>
                            <th>Vц, мл</th>
                            <th>Δp1, кПа</th>
                            <th>Δp2, кПа</th>
                            <th>p, кПа</th>
                            <th>1/p, 1/кПа</th>
                        </thead>
                        <tbody>
                            %for row in rows:
                            <tr>
                                <td>{{ row }}</td>
                                <td>{{ row * 10 + 40 }}</td>
                                <td>
                                    {{ data[f"p1{table}{row}"] }}
                                </td>
                                <td>
                                    {{ data[f"p2{table}{row}"] }}
                                </td>
                                <td>
                                    p
                                </td>
                                <td>
                                    1/p
                                </td>
                            </tr>
                            %end
                        </tbody>
                    </table>
                </div>
            </div>
        %end
        <div class="ui text container">
            <p>
                По данным таблиц построим на одной координатной сетке графики зависимости рабочего объема Vц от обратного давления 1/p
            </p>
        </div>


        <div class="ui text container">
            <p>
                Рассчитаем значение углового коэффициента K для каждого из графиков зависимости Vц от 1/p:
                $$ K = A = \frac{\sum_{i=1}^{n}(X_i - \overline{X})Y_i}{\sum_{i=1}^{n}(X_i - \overline{X})^2} $$
                где
                $$ \overline{X} = \frac{1}{N}\sum_{i=1}^{N}X_i $$
                Перенесем значения рабочих температур, а также коэффициент K в следующую таблицу:
            </p>
        </div>


        <div class="ui container" style="padding-top: 10px;">
            <table class="ui grey celled table">
                <thead>
                    <th>№ п.п.</th>
                    <th>t, °С</th>
                    <th>K, Дж</th>
                </thead>
                <tbody>
                    %for table in tables:
                    <tr>
                        <td>{{ tables[table - 1] }}</td>
                        <td>t</td>
                        <td>K</td>
                    </tr>
                    %end
                </tbody>
            </table>
        </div>

        <div class="ui text container">
            <p>
                По данным таблицы построим график зависимости K(t).
                Для начала нанесем на график экспериментальные точки и затем воспользуемся методом наименьших квадратов:
                $$  A = \frac{\sum_{i=1}^{n}(X_i - \overline{X})Y_i}{\sum_{i=1}^{n}(X_i - \overline{X})^2} = $$
                $$ C = \overline{Y} - A\overline{X} = $$
                Теперь рассчитаем тепературу абсолютного нуля:
                $$ t_{*} = -\frac{C}{A} = $$
                По данным первых таблиц заполним следующую таблицу, где для каждого из объемов найдем значение обратного объема 1/Vц и рассчитаем величину t∗ по формуле:
                $$ \widetilde{t_{*}} = -\frac{c}{a} = $$
            </p>
        </div>


        <div class="ui container" style="padding-top: 10px;">
            <table class="ui {{ colours[table] }} celled table">
                <thead>
                  <tr>
                    <th> Vц </th>
                    <th> 50 </th>
                    <th> 60 </th>
                    <th> 70 </th>
                    <th> 80 </th>
                    <th> 90 </th>
                    <th> 100 </th>
                    <th> 110 </th>
                    <th> 120 </th>
                  </tr>
                </thead>
                <thead>
                    <th>t, C</th>
                    <th class="center aligned" colspan="8">
                        p, кПа
                    </th>
                </thead>
                <tbody>
                    %for table in tables:
                        <tr>
                            <td>t</td>
                            <td>p</td>
                            <td>p</td>
                            <td>p</td>
                            <td>p</td>
                            <td>p</td>
                            <td>p</td>
                            <td>p</td>
                            <td>p</td>
                        </tr>
                    %end
                    <tr>
                        <td>1/Vц</td>
                        <td>V</td>
                        <td>V</td>
                        <td>V</td>
                        <td>V</td>
                        <td>V</td>
                        <td>V</td>
                        <td>V</td>
                        <td>V</td>
                    <tr>
                    <tr>
                        <td>t∗, C</td>
                        <td>t</td>
                        <td>t</td>
                        <td>t</td>
                        <td>t</td>
                        <td>t</td>
                        <td>t</td>
                        <td>t</td>
                        <td>t</td>
                    <tr>
                </tbody>
            </table>
        </div>
        <div class="ui text container">
            <p>
                Пользуясь этой таблицей, построим графики p(t) на одной координатной сетке:
            </p>
        </div>


        <div class="ui text container">
            <p>
                Также с помощью этой таблицы, найдем угловой коэффициент A′ и свободное слагаемое C′ для зависимости t∗(1/Vц):
                $$ A' = \frac{1}{D}\sum_{i=1}^N(X_i -\overline{X})Y_i = $$
                Величина C' - фактически есть предел
                $$ \lim\limits_{1/V\to0} \widetilde{t_{*}} $$
                то есть совпадает со значением t∗.
                $$ C' = \overline{Y} - A\overline{X} = = \widetilde{t_{*}} $$
                На координатной сетке t∗ от 1/Vц отметим экспериментальные точки и начертим прямую,
                соответствующую найденным параметрам A' и C'. Продолжим прямую до пересечения с осью ординат
            </p>
        </div>


        <div class="ui text container">
            <h1 class="ui dividing header">Окончательные результаты</h1>
            <p>
                Температура абсолютного нуля, рассчитанная в работе двумя способами:
                <div class="ui bulleted list">
                  <div class="item">раз с погрешностями</div>
                  <div class="item">два с погрешностями</div>
                </div>
            </p>
        </div>


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

            .accordion {
                background-color: #eee;
                color: #444;
                cursor: pointer;
                padding: 18px;
                width: 100%;
                border: none;
                text-align: left;
                outline: none;
                font-size: 15px;
                transition: 0.4s;
            }

            .active, .accordion:hover {
                background-color: #ccc;
            }

            .panel {
                padding: 0 18px;
                background-color: white;
                max-height: 0;
                overflow: hidden;
                transition: max-height 0.2s ease-out;
            }
        </style>

        <script>
            var acc = document.getElementsByClassName("accordion");
            var i;

            for (i = 0; i < acc.length; i++) {
              acc[i].addEventListener("click", function() {
                this.classList.toggle("active");
                var panel = this.nextElementSibling;
                if (panel.style.maxHeight){
                  panel.style.maxHeight = null;
                } else {
                  panel.style.maxHeight = panel.scrollHeight + "px";
                }
              });
            }
        </script>
    </body>
</html>