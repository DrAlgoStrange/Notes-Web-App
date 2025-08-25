from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db=SQLAlchemy()    #creating a database 
DB_NAME="database.db"

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']= "surya@123"
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'    #making a sqlite db  
    db.init_app(app)

    from .views import views
    from .auth import auth
    
    

    app.register_blueprint(views, url_prefix='/') #will redirect any request with http://127.0.0.1:5000/views/home  as prefix to views home page
    app.register_blueprint(auth, url_prefix='/auth/')#will redirect any request with http://127.0.0.1:5000/auth/home  as prefix to auth home page


    from .models import User,Notes

    create_database(app) # we pass our app to this function that will create DB for this app and if we pass a another app it can create DB for that as well 


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #telling flask which user we are looling for 

    return app


def create_database(app):# will create the data base is not created previously
    if not path.exists('Notes App/instances'+DB_NAME):
         with app.app_context():   #  push the app context
            db.create_all()
            print("DB created")