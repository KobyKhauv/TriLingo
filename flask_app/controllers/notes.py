from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.note import Note
from flask_app.models.user import User


@app.route('/notes')
def new_note():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('notes.html',user=User.get_by_id(data))


@app.route('/create/note',methods=['POST'])
def create_sighting():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Note.validate_note(request.form):
        return redirect('/notes')
    data = {
        "notestaken": request.form["notestaken"],
        "date_of_note": request.form["date_of_note"],
        "user_id": session["user_id"]
    }
    Note.save(data)
    return redirect('/dashboard')

@app.route('/edit/sighting/<int:id>')
def edit_sighting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("notes.html",edit=Sighting.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/note',methods=['POST'])
def update_note():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Note.validate_note(request.form):
        return redirect('/new/note')
    data = {
        "notestaken": request.form["notestaken"],
        "date_of_note": request.form["date_of_note"],
        "id": request.form['id']
    }
    Note.update(data)
    return redirect('/dashboard')

@app.route('/note/<int:id>')
def show_note(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("notes.html",note=Note.get_one(data),user=User.get_by_id(user_data))

@app.route('/destroy/note/<int:id>')
def destroy_note(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Note.destroy(data)
    return redirect('/dashboard')
