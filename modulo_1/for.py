print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento, end=' ')
print("\n")

print("For utilizando tupla")
tupla = [1, 2, 3, 4, 5]
for elemento in tupla:
    print(elemento, end=' ')
print("\n")

print("For utilizando dicionário - keys")
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
for chave in pessoa.keys():
    print(chave)
print("\n")

print("For utilizando dicionário - values")
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
for valor in pessoa.values():
    print(valor)
print("\n")

print("For utilizando dicionário - items")
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
for key, values in pessoa.items():
    print(f"{key} : {values}")

# range() : intervalo numérico
# [0, 1, 2, 3, 4]
print("\nUtilizando a função range()")
for numero in range(5):
    print("Número:", numero)

print("\nUtilizando a função range() com len()")
lista = ["a", "b", "c", "d", "e"]
for indice in range(len(lista)):
    print("Indice:", indice)
    print("Elemento:", lista[indice]) 

# enumerate()
print("\nUtilizando a função enumerate()")
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"Indice = {indice}, Valor = {valor}")
    if indice == 1:
