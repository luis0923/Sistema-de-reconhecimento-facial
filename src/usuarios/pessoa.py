class pessoa:
    def __init__(self, nome, embedding, turma, presença):
        self.set_embedding(embedding)
        self.set_nome(nome)
        self.set_turma(turma)
        self.set_presença(presença)
        
  #Metodos Settersss
  
    def set_embedding(self, embedding):
        self.embedding = embedding

    def set_nome(self, nome):
        self.nome = nome

    def set_presença(self, presença):
        self.presença = presença
    
    def set_turma(self, turma):
        self.turma = turma

  #metodos getters

    def get_nome(self):
        return self.nome
    
    def get_embedding(self):
        return self.embedding
    
    def get_presença(self):
        return self.presença
    
    def get_turma(self):
        return self.turma