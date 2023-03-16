from flask import *
from flask.views import View
from flask_appbuilder import ModelView
from flask_appbuilder.models.mongoengine.interface import MongoEngineInterface
from flask_appbuilder.api import *
from flask_appbuilder.security.api import *
from .models import *
from .urls import *
from config import *

def main_page():
    return render_template('reg.html')

def resister_view():
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    password = request.form["password"]
    mobile_no = request.form["mobile_no"]
    email = request.form["email"]
    data = myuser(
        firstname = firstname,
        lastname = lastname,
        password = password,
        mobile_no = mobile_no,
        email = email,
    )
    data.save()
    return render_template('login.html')

def login():
    return render_template('login.html')

def login_view():
    email = request.form["email"]
    password = request.form["password"]
    user = myuser.objects(email=email,password=password).first()
    data={
        "user_id":user.id,
        "name": user.firstname
    }
    if user:
        return render_template('userpage.html',data=data)
    else:
        return "plz enter crt data"
    
def booking(user_id):
    return render_template('booking.html',data=user_id)


def ticket_booking(user_id):
    movie_name = request.form["movie_name"]
    ticket_price = 100
    ticket_number = request.form["ticket_number"]
    no_of_ticket = request.form["no_of_ticket"]
    
    user = myuser.objects(id=user_id).first()
    
    data = ticket_history(
        movie_name = movie_name,
        ticket_price = ticket_price,
        ticket_number = ticket_number,
        no_of_ticket = no_of_ticket,
        total_ticket = int(ticket_price) * int(no_of_ticket),
        
        status = "Booked"
    )
    user.ticket.append(data)
    user.save()
    return "successfully booked"

def cancel_ticket():
    movie_name = request.form["movie_name"]
    ticket_number = request.form["ticket_number"]
    ticket = ticket_history.objects(movie_name=movie_name,ticket_number=ticket_number).first()
    ticket.update(status="cancelled")
    ticket.save()

def history(user_id):
    user = myuser.objects(id=user_id).first()
    data_list = []
    for i in user.ticket:
        data = {
            "movie_name" : i.movie_name,
            "ticket_price" : i.ticket_price,
            "ticket_number" : i.ticket_number,
            "total_ticket" : i.total_ticket,
            "no_of_ticket" : i.no_of_ticket,
            "status" : i.status
        }
        data_list.append(data)
    return data_list

def cancel_page(user_id):
    user = myuser.objects(id=user_id).first()
    data_list = []
    for i in user.ticket:
        print(i)
        data = {
            "movie_name" : i.movie_name,
            "ticket_price" : i.ticket_price,
            "ticket_number" : i.ticket_number,
            "total_ticket" : i.total_ticket,
            "no_of_ticket" : i.no_of_ticket,
            "status" : i.status
        }
        data_list.append(data)
        
    return render_template("cancel.html",userid = user.id,data=data)

def cancel_ticket(user_id):
    user = myuser.objects(id=user_id).first()
    movie_name = request.form["movie_name"]
    ticket_number = request.form["ticket_number"]
    for i in user.ticket:
        if i.movie_name == movie_name and i.ticket_number == ticket_number:
            print("**********")
            i.status = "cancel"
            user.save()
    return "succefully cancelled"