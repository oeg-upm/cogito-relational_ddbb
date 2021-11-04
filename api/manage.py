from flask.app import Flask
from project import create_app, db
import os
from flask.cli import FlaskGroup
from project.models import File

app = create_app(os.environ.get("FLASK_CONFIG") or "default")
#cli = FlaskGroup(app)

@app.cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@app.cli.command("seed_db")
def seed_db():
    file = File(file_name="Demo.ifc")
    db.session.add(file)
    db.session.commit()

#if __name__ == "__main__":
#    cli()

