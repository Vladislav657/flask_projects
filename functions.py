import json


def load_posts(path):
    with open(path, "r", encoding='UTF-8') as data:
        return json.load(data)


def get_posts(posts, sub):
    return [i for i in posts if sub.lower() in i['content'].lower()]


def allowed_file(filename):
    allowed_extensions = ['png', 'jpg', 'jpeg']
    return '.' in filename and filename.rsplit('.', 1)[1] in allowed_extensions


def upload_posts(path, data):
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(data, file, ensure_ascii=False)