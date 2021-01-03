from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InsertPedalForm(FlaskForm):
    model = StringField('Model Name', validators=[DataRequired()])
    effect = StringField('Effect Type',validators=[DataRequired()])
    year_intro = StringField('Year Introduced',validators=[DataRequired()])
    series = StringField('Series',validators=[DataRequired()])
    submit1 = SubmitField('Submit Entry')

class UpdatePedalForm(FlaskForm):
    modelname = StringField('Entry to Update', validators=[DataRequired()])
    model = StringField('Model Name')
    effect = StringField('Effect Type')
    year_intro = StringField('Year Introduced')
    series = StringField('Series')
    submit2 = SubmitField('Submit Entry')
    
class DeletePedalForm(FlaskForm):
    model = StringField('Model Name', validators=[DataRequired()])
    submit3 = SubmitField('Submit Entry')


class BandmemberForm(FlaskForm):
    first_name= StringField('first_name', validators=[DataRequired()])
    second_name= StringField('second_name',validators=[DataRequired()])
    submit = SubmitField('Submit Entry')
