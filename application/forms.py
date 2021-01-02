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



