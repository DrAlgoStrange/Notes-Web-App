'''this the models file where we are goinf to store the database table schemas for our project so we will have two tables one is USERS that will contain the information of all the users there passwords and emails and the NOTES table that will contain the notes of all the users both will be connected by primary key ID '''

from . import db 
from flask_login import UserMixin #this is a flask module that helps in user logins 
from sqlalchemy.sql import func # this acctually helps in getting the current date and time 

class Notes(db.Model):
    id = db.Column(db.Integer , primary_key=True)   #will create a coulmn ID that will be auto populated by flask with unique values
    data = db.Column(db.String(100000)) #this is actually the size of string this field can store 
    date = db.Column(db.DateTime(timezone=True),default=func.now()) #will pick a timezone and func.now() will give value
    user_id= db.Column(db.Integer , db.ForeignKey('user.id')) #now it is connected with id coulmn of the users table as its SQL so its case insensative 


# class Videos(db.Model):
#      pass # Future progress
# class Reminder(db.Model):
#      pass # Future progress


class User(db.Model, UserMixin): # UserMixin because this class will store the current user session
     id = db.Column(db.Integer , primary_key=True)
     email = db.Column(db.String(100), unique=True)
     password = db.Column(db.String(500))
     name = db.Column(db.String(200))
     notes =db.relationship('Notes') #so basically whenever a new note is created its id is stored in this field as list