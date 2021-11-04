from flask import jsonify, request, flash, url_for, make_response, redirect
from werkzeug.utils import secure_filename
import os
from . import main
from ..models import File
from .. import db

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
files_dir = os.path.join(base_dir, "files")

os.makedirs(files_dir, exist_ok=True)

@main.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        if "file" not in request.files:
            flash("No file part")
            return redirect(url_for("main.upload"))

        ifc_file = request.files["file"]
        filename = secure_filename(ifc_file.filename)

        if filename == "":
            flash("No file selected")
            return redirect(url_for("main.upload"))

        if File.query.filter_by(file_name=filename).first() is not None:
            flash("File already exists in the database.")
            return redirect(url_for("main.upload"))
        else:
            description = request.args.get("description", "")
            construction_ifc_id = request.args.get("construction_ifc_id", "")
            file_entry = File(file_name=ifc_file.filename, description=description, construction_ifc_id=construction_ifc_id)
            ifc_file.save(os.path.join(files_dir, filename))
            db.session.add(file_entry)
            db.session.commit()

        return make_response(jsonify({"response": "Success"}), 202)
    
    return make_response(jsonify({"response": "Upload a new file"}), 200)


@main.route("/constructions/<construction_id>", methods=["GET"])
def get_ifc_file(construction_id):

    ifc_file = File.query.filter_by(construction_id=construction_id).first()
