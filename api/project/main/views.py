from flask import json, jsonify, request, flash, url_for, make_response, redirect, abort
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
            return make_response(jsonify({"response": "No file part"}))

        ifc_file = request.files["file"]

        filename = request.args.get("filename")
        description = request.args.get("description", "")
        file_id = request.args.get("file_id", "")

        if filename == "":
            return make_response(jsonify({"response": "No file selected"}))

        if filename[-4:] != ".ifc":
            return make_response(jsonify({"response": "File extension not allowed, the file should be an IFC file"}))
        
        file_entry = File(file_name=filename, description=description, construction_ifc_id=file_id)
        ifc_file.save(os.path.join(files_dir, filename))
        db.session.add(file_entry)
        db.session.commit()

        return make_response(jsonify({"response": "Success"}), 201)
    
    return make_response(jsonify({"response": "Upload a new file"}), 200)


@main.route("/files/<id>", methods=["GET"])
def get_ifc_file(id):

    file_record = File.query.filter_by(construction_ifc_id=id).first()

    if file_record is None:
        abort(404)

    filepath = os.path.join(files_dir, file_record.file_name)
    file = open(filepath).read()
    
    return file