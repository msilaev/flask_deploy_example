from flask import Flask, render_template
from game_of_life import GameOfLife

app=Flask(__name__)

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