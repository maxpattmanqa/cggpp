from application import app, db
from application import Pedal,Bandmember
from application.forms import InsertPedalForm , DeletePedalForm, UpdatePedalForm ,BandmemberForm

from flask import render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
Session.configure(bind=db)

session = Session()

@app.route("/")
@app.route("/home")
def view_home():  return render_template('home.html')

@app.route("/kytopia")
def view_kytopia():

    bandmembers = get_all_bandmembers()


    return render_template('kytopia.html',bandmembers=bandmembers)

@app.route("/pedalgallery")
def view_pedalgallery():
    pedals = get_pedals_table()
    return render_template('pedalgallery.html',pedals=pedals)

@app.route("/pedalgalleryeditor",methods=['GET','POST'])
def view_pedalgalleryeditor(): 
    error = ""
    insert_form  = InsertPedalForm()
    update_form = UpdatePedalForm()
    delete_form = DeletePedalForm()
    
    if (request.method =='POST')and(insert_form.validate_on_submit()):
        model = insert_form.model.data
        effect = insert_form.effect.data
        year_intro = insert_form.year_intro.data
        series = insert_form.series.data
        insert_pedal_entry(model=model,effect=effect,year_intro=year_intro,series=series)
       # return render_template('pedalgalleryeditor.html',insert_form=insert_form)

    if (request.method == 'Post') and (update_form.validate_on_submit()):
        modelname = update_form.modelname.data
        model = update_form.model.data
        effect = update_form.effect.data
        year_intro = update_form.year_intro.data
        series = update_form.series.data
        #this is clunky 
        if(model != ''):
            update_pedal_entry_model(str(modelname,model))
        if(effect != ''):
            update_pedal_entry_effect(str(modelname,effect))
        if(year_intro != ''):
            update_pedal_entry_year_intro(str(modelname,year_intro))
        if(series != ''):
            update_pedal_entry_series(str(modelname,series))
        
        #return render_template('pedalgalleryeditor.html',update_form=update_form)
    
    if (request.method == 'Post') and (delete_form.validate_on_submit()):
        delete_pedal_entry(str(delete_form.model.data))
       # return render_template('pedalgalleryeditor.html', delete_form=delete_form)


    return render_template('pedalgalleryeditor.html',insert_form=insert_form,update_form=update_form,delete_form=delete_form,message=error)


#--------------------------------------------------------------------------------#
#                 ORM FUNCTIONS 
#---------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------#
#                Pedal FUNCTIONS 
#---------------------------------------------------------------------------------#


def get_pedals_table():
    print(Pedal.query.all())
    return Pedal.query.all()

#crud helper operations 

def insert_pedal_entry(model,effect,year_intro,series):
    new_entry = Pedal(model=model,effect=effect,year_intro=year_intro,series=series)
    db.session.add(new_entry)
    db.session.commit()

def get_pedal_entry(model):
    return Pedal.query.filter_by(model=model).first()

def delete_pedal_entry(model):
    #query the db first to get the correct mapping 
    entry = Pedal.query.filter_by(model=model).first()
    db.session.delete(entry)
    db.session.commit()
    print('Entry:' + str(entry.model) + '-' + str(entry.effect) + '-' + str(entry.year_intro) + '-' + str(entry.series) + '\n' 
            + "( HAS BEEN DELETED)")

def update_pedal_entry_model(modelname,new_model):
    update = Pedal.query.filter_by(model=modelname).first()
    update.model = new_model
    print(new_model)
    db.session.commit()
   
def update_pedal_entry_effect(model,new_effect):
    update = Pedal.query.filter_by(model=model).first()
    update.effect = new_effect
    print(new_effect)
    db.session.commit()

def update_pedal_entry_year_intro(model,new_year_intro):
    update = Pedal.query.filter_by(model=model).first()
    update.year_intro = new_year_intro
    print(new_year_intro)
    db.session.commit()

def update_pedal_entry_series(model,new_series):
    update = Pedal.query.filter_by(model=model).first()
    update.series = new_series
    print(new_series)
    db.session.commit()

#--------------------------------------------------------------------------------#
#                 Bandmember FUNCTIONS 
#---------------------------------------------------------------------------------#

def get_all_bandmembers():
    return Bandmember.query.all()

# def get_bandmember_entry():


# def insert_bandmember_entry():

# def delete_bandmember_entry():

