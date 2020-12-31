import pytest

from application.routes import get_pedal_entry, insert_pedal_entry, delete_pedal_entry, Pedal,get_pedals_table, db

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
    
def test_get_pedals_table():
   get_pedals_table()





#def test_update_pedal_entry():




   