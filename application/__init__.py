
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import pandas as pd 

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


#create global access to session object 

#create a pedal flask form 

class PedalForm(FlaskForm):
    model = StringField('Model Name', validators=[DataRequired()])
    effect = StringField('Effect Type',validators=[DataRequired()])
    year_intro = StringField('Year Introduced',validators=[DataRequired()])
    series = StringField('Series',validators=[DataRequired()])
    submit = SubmitField('Submit Entry')




#classes 
class Pedal(db.Model):
    __tablename__='pedal'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(300),nullable=False)
    effect = db.Column(db.String(3000), nullable = True)
    year_intro = db.Column(db.String(300), nullable= True)
    series = db.Column(db.String(300), nullable= True)

    def __repr__(self):
        return f"<'{self.model}','{self.effect}','{self.year_intro}','{self.series}'>"


class Bandmember(db.Model):
    __tablename__ ='bandmember'
    id = db.Column(db.Integer, primary_key=True)
    first_name =db.Column(db.String(300),nullable=False)
    second_name = db.Column(db.String(300),nullable=False)
    fav_pedal_id= db.Column(db.Integer,db.ForeignKey('pedal.id'))


#bandmember csv
banddata= pd.read_csv('application/bandmember.csv')
df1 = pd.DataFrame(banddata, columns=['first_name','second_name','fav_pedal_id'])
df1 = df1.fillna('')

#convert csv into transferable form 
data = pd.read_csv('application/database.csv')
df2 = pd.DataFrame(data, columns = ['model','effect','year_intro','series'])
df2 = df2.fillna('')


db.drop_all()
db.create_all()
#add all entries into database 


for _,row in df2.iterrows():
    entry = Pedal(model=row['model'],effect=row['effect'],year_intro=row['year_intro'],series=row['series'])
    
    db.session.add(entry) 
    db.session.commit()

for _,row in df1.iterrows():
    entry = Bandmember(first_name=row['first_name'],second_name=['second_name'],fav_pedal_id=['fav_pedal_id'])
    db.session.add(entry) 
    db.session.commit()
from application import routes
