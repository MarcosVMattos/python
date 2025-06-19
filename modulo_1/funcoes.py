# def (definition) == função
def saudacao(nome):
    print(f"Olá, {nome}!")

print("Chamando a função saudação:")
saudacao("Alice")
saudacao("Mark")

# Função com retorno
def quadrado(num):
    resultado = num ** 2
    return resultado

print("\nChamando função quadrado:")
x = quadrado(5)
print("Resultado da função quadrado:", x)


def soma(n1, n2):
    resultado = n1 + n2
    return resultado

print("\nChamando a função soma:")
numero_1 = 20
numero_2 = 50
print(f"A soma do numero {numero_1} e {numero_2} é {soma(numero_1, numero_2)}")