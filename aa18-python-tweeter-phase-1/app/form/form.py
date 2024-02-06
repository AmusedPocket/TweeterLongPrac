from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class Tweet(FlaskForm):
    author = StringField("Author", validators=[InputRequired()])
    tweet = StringField("Tweet", validators=[InputRequired()])
    submitButton = SubmitField("Create Tweet")
