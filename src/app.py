from flask import Flask, render_template, request, url_for
from game_of_life import GameOfLife
from config import Config
from werkzeug.utils import redirect

from project.forms import MessageForm

import os

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(current_dir)
template_folder = os.path.join(parent_dir, 'templates')
static_folder = os.path.join(parent_dir, 'static')

# Set the template folder for the Flask application

app = Flask(__name__)
app.config.from_object(Config)

app.template_folder = template_folder
app.static_folder = static_folder

@app.route('/', methods=['GET', 'POST'])
def index():
    height = 25
    width = 25

    form = MessageForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        height = form.height.data
        width = form.width.data
        print('\n Data received. Redirection ..')

        GameOfLife(height, width)
        print(f"param {height}, {width}")

        return redirect(url_for('creation'))

    return render_template("index.html", form=form, width=width, heigth=height)

@app.route('/creation', methods=['GET', 'POST'])
def creation():
    print("creation")

    return render_template("creation.html")

@app.route('/live_box')
def live_box():
    game = GameOfLife()
    if game.counter > 0:
        game.form_new_generation_box()
    game.counter = game.counter + 1
    return render_template("live_box.html", game=game)

@app.route('/live_periodic')
def live_periodic():
    game = GameOfLife()
    if game.counter > 0:
        game.form_new_generation_periodic()
    game.counter = game.counter + 1
    return render_template("live_periodic.html", game=game)

if __name__=="__main__":
    app.run(host= "0.0.0.0", port =5000)