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

updateListCommand = listCtrlr.model('Update List command', {
    'title': fields.String(required=True, description='list description'),    
})

listDto = listCtrlr.model('List DTO', {
    'id': fields.Integer(description='Id of List'),
    'title': fields.String(description='List details')    
})

taskCtrlr = Namespace(
    'task', path="/task", description='Task API Controller')

createTaskCommand = taskCtrlr.model('Create task command', {
    'value': fields.String(required=True, description='task description'),
    'order': fields.Integer(required=True, description='priority of task'),
    'completed': fields.Boolean(required=True, description='task completion'),
    'list_id': fields.Integer(required=True, description='Task must be assigned to a List')
})

updateTaskCommand = taskCtrlr.model('Update Task command', {
    'value': fields.String(required=True, description='task description'),
    'order': fields.Integer(required=True, description='priority of task'),
    'completed': fields.Boolean(required=True, description='task completion'),
    'list_id': fields.Integer(required=True, description='Task must be assigned to a List')
})

taskDto = taskCtrlr.model('Task DTO', {
    'id': fields.Integer(description='Id of Task'),
    'value': fields.String(description='Task details'),
    'order': fields.Integer(description='Task order'),
    'completed': fields.Boolean(required=True),
    'list_id': fields.Integer(description='Task must be assigned to a List')
})

langchainCtrlr = Namespace(
    'langchain', path="/langchain", description='List API for Langchain')

createlangChainCommand = langchainCtrlr.model('Create LangChain command', {
    'prompt': fields.String(required=True, description='template prompt'),    
})