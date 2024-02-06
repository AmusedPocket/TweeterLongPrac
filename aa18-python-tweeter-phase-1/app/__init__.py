# !!START
from flask import Flask, render_template, redirect
from .config import Config
from .tweets import tweets
from random import choice, randint
from .form.form import Tweet
from datetime import datetime, timedelta



app = Flask(__name__)

app.config.from_object(Config)
# !!END

@app.route("/")
def index():
    tweet = choice(tweets)
    return render_template("index.html", tweet=tweet)

@app.route("/feed")
def feed():
    tweets_sorted = sorted(tweets, key=lambda i: datetime.strptime(i['date'], '%m/%d/%y'), reverse=True)
    # print(tweets_sorted)
    return render_template("feed.html", tweets=tweets_sorted)

@app.route('/new', methods=['GET', 'POST'])
def form():
    form = Tweet()
    if form.validate_on_submit():
        params = {
            "id": len(tweets) + 1,
            "author": form.data["author"],
            "date": datetime.now().strftime("%m/%d/%y"),
            "tweet" : form.data["tweet"],
            "likes" : randint(10, 100000)
        }
        tweets.append(params)
        print(tweets)
        return redirect('/feed')

    if form.errors:
        return redirect('/')

    return render_template("new_tweet.html", form=form)
