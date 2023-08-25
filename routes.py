import os
from flask import Flask, Blueprint, make_response
from flask_restx import Api, Resource, reqparse

from config import app, db

from models import CheckList, check_list_schema
from api_control import listCtrlr, listDto, createListCommand

# Crea el blueprint de la aplicación
blueprint = Blueprint('api', __name__, url_prefix='/api')

# La aplicación API se crea atada a un blueprint
# Tambien puedes atar el API directamente en una aplicación flask convencional
# Si configuras doc=False desabilitaras la pagina UI swagger
# Usa validate=True para permitir la validación de los request en todos los APIS
api = Api(blueprint,
          title="Aplicación de tareas",
          description="Un ejemplo de aplicación API usando flask-restx",
          version="1.0",
          doc="/swagger/",
          validate=True
          )

# Se crea una endpoint indicando la ruta
# Una ruta se representa pot una clase python que herede de "Resource"
# Una petición HTTP maneja funciones definidas por get, post, put, delete
# Create a request parser to handle query parameters
@listCtrlr.route("/")
class CheckListDisplay(Resource):
    @listCtrlr.marshal_list_with(listDto)
    def get(self):        
        list = CheckList.query.all()
        return list
        
    @listCtrlr.expect(createListCommand)
    def post(self):        
        payload = listCtrlr.payload        
        newList = CheckList(title=payload["title"])
        db.session.add(newList)
        db.session.commit()
        return check_list_schema.dump(newList)
    
api.add_namespace(listCtrlr)