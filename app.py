from flask import Flask
#from repository.repository import RepositorioTarefas
#from view.view import TarefasView
from controller.tarefasController import tarefas_route
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)

#CONSERTE O METODO DE CRIAR TAREFAS!!!!
#TENTE FAZER OS ENDPINTS DE BUSCAR_TAREFA E O DELETAR _TAREFA

""" 
link do swagger - 
http://localhost:5001/api/swagger

No postman
http://localhost:5001/api/tarefas

"""

def setup_app():
    
    app.static_url_path = '/static'
    app.static_folder = 'static'

    app.register_blueprint(tarefas_route, url_prefix='/api')
    
        # Defina as informações gerais da API
    app.config['SWAGGER_INFO'] = {
    'title': 'Tarefas_Flash: Sua API de Tarefas',
    'version': '2.0',
    'description': 'Documentação interativa da API de Tarefas',
    }
        
    # Configure o Swagger UI
    SWAGGER_URL = '/api/swagger'  # URL da página do Swagger
    API_URL = '/static/swagger.json'  # Rota do Swagger JSON
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Tarefas_Flash: Sua API de Tarefas"
        }
    )

    # Registre o Swagger UI Blueprint
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    setup_app()
    app.run(host='0.0.0.0', port=5001, debug=True)
