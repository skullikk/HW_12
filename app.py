import logging
from flask import Flask, request, render_template, send_from_directory
from loader.views import loader_blueprint
from main.views import main_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# Регистрируем blueprint's
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

# Устанавливаем логирование и уровень
logging.basicConfig(filename='log.log', level=logging.INFO)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

if __name__ == "__main__":
    app.run()

