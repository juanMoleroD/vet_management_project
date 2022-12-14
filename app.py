from flask import Flask, Blueprint, redirect, render_template

#Blueprint imports
from controllers.vet_controller import vets_blueprint
from controllers.owner_controller import owners_blueprint
from controllers.animal_controller import animals_blueprint
from controllers.appointment_controller import appointments_blueprint
from controllers.note_controller import notes_blueprint

app = Flask(__name__)

#Blueprint loading
app.register_blueprint(vets_blueprint)
app.register_blueprint(owners_blueprint)
app.register_blueprint(animals_blueprint)
app.register_blueprint(appointments_blueprint)
app.register_blueprint(notes_blueprint)

if __name__ == "__main__":
    app.run()

@app.route("/")
def index():
    return render_template("home.html")