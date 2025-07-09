from app_folder import app
from flask import redirect, render_template, request, jsonify
from app_folder.models import User, db

@app.route("/emp", methods = ['GET', 'POST'])
def view():
    if request.method == 'GET':

        user_details = User.query.all()        
        users = []
        for user in user_details:
            users.append({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "salary": user.salary
            })
        return jsonify(users)
    
    if request.method == 'POST':
        new_user = request.form['user']
        new_email = request.form['email']
        new_salary = request.form['salary']
        user = User(username=new_user, email=new_email, salary=new_salary)
        db.session.add(user)
        db.session.commit()
        return f"User with id: {user.id} created successfully", 201

@app.route("/emp/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def check_by_id(id):
    if request.method == 'GET':

        user_id = User.query.filter_by(id=id).first()
        if user_id is not None:
            return (user_id.to_dict())
        else:
            return "Something went wrong !"
        
    if request.method == 'PUT':
        new_user = request.form['user']
        new_email = request.form['email']
        new_salary = request.form['salary']
        user_modify = User.query.filter_by(id=id).first()
        user_modify.salary = new_salary
        user_modify.email  = new_email
        user_modify.username  = new_user
        db.session.commit()
        return jsonify(user_modify.to_dict())

    if request.method == 'DELETE':
        delete_user = User.query.filter_by(id=id).first()
        db.session.delete(delete_user)
        db.session.commit()
        return f"The user with id: {id} has been deleted", 200

        

        



