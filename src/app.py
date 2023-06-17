from flask import Flask, render_template
from game_of_life import GameOfLife
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(current_dir)
template_folder = os.path.join(parent_dir, 'templates')
static_folder = os.path.join(parent_dir, 'static')

print(template_folder )

# Set the template folder for the Flask application

app = Flask(__name__)

app.template_folder = template_folder
app.static_folder = static_folder


@app.route('/')
def index():
    GameOfLife(25, 25)

    return render_template("index.html")

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