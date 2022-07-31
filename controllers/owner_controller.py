import pdb
from flask import Flask, Blueprint, render_template, redirect, request
from repositories import animal_repository, owner_repository
from models.owner import Owner

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route("/owners")
def show_all_owners():
    all_owners = owner_repository.select_all()
    return render_template("owners/owners.html", all_owners=all_owners)

@owners_blueprint.route("/owners/<id>")
def show_one_owner(id):
    owner = owner_repository.select(id)
    animals_owned = animal_repository.select_all_with_owner_id(id)
    return render_template("owners/owner.html", owner=owner, animals=animals_owned)

@owners_blueprint.route("/owners/new")
def get_new_form():
    return render_template("owners/new.html")

@owners_blueprint.route("/owners", methods=["POST"])
def create_owner():
    name = request.form["name"]
    contact_details = request.form["contact-details"]
    registered = True #by default
    new_owner = Owner(name, contact_details, registered)
    owner_repository.save(new_owner)
    return redirect("/owners")

@owners_blueprint.route("/owners/<id>/delete", methods=["POST"])
def delete(id):
    owner_repository.delete(id)
    return redirect("/owners")

@owners_blueprint.route("/owners/<id>/edit")
def get_update_form(id):
    owner_to_update = owner_repository.select(id)
    return render_template("owners/edit.html", owner=owner_to_update)

@owners_blueprint.route("/owners/<id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    contact_details = request.form["contact-details"]
    registration = request.form["registered"]
    owner_to_update = Owner(name, contact_details, registration ,id)
    owner_repository.update(owner_to_update)
    return redirect("/owners/" + id)