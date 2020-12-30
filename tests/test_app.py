# import unittest
# from flask import url_for
# from flask_testing import TestCase
# from os import getenv

# from application import app,db,Pedal

# #create the base Class

# class TestBase(TestCase):
#     def create_app(self):
#         #change to get env variables 
#         # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
#         app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
#                 SECRET_KEY='TEST_SECRET_KEY',
#                 DEBUG=True
#                 )
#         return app

#     def setUp(self):
#           """
#         Will be called before every test
#         """
#         # Create table
#         db.create_all()

#         # Create test registree
#         sample1 = Pedal(model="MX-101",effect="Phase 90",year_intro="1974",series="Reference")

#         # save users to database
#         db.session.add(sample1)
#         db.session.commit()
    
#     def tearDown(self):
#         """
#         Will be called after every test
#         """

#         db.session.remove()
#         db.drop_all()

# class TestViews(TestBase):

#     #test pedal gallery editor crud 

#     def test_pedalgalleryeditor_add_entry_post(self):
#         response = self.client.post()
    
       

      
