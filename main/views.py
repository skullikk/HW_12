import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request
from functions import search_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='template')


# Маршрутизация на главную страницу
@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


# Mаршрутизация на результаты поиска по вхождению подстроки s
@main_blueprint.route('/search')
def search_page():
    s = request.args.get('s')
    logging.info('Выполняю поиск')
    try:
        list_posts = search_by_word(s)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл json не найден'
    except JSONDecodeError:
        return 'Файл json поврежден'
    return render_template('post_list.html', list_posts=list_posts, s=s)
