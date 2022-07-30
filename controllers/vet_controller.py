from flask import Blueprint, Flask, blueprints, render_template, redirect, request
from repositories import vet_repository, animal_repository
from models.vet import Vet

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets")
def show_all_vets():
    all_vets = vet_repository.select_all()
    return render_template("vets/vets.html", all_vets=all_vets)

@vets_blueprint.route("/vets/<id>")
def show_one_vet(id):
    vet = vet_repository.select(id)
    return render_template("vets/vet.html", vet=vet)

@vets_blueprint.route("/vets/new")
def get_new_form():
    return render_template("vets/new.html")

@vets_blueprint.route("/vets", methods=["POST"])
def create_vet():
    name = request.form['name']
    vet = Vet(name)
    vet_repository.save(vet)
    return redirect("/vets")

@vets_blueprint.route("/vets/<id>/delete", methods=["POST"])
def delete(id):
    vet_repository.delete(id)
    return redirect("/vets")

@vets_blueprint.route("/vets/<id>/edit")
def get_update_form(id):
    vet_to_edit = vet_repository.select(id)
    return render_template("vets/edit.html", vet_to_edit=vet_to_edit)

@vets_blueprint.route("/vets/<id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    updated_vet = Vet(name, id)
    vet_repository.update(updated_vet)
    return redirect("/vets/" + id)