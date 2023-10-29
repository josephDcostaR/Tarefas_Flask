from flask import Blueprint, jsonify, request, Flask
from flask_restful import Api
from services.servicesTarefas import ServicoTarefas
from repository.repository import RepositorioTarefas


app = Flask(__name__)
tarefas_route = Blueprint('tarefas_route', __name__)
api = Api(tarefas_route)
repositorio_tarefas = RepositorioTarefas() # Criando uma única instância de RepositorioTarefas
servico_tarefas = ServicoTarefas(repositorio_tarefas) #Guardando a instancia de RepositorioTarefas

#ENDPOINTS DA API
@tarefas_route.route('/tarefas', methods=['GET'])
def listar_tarefas():
    tarefas = servico_tarefas.listar_tarefas()
    tarefas_serializadas = [tarefa.to_dict() for tarefa in tarefas]
    return jsonify(tarefas_serializadas)

@tarefas_route.route('/tarefas/<int:id>', methods=['GET'])
def encontrar_tarefa_por_id(id):
    tarefa = servico_tarefas.entcontar_tarefa_por_id(id)
    
    if tarefa is not None:
        return jsonify(tarefa.to_dict())
    else:
        return {'message': 'Tarefa not found'}, 404

@tarefas_route.route('/tarefas', methods=['POST'])
def criar_tarefas():
    tarefas = request.json
    if not isinstance(tarefas, list):
        return jsonify({'message': 'Requisição inválida. Envie uma lista de tarefas no formato JSON.'}), 400


    for tarefa in tarefas:
        titulo = tarefa.get('titulo')
        descricao = tarefa.get('descricao')
        prioridade = tarefa.get('prioridade')
        data_de_criacao = tarefa.get('data_de_criacao')

        if titulo and descricao and prioridade and data_de_criacao:
            servico_tarefas.criar_tarefa(titulo, descricao, prioridade, data_de_criacao)

    return jsonify({'message': 'Tarefas criadas com sucesso'})

@tarefas_route.route('/tarefas/<int:id>', methods=['PUT'])
def editar_tarefa(id):
    tarefa_data = request.json
    titulo = tarefa_data.get('titulo')
    descricao = tarefa_data.get('descricao')
    prioridade = tarefa_data.get('prioridade')
    data_de_criacao = tarefa_data.get('data_de_criacao')
    
    if titulo and descricao and prioridade and data_de_criacao:
        tarefa = servico_tarefas.editar_tarefa(id, titulo, descricao, prioridade, data_de_criacao)
        if tarefa:
            return jsonify(tarefa.to_dict())
    
    return jsonify({'message': 'Tarefa not found or invalid data'}), 404
        
@tarefas_route.route('/tarefas/<int:id>', methods=['DELETE'])
def remover_tarefa(id):
     tarefa = servico_tarefas.entcontar_tarefa_por_id(id)
     
     if tarefa is not None:
           repositorio_tarefas.deletar_tarefa(tarefa)
           return jsonify({'message': 'Tarefa removida com sucesso'})
     else:
        return jsonify({'message': 'Tarefa not found'}), 404  
      