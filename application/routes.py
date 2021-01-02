from application import app, db, Pedal
from application.forms import InsertPedalForm , DeletePedalForm, UpdatePedalForm

from flask import render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
Session.configure(bind=db)

session = Session()



@app.route("/")
@app.route("/home")
def view_home():  return render_template('home.html')

@app.route("/kytopia")
def view_kytopia(): return render_template('kytopia.html')

# @app.route("/pedalgalleryeditor")
# def view_pedalgalleryeditor():
#     insert_form = InsertPedalForm()
#     update_form = UpdatePedalForm()
#     delete_form = DeletePedalForm()
#     return render_template('pedalgalleryeditor.html',insert_form=insert_form,update_form=update_form,delete_form=delete_form)

# @app.route("/pedalgalleryeditor_insert",methods=['GET','POST'])
# def view_pedalgalleryeditor_insert():
#     insert_form = InsertPedalForm()
#     update_form = UpdatePedalForm()
#     delete_form = DeletePedalForm()



# @app.route("/pedalgalleryeditor_update",methods=['GET','POST'])
# def view_pedalgalleryeditor_update(): 

# @app.route("/pedalgalleryeditor_delete",methods=['GET','POST'])
# def view_pedalgalleryeditor_delete(): 

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







@app.route("/pedalgallery")
def view_pedalgallery():
    pedals = get_pedals_table()
    return render_template('pedalgallery.html',pedals=pedals)


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
















# #   form = TaskForm()
# #     if request.method == "POST":
# #         if form.validate_on_submit():
#             new_task = Tasks(description=form.description.data)
#             db.session.add(new_task)
#             db.session.commit()
#             return redirect(url_for("home"))
#     return render_template("add.html", title="Create a Task", form=form)

# @app.route("/complete/<int:id>")
# def complete(id):
#     task = Tasks.query.filter_by(id=id).first()
#     task.completed = True
#     db.session.commit()
#     return f"Task {id} is now complete"

# @app.route("/incomplete/<int:id>")
# def incomplete(id):
#     task = Tasks.query.filter_by(id=id).first()
#     task.completed = False
#     db.session.commit()
#     return f"Task {id} is now incomplete"

# @app.route("/update/<int:id>", methods=["GET", "POST"])
# def update(id):
#     form = TaskForm()
#     task = Tasks.query.filter_by(id=id).first()
#     if request.method == "POST":
#         task.description = form.description.data
#         db.session.commit()
#         return redirect(url_for("home"))

#     return render_template("update.html", form=form, title="Update Task", task=task)

# @app.route("/delete/<int:id>", methods=["GET", "POST"])
# def delete(id):
#     task = Tasks.query.filter_by(id=id).first()
#     db.session.delete(task)
#     db.session.commit()
#     return redirect(url_for("home"))

# @app.route("/layout")
# def layout():
#     return render_template("layout.html")


#this function queries our database and returns the values 
#