import logging

from flask import Blueprint, render_template, request
from functions import save_data_to_file
from loader.utils import add_picture_to_post

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='template')


# Маршрутизация на страницу добавления поста
@loader_blueprint.route('/post')
def loader_page():
    return render_template('post_form.html')


# Маршрутизация на страницу результата добавления поста
@loader_blueprint.route('/post', methods=['POST'])
def add_page():
    picture = request.files.get('picture')
    if picture.filename.split('.')[-1] not in ['jpeg', 'png']:
        logging.info('Файл не картинка')
        return 'Неверное расширение файла'
    content = request.form.get('content')
    if not picture or not content:
        return f'Ошибка загрузки. Ничего нет. Проверяйте файл или коммент'
    path_picture = add_picture_to_post(picture)
    post = {'pic': path_picture, 'content': content}
    save_data_to_file(post)
    return render_template('post_uploaded.html', post=post)
