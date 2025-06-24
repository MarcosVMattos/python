# POO


# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
    
# Objetos
pessoa1 = Pessoa("Duda", 24)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome="Marcos", idade=27)
mensagem = pessoa2.saudacao()
print(mensagem)