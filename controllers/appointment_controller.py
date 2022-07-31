import pdb
from flask import Flask, Blueprint,request, redirect, render_template
from repositories import animal_repository, appointment_repository
from models.appointment import Appointment

appointments_blueprint = Blueprint("appointments", __name__)

@appointments_blueprint.route("/appointments")
def show_all_appointments():
    all_appointments = appointment_repository.select_all()
    return render_template("appointments/appointments.html", appointments=all_appointments)

@appointments_blueprint.route("/appointments/<id>")
def show_one_appointment(id):
    appointment = appointment_repository.select(id)
    return render_template("appointments/appointment.html", appointment=appointment)

@appointments_blueprint.route("/appointments/new")
def get_new_form():
    all_animals = animal_repository.select_all()
    return render_template("appointments/new.html", animals=all_animals)

@appointments_blueprint.route("/appointments", methods=["POST"])
def create_appointment():

    animal = animal_repository.select(request.form["animal_id"])
    check_in = request.form["check_in"]
    check_out = request.form["check_out"]
    new_appointment = Appointment(animal, check_in, check_out)
    appointment_repository.save(new_appointment)
    return redirect("/appointments")

