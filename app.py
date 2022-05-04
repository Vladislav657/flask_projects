import os
import logging
from flask import Flask, request, render_template, send_from_directory
from functions import load_posts, get_posts, allowed_file, upload_posts


POST_PATH = "posts.json"
UPLOAD_FOLDER = "static/uploads/images/"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
logging.basicConfig(filename="info.log", level=logging.INFO)
logging.info("Запуск приложения")


@app.route("/")
def page_index():
    return render_template('index.html')


@app.route('/search', methods=["GET", "POST"])
def page_search():
    if request.method == 'POST':
        req = request.form['search']
        try:
            posts = get_posts(load_posts('posts.json'), req)
            logging.info(f'Поиск постов по запросу "{req}"')
            return render_template('post_list.html', posts=posts, key=req)
        except:
            logging.error('Ошибка при загрузке файла')
            return 'ошибка загрузки'


@app.route("/post")
def page_post_form():
    return render_template('post_form.html')


@app.route("/post_upload", methods=["GET", "POST"])
def page_post_upload():
    if request.method == 'POST':
        pic = request.files['picture']
        text = request.form['content']
        if pic and allowed_file(pic.filename):
            filename = pic.filename
            try:
                posts = load_posts('posts.json')
                posts.append({'pic': UPLOAD_FOLDER + filename, 'content': text})
                upload_posts('posts.json', posts)
            except:
                logging.error('Ошибка при загрузке файла')
                return 'ошибка загрузки'
            try:
                pic.save(os.path.join('static/uploads', 'images', filename))
                logging.info('Пост загружен')
                return render_template('post_uploaded.html', path=UPLOAD_FOLDER + filename, text=text)
            except:
                logging.error('Ошибка при загрузке файла')
                return 'ошибка загрузки'
        else:
            logging.info('Загруженный файл - не картинка (расширение не jpeg и не png)')
            return 'ошибка загрузки'


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory(app.config['UPLOAD_FOLDER'], path)


if __name__ == '__main__':
    app.run()
