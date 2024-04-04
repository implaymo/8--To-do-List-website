from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class ToDoForm(FlaskForm):
    checkmark = BooleanField()
    input = StringField('', validators=[DataRequired()])