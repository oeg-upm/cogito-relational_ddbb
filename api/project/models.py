from enum import unique
from . import db

class File(db.Model):
    __tablename__ = "files"

    file_id = db.Column(db.Integer, primary_key=True, unique=True)
    construction_ifc_id = db.Column(db.String(64))
    file_name = db.Column(db.String(64))
    description = db.Column(db.String(64))