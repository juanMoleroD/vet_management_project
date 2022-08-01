from flask import Blueprint, request, redirect, render_template
from models.note import Note
from repositories import animal_repository, note_repository

notes_blueprint = Blueprint("notes", __name__)

@notes_blueprint.route("/notes", methods=["POST"])
def add_new():
    content = request.form["content"]
    animal = animal_repository.select(request.form["animal_id"])
    new_note = Note(animal, content)
    note_repository.save(new_note)
    return redirect("/animals/" + str(animal.id))