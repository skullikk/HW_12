from flask import Blueprint, render_template, request

from main.utils import search_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='template')

@main_blueprint.route('/')
def main_page():
    return render_template('index.html')

@main_blueprint.route('/search')
def search_page():
    s = request.args.get('s')
    list_posts = search_by_word(s)
    return render_template('post_list.html', list_posts = list_posts, s = s)

