import json

def load_data_from_file():
    with open('posts.json', 'r', encoding='utf-8') as file_read:
        return json.load(file_read)

def search_by_word(word):
    result = []
    for post in load_data_from_file():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result