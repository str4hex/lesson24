import os

from flask import Flask, request, abort
from utils import answer

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=["POST"])
def perform_query():
    quest = ['file_name', 'cmd1', 'value1', 'cmd2', 'value2']

    file_dir = os.listdir(DATA_DIR)
    file_name = [request.values.get('file_name')]

    data = filter(lambda x: x is False is abort(400), map(lambda x: x in quest, list(request.values)))
    file_check = filter(lambda x: x is False is abort(400), map(lambda x: x in file_dir, file_name))
    list(data)
    list(file_check)

    file = DATA_DIR + '\\' + request.values.get('file_name')
    cmd1 = request.values.get('cmd1')
    value1 = request.values.get('value1')
    cmd2 = request.values.get('cmd2')
    value2 = request.values.get('value2')

    res = None

    if cmd1 and value1:
        res = answer(cmd1, value1, file)

        if cmd2 and value2:
            file_res = DATA_DIR + '\\' + 'res.txt'
            with open('data/res.txt', 'w', encoding='utf-8') as f:
                f.write(res)
            res = answer(cmd2, value2, file_res)

        return res

    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат

    return app.response_class(res, content_type="text/plain")
