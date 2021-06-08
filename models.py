class Notas:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

class Usuario(Notas):
    def __init__(self, username, senha):
        self.username = username
        self.senha = senha

    def nova_nota(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo
