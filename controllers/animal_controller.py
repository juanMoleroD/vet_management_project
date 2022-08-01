import pdb
from flask import Flask, Blueprint, render_template, redirect, request
from repositories import animal_repository, vet_repository, owner_repository
from models.animal import Animal

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/animals")
def show_all_animals():
    all_animals = animal_repository.select_all()
    return render_template("animals/animals.html", all_animals=all_animals)

@animals_blueprint.route("/animals/<id>")
def show_one_animal(id):
    animal = animal_repository.select(id)
    return render_template("animals/animal.html", animal=animal)

@animals_blueprint.route("/animals/new")
def get_new_form():
    vets = vet_repository.select_all()
    owners = owner_repository.select_all()
    return render_template("animals/new.html", vets=vets, owners=owners)

@animals_blueprint.route("/animals", methods=["POST"])
def create_animal():
    name = request.form["name"]
    dob = request.form["date-of-birth"]
    type = request.form["type"]
    owner = owner_repository.select(request.form["owner_id"])
    vet = vet_repository.select(request.form["vet_id"])
    treatement_notes = request.form["treatment_notes"]
    new_animal = Animal(name, dob, type, owner, vet, treatement_notes)
    animal_repository.save(new_animal)
    return redirect("/animals")

@animals_blueprint.route("/animals/<id>/delete", methods=["POST"])
def delete(id):
    animal_repository.delete(id)
    return redirect("/animals")

@animals_blueprint.route("/animals/<id>/edit")
def get_update_form(id):
    vets = vet_repository.select_all()
    owners = owner_repository.select_all()
    animal_to_update = animal_repository.select(id)
    return render_template("animals/edit.html", animal=animal_to_update, vets=vets, owners=owners)

@animals_blueprint.route("/animals/<id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    dob = request.form["date-of-birth"]
    type = request.form["type"]
    owner = owner_repository.select(request.form["owner_id"])
    vet = vet_repository.select(request.form["vet_id"])
    treatement_notes = request.form["treatment_notes"]
    animal_to_update = Animal(name, dob, type, owner, vet, treatement_notes, id)
    animal_repository.update(animal_to_update)
    return redirect("/animals/" + id)

