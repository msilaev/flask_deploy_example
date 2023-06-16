from flask import Flask, render_template
import os
from game_of_life import GameOfLife

app=Flask(__name__)

# Get the current directory (location of app.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)


# Define the relative path to the template folder
template_folder = os.path.join(parent_dir, 'templates')

# Set the template folder for the Flask application
app.template_folder = template_folder
app.static_folder = os.path.join(parent_dir, 'static')


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
    print(app.static_folder)
    app.run(host= "0.0.0.0", port =5000)