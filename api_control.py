from flask_restx import fields, Namespace

# Se crea el API namespace
# El Namespace sirve para agrupar rutas/endpoints como si fuera un MVC
listCtrlr = Namespace(
    'list', path="/list", description='List API Controller')

# Creamos los modelos del API
# Se valida los tipos de datos de cada modelo
# Cada objeto JSON puede ser validado o mapeado usando este modelo 
createListCommand = listCtrlr.model('Create List command', {
    'title': fields.String(required=True, description='list description'),    
})

listDto = listCtrlr.model('List DTO', {
    'id': fields.Integer(description='Id of List'),
    'title': fields.String(description='List details')    
})