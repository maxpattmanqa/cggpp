import pytest
from flask_testing import TestCase


from application.routes import update_pedal_entry_series,update_pedal_entry_year_intro,update_pedal_entry_effect,update_pedal_entry_model,get_pedal_entry, insert_pedal_entry, delete_pedal_entry, Pedal,get_pedals_table, db
from application import app,db,populate_database


#test database crud functions 

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY="TEST_SECRET_KEY",
            DEBUG=True)
        return app

     #will be run before every test    
    def setUp(self):
        db.create_all()
        populate_database()

class TestCRUD(TestBase):

    def test_read_pedal_entry(self):
        entry = get_pedal_entry('MX-101')
        print(entry)
        assert(entry.model == 'MX-101')

    def test_insert_pedal_entry(self):
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
        
    def test_delete_pedal_entry(self):
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


    def test_update_pedal_entry_model(self):
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
    

    def test_update_pedal_entry_effect(self):
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

    def test_update_pedal_entry_year_intro(self):
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

    def test_update_pedal_entry_series(self):
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




   