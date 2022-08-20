import json

def load_data_from_file():
    """Функция загрузки данных из json файла"""
    with open('posts.json', 'r', encoding='utf-8') as file_read:
        return json.load(file_read)

def search_by_word(word):
    """Функция поиска строки в постах"""
    result = []
    for post in load_data_from_file():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result

def save_data_to_file(post):
    """Функция записи данных по постав в json файл"""
    list_posts = load_data_from_file()
    list_posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file_write:
        json.dump(list_posts, file_write, ensure_ascii=False, indent=4)