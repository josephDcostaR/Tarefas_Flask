from src.model.tarefas import Tarefa
from src.repository.repository import RepositorioTarefas

repositorioTarefas = RepositorioTarefas()

class ServicoTarefas:
    
    def __init__(self, repositorio_tarefas):
        self.repositorio_tarefas = repositorio_tarefas

    def criar_tarefa(self, titulo, descricao, prioridade, data_de_criacao):
        nova_tarefa = Tarefa(len(self.repositorio_tarefas.listar_tarefas()) + 1, titulo, descricao, False, prioridade, data_de_criacao)
        self.repositorio_tarefas.adicionar_tarefa(nova_tarefa)
        return nova_tarefa
    
    def editar_tarefa(self, id, titulo, descricao, prioridade, data_de_criacao):
        tarefa = self.repositorio_tarefas.encontrar_tarefa_por_id(id)
        
        if tarefa:
            tarefa.titulo = titulo
            tarefa.descricao = descricao
            tarefa.prioridade = prioridade
            tarefa.data_de_criacao = data_de_criacao
            return tarefa
        else:
            return None

    def listar_tarefas(self):
        return self.repositorio_tarefas.listar_tarefas()
    
    def entcontar_tarefa_por_id(self, id):
        return self.repositorio_tarefas.encontrar_tarefa_por_id(id)
    
    def remover_tarefa(self ,id):
       tarefa = self.encontrar_tarefa_por_id(id)
   
       if tarefa is None:
            return {'message': 'Tarefa not found'}, 404
        
       self.repositorio_tarefas.deletar_tarefa(id)
        
