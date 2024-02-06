from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class Tweet(FlaskForm):
    author = StringField("Author")
    tweet = StringField("Tweet")
    submitButton = SubmitField("Create Tweet")