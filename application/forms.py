from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class IntegerValidator:
     def __init__(self, message=None):
         self.message = message
    
     def __call__(self, form, field):
         if field.data.isnumeric() == False:
             raise ValidationError(self.message)

class ArmyForm(FlaskForm):
    name = StringField(
        'Name of army', 
        validators = [DataRequired(message='Field requried'), 
        Length(min=1,max=30,message='Input was too long')])
    faction = StringField(
        "The army's faction", 
        validators = [DataRequired(message='Field requried'), 
        Length(min=1,max=30,message='Input was too long')])
    codex = StringField(
        'Codex edition', 
        validators = [DataRequired(message='Field requried'),
        IntegerValidator(message='Please enter a number')])
    submit = SubmitField('Submit')

class UnitForm(FlaskForm):
    name = StringField(
        'Name of unit', 
        validators = [DataRequired(message='Field requried'), 
        Length(min=1,max=30,message='Input was too long')])
    category = SelectField(
        'Category of unit',
        choices=['HQ','Elites','Troops','Heavy Support','Fast Attack'],
        validators = [DataRequired(message='Field requried')])
    army = SelectField(
        "The army's faction",
        choices=[], 
        validators = [DataRequired(message='Field requried')])
    price = StringField(
        'Points per model', 
        validators = [DataRequired(message='Field requried'),
        IntegerValidator(message='Please enter a number')])
    quantity = StringField(
        'Quantity owned', 
        validators = [DataRequired(message='Field requried'),
        IntegerValidator(message='Please enter a number')])
    submit = SubmitField('Submit')

