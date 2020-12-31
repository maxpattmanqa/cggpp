from application import app, db, Pedal, PedalForm

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

@app.route("/pedalgalleryeditor",methods=['GET','POST'])
def view_pedalgalleryeditor(): 
    error = ""
    form  = PedalForm()
    

    if (request.method =='POST')and(form.validate_on_submit()):
        model = form.model.data
        effect = form.effect.data
        year_intro = form.year_intro.data
        series = form.series.data


    return render_template('pedalgalleryeditor.html',form=form,message=error)


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

def update_pedal_entry_model(model,new_model):
    Pedal.update()
    


def update_pedal_entry_effect(model,new_effect):
    Pedal.update()

def update_pedal_entry_year_intro(model,new_year_intro):
    Pedal.update()

def update_pedal_entry_series(model,new_series):
    Pedal.update()
















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