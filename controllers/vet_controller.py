from flask import Blueprint, Flask, blueprints, render_template, redirect
from repositories import vet_repository, animal_repository

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets")
def show_all_vets():
    all_vets = vet_repository.select_all()
    return render_template("vets/vets.html", all_vets=all_vets)

@vets_blueprint.route("/vets/<id>")
def show_one_vet(id):
    vet = vet_repository.select(id)
    return render_template("vets/vet.html", vet=vet)