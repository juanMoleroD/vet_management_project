from flask import Flask, Blueprint, redirect

#Blueprint imports
from controllers.vet_controller import vets_blueprint

app = Flask(__name__)

#Blueprint loading
app.register_blueprint(vets_blueprint)

if __name__ == "__main__":
    app.run()

@app.route("/")
def index():
    return redirect("/vets") 