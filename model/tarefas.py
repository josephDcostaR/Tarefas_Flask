# Serviços de Aplicação

# Entidades
class Tarefa:
    
    def __init__(self, id, titulo, descricao, concluida, prioridade, data_de_criacao):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida
        self.prioridade = prioridade
        self.data_de_criacao = data_de_criacao
        
    def to_dict(self):
            return {
                "id": self.id,
                "titulo": self.titulo,
                "descricao": self.descricao,
                "concluida": self.concluida,
                "prioridade": self.prioridade,
                "data_de_criacao": self.data_de_criacao
            }


# Objeto de Valor para Data de Criação
class DataDeCriacao:
    
    def __init__(self, ano, mes, dia):
        self.ano = ano
        self.mes = mes
        self.dia = dia

    #def __eq__(self, other):
    #    if not isinstance(other, DataDeCriacao):
    #        return False
    #    return self.ano == other.ano and self.mes == other.mes and self.dia == other.dia

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"

    #def __repr__(self):
    #    return f"DataDeCriacao({self.ano}, {self.mes}, {self.dia})"