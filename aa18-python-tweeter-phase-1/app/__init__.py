# !!START
from flask import Flask, render_template
from .config import Config
from .tweets import tweets
from random import choice
from .form.form import Tweet

app = Flask(__name__)

app.config.from_object(Config)
# !!END

@app.route("/")
def index():
    tweet = choice(tweets)
    return render_template("index.html", tweet=tweet)

@app.route("/feed")
def feed():
    return render_template("feed.html", tweets=tweets)

@app.route('/new')
def form():
    form = Tweet()
    return render_template("new_tweet.html", form=form)

