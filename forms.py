from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class ToDoForm(FlaskForm):
    input = StringField('', validators=[DataRequired()], render_kw={'autofocus': True})

