from flask import Flask, Blueprint, render_template, redirect
from repositories import owner_repository

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route("/owners")
def all_owners():
    all_owners = owner_repository.select_all()
    return render_template("owners/owners.html", all_owners=all_owners)

@owners_blueprint.route("/owners/<id>")
def owner(id):
    owner = owner_repository.select(id)
    return render_template("owners/owner.html", owner=owner)