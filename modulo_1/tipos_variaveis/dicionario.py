# Criando um dicionário (O primeiro é a chave e o segundo é o valor)
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print(pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Adicionando intens no dicionário
pessoa["moto"] = "xtrem"
print("Adicionando veículo:", pessoa)

# Como alterar um valor do dicionário
pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor (del)
del pessoa["moto"]
print("Dicionário atualizado:", pessoa)

# Métodos:
# Keys()
chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:",  chaves[0])

# Values
valores = list(pessoa.values())
print("Valores do dicionário:", valores)
print("Primeiro valor do dicionário:", valores[0])

# Items
itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)
print(f"Primeira-chave valor: {itens[0][0]} = {itens[0][1]}")