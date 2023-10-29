
# Repositório (simulado)
class RepositorioTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        return self.tarefas
    
    def encontrar_tarefa_por_id(self, id):
        for tarefa in self.tarefas:
            if tarefa.id == id:
                return tarefa
        return None
    
    def deletar_tarefa(self, tarefa):
        if tarefa in self.tarefas:
            self.tarefas.remove(tarefa)
        