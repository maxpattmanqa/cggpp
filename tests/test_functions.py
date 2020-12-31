import pytest

from application.routes import update_pedal_entry_series,update_pedal_entry_year_intro,update_pedal_entry_effect,update_pedal_entry_model,get_pedal_entry, insert_pedal_entry, delete_pedal_entry, Pedal,get_pedals_table, db

#test database crud functions 

#test Read function 

def test_read_pedal_entry():
   entry = get_pedal_entry('MX-101')
   print(entry)
   assert(entry.model == 'MX-101')

def test_insert_pedal_entry():
    model = "test_model"
    effect = "test_effect"
    year_intro  = "test_intro"
    series = "test_series"
    insert_pedal_entry(model,effect,year_intro,series)
    # retrieve entry from db 
    entry = get_pedal_entry(model)
    assert(entry.model == model)
    assert(entry.effect == effect)
    assert(entry.year_intro == year_intro)
    assert(entry.series == series)
    delete_pedal_entry(model)

def test_delete_pedal_entry():
    #delete all previous entries of test ! 
  #  Pedal.query.filter_by(Pedal.model='test_model').all()
    model = "test_model"
    effect = "test_effect"
    year_intro  = "test_intro"
    series = "test_series"
    insert_pedal_entry(model,effect,year_intro,series)
    #query database to see if the entry is there 
    entry = get_pedal_entry(model)
    assert(entry.model == model)
    assert(entry.effect == effect)
    assert(entry.year_intro == year_intro)
    assert(entry.series == series)

    delete_pedal_entry(model)
    entry_exists = bool(db.session.query(Pedal).filter_by(model='test_model').first())
    assert(entry_exists==False)
    #query the database to see if the entry has been deleted 


def test_update_pedal_entry_model():
    model = "test_model"
    effect = "test_effect"
    year_intro  = "test_intro"
    series = "test_series"
    #insert pedal entry into database
    insert_pedal_entry(model,effect,year_intro,series)
    #check that test_model exists 
    entry_exists = bool(get_pedal_entry(model))
    assert(entry_exists== True)
    #call the update function 
    update_pedal_entry_model("test_model",'new_test_model')
    #query function and assert that the change has taken place
    entry_exists = bool(db.session.query(Pedal).filter_by(model='new_test_model').first())
    assert(entry_exists== True)
    # delete the entry
    delete_pedal_entry('new_test_model')
    #comfirm deletion
    entry_exists = bool(db.session.query(Pedal).filter_by(model='new_test_model').first())
    assert(entry_exists== False)
    

def test_update_pedal_entry_effect():
    model = "test_model"
    effect = "test_effect"
    year_intro  = "test_intro"
    series = "test_series"
    insert_pedal_entry(model,effect,year_intro,series)
    entry_exists = bool(get_pedal_entry(model))
    assert(entry_exists== True)
        #call the update function 
    update_pedal_entry_effect(model,'new_test_effect')
    #query function and assert that the change has taken place
    entry_exists = bool(db.session.query(Pedal).filter_by(effect='new_test_effect').first())
    assert(entry_exists== True)
    # delete the entry
    delete_pedal_entry('test_model')
    #comfirm deletion
    entry_exists = bool(db.session.query(Pedal).filter_by(model='test_model').first())
    assert(entry_exists== False)

def test_update_pedal_entry_year_intro():
    model = "test_model"
    effect = "test_effect"
    year_intro  = "test_intro"
    series = "test_series"
    insert_pedal_entry(model,effect,year_intro,series)
    entry_exists = bool(get_pedal_entry(model))
    assert(entry_exists== True)
    #call the update function 
    update_pedal_entry_year_intro(model,'new_test_intro')
    #query function and assert that the change has taken place
    entry_exists = bool(db.session.query(Pedal).filter_by(year_intro='new_test_intro').first())
    assert(entry_exists== True)
    # delete the entry
    delete_pedal_entry('test_model')
    #comfirm deletion
    entry_exists = bool(db.session.query(Pedal).filter_by(model='test_model').first())
    assert(entry_exists== False)


def test_update_pedal_entry_series():
    model = "test_model"
    effect = "test_effect"
    year_intro  = "test_intro"
    series = "test_series"
    insert_pedal_entry(model,effect,year_intro,series)
    entry_exists = bool(get_pedal_entry(model))
    assert(entry_exists== True)
        #call the update function 
    update_pedal_entry_series(model,'new_test_series')
    #query function and assert that the change has taken place
    entry_exists = bool(db.session.query(Pedal).filter_by(series='new_test_series').first())
    assert(entry_exists== True)
    # delete the entry
    delete_pedal_entry('test_model')
    #comfirm deletion
    entry_exists = bool(db.session.query(Pedal).filter_by(model='test_model').first())
    assert(entry_exists== False)




   