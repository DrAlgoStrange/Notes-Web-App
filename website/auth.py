''' so the views page basically stores the app routes the user sign in page end point actually its actually a blueprint of where each sign in request will redirected '''

from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash # these modules will hash the enterd password to store in database 
from . import db
from flask_login import login_user, login_required, logout_user,current_user #we can use current user because we have used UserMixin this current use will have all information of the user like email pass notes id if user is logged in

auth=Blueprint('auth',__name__) #this delcears views as a blueprint object capable of redirecting to new urls

@auth.route('login',methods=['POST','GET'])
def login():
    data= request.form    #this will collect the data from the from attribute in HTML when there is a POST request
    #print (data)   # ImmutableMultiDict([('email', 'stripathy461@gmail.com'), ('password', 'stripa50')])
    if request.method=='POST':
        email=data.get('email')
        password=data.get('password')
        user = User.query.filter_by(email=email).first()
        #print(user.notes)
        if user:
            if check_password_hash(user.password,password):
                flash("LogIn Success", category="success")
                login_user(user , remember=True)
                return redirect(url_for('views.home_page'))
            else:
                flash("Invalid password", category="error")
        else:
            flash("Could not find a user with this Email id", category="error")
    return render_template('login.html')

@auth.route('logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('signup',methods=['POST','GET'])
def signin():
    if request.method=='POST':
        data=request.form
        print(data)
        name=data.get('name')
        email=data.get('email')
        password1=data.get('password1')
        password2=data.get('password2')
        user= User.query.filter_by(email=email).first()
        if user:
            flash("User already exists please use a other Email", category="error")
        elif '@' not in email or '.com' not in email:
            flash("Please enter a valid Email Address",category="error")
        elif len(password1)<7:
            flash("Length of the password is less than 7",category="error")
        elif password1!=password2:
            flash("Passwords don't match",category="error")
        else: #insert to db
            new_user=User(name=name , email=email ,password=generate_password_hash(password1,method='pbkdf2:sha512'))
            db.session.add(new_user)
            db.session.commit()
            flash(f"Hi {name} your account is created successfully !!. Please return to Login page to continue",category="success")
            login_user(user , remember=True)
            return redirect(url_for('views.home_page'))
    return render_template('signup.html')