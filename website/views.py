''' so the views page basically stores the app routes end points actually its actually a blueprint of where each request will redirected '''

from flask import Blueprint ,render_template,redirect,url_for,request,flash,jsonify
from flask_login import  login_required,current_user
from .models import Notes
from . import db
import json

views=Blueprint('views',__name__) 

@views.route('/', methods=['POST','GET'])
@login_required
def home_page():
    if (request.method=="POST"):
        data = request.form
        note=data.get('note')
        if len(note)>=1:
            new_note=Notes(data=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash(f"Note Created successfully",category="success")


    return render_template('home.html',user=current_user)#now in our home template we can access the user details as current_user is storing all the details 

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Notes.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})