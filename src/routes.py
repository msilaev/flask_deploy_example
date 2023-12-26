from . import app
from flask import Flask, render_template, request, url_for
from .game_of_life import GameOfLife
from werkzeug.utils import redirect

from .project.forms import MessageForm

#from flask import session

from flask import g

@app.before_request
def before_request():
    if not hasattr(g, 'game'):
        g.game = GameOfLife()  # Initialize the instance if not present in 'g'


@app.route('/', methods=['GET', 'POST'])
def index():
    height = 25
    width = 25

    form = MessageForm()
    #print(form.validate_on_submit())
    if form.validate_on_submit():
        g.game.counter =0

        height = form.height.data
        width = form.width.data
        #print('\n Data received. Redirection ..')

        g.game.height = height
        g.game.width =  width
        #GameOfLife(height, width)
        #print(f"param {height}, {width}")

        g.game.world = g.game.generate_universe()

        return redirect(url_for('creation'))

    g.game.world = g.game.generate_universe()
    return render_template("index.html", form=form, width=width, heigth=height)

@app.route('/creation', methods=['GET', 'POST'])
def creation():
    #print("creation")

    return render_template("creation.html")

@app.route('/live_box')
def live_box():
   #game = GameOfLife()
   game = g.game
   if game.counter > 0:
      game.form_new_generation_box()
   game.counter = game.counter + 1
   return render_template("live_box.html", game=game)

@app.route('/live_periodic')
def live_periodic():
    game = g.game
    if game.counter > 0:
        game.form_new_generation_box()
    game.counter = game.counter + 1
    return render_template("live_periodic.html", game=game)

