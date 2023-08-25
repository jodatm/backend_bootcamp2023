# this is a simple todos API flask application using flask-restx
import os
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from config import app

from routes import blueprint

print()

# Se registra el blueprint en la aplicación Flask
app.register_blueprint(blueprint)

# Este comando ejectura el servidor flask
app.run(host="0.0.0.0", port=50100, debug=True)