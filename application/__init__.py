
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import pandas as pd 
from sqlalchemy.orm import relationship

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#create application 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")

app.config["SECRET_KEY"] = getenv("SECRET_KEY")

#set up database 
db = SQLAlchemy(app)
#db.drop_all()
from application.models import Pedal , Bandmember

class BandmemberForm(FlaskForm):
    first_name= StringField('first_name', validators=[DataRequired()])
    second_name= StringField('second_name',validators=[DataRequired()])
    submit = SubmitField('Submit Entry')

#bandmember csv
banddata= pd.read_csv('application/csv_data/bandmember.csv')
df2 = pd.DataFrame(banddata, columns=['first_name','second_name','fav_pedal_id'])
df2 = df2.fillna('')

#convert csv into transferable form 
data = pd.read_csv('application/csv_data/database.csv')
df1 = pd.DataFrame(data, columns = ['model','effect','year_intro','series'])
df1 = df1.fillna('')


db.drop_all()
db.create_all()
#add all entries into database 

def populate_database():
    for _,row in df1.iterrows():
        entry = Pedal(model=row['model'],effect=row['effect'],year_intro=row['year_intro'],series=row['series'])
        db.session.add(entry) 
        db.session.commit()
    for _,row in df2.iterrows():
        entry = Bandmember(first_name=row['first_name'],second_name=row['second_name'],fav_pedal_id=row['fav_pedal_id'])
        db.session.add(entry) 
        db.session.commit()

populate_database()


from application import routes
