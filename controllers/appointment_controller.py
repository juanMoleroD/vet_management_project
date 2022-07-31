from flask import Flask, Blueprint,request, redirect, render_template
from repositories import appointment_repository
from models.appointment import Appointment

appointments_blueprint = Blueprint("appointments", __name__)

