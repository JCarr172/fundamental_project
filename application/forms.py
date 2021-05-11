from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class ArmyForm(FlaskForm):
    name = StringField('Name of army', validators = [DataRequired()])
    faction = StringField("The army's faction", validators = [DataRequired()])
    codex = StringField('Codex edition', validators = [DataRequired()])
    submit = SubmitField('Submit')