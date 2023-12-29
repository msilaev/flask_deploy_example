from . import app
from flask import Flask, render_template, request, url_for
from .game_of_life import GameOfLife
from werkzeug.utils import redirect
from .project.forms import MessageForm

@app.route('/', methods=['GET', 'POST'])
def index():
    height = 5
    width = 5
    form = MessageForm()

    if form.validate_on_submit():

        height = form.height.data
        width = form.width.data
        game = GameOfLife(width, height)
        return redirect(url_for('creation'))

    return render_template("index.html", form=form, width=width, heigth=height)

@app.route('/creation', methods=['GET', 'POST'])
def creation():
    return render_template("creation.html")

@app.route('/live_box')
def live_box():
   game = GameOfLife()
   if game.counter > 0:
        game.form_new_generation_box()
   game.counter = game.counter + 1
   return render_template("live_box.html", game = game)

@app.route('/live_periodic')
def live_periodic():
    game = GameOfLife()
    if game.counter > 0:
        game.form_new_generation_periodic()
    game.counter = game.counter + 1
    return render_template("live_periodic.html", game=game)

@app.route('/start_over_periodic')
def start_over_periodic():
    game = GameOfLife()
    game.world = game.generate_universe()
    game.counter =1
    return render_template("live_periodic.html", game=game)

@app.route('/start_over_box')
def start_over_box():
    game = GameOfLife()
    game.world = game.generate_universe()
    game.counter = 1
    return render_template("live_box.html", game=game)

    #return render_template("start_over.html", game=game)