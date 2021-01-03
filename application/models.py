from application import app, db
from datetime import datetime

  
#classes 
class Pedal(db.Model):
    __tablename__='pedal'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(300),nullable=False)
    effect = db.Column(db.String(3000), nullable = True)
    year_intro = db.Column(db.String(300), nullable= True)
    series = db.Column(db.String(300), nullable= True)
    bandmember_id =db.Column(db.Integer,db.ForeignKey('bandmember.id'))
    def __repr__(self):
        return f"<'{self.model}','{self.effect}','{self.year_intro}','{self.series}'>"

class Bandmember(db.Model):
    __tablename__ ='bandmember'
    id = db.Column(db.Integer, primary_key=True)
    first_name =db.Column(db.String(300),nullable=False)
    second_name = db.Column(db.String(300),nullable=False)
    pedal_model= db.relationship('Pedal',backref='bandmember')
    def __repr__(self):
        return f"<'{self.first_name}','{self.second_name}'>"