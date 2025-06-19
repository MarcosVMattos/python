# Declaração
minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# Listas (Mutável)
print("Minha lista de exemplo", minha_lista)

# Manejando a lista
minha_lista[0] = "python"
print("Minha lista de exemplo", minha_lista)
print("minha_lista[0]:", minha_lista[0])
print("minha_lista[6]:", minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7])
print("minha_lista[:6]:", minha_lista[:6])
print("minha_lista[2:]", minha_lista[2:])

# Métodos para adicionar ou mostrar índice: 
# Append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após .append(6)", minha_lista)

# Index(): Retorna o índice do elemento escolhido
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

# Insert(): Insere um elemento em um inidice específico, primeiro passa o indice que vc deseja depois o elemento
minha_lista.insert(2, 10)
print("Após o insert(2, 10):", minha_lista)

# Métodos para deletar:
# Pop
elemento_removido = minha_lista.pop(3)
print("Elemento removido:" , elemento_removido)
print("Após pop(3):", minha_lista)

# Remove
minha_lista.remove(True)
print("Após remove(True):", minha_lista)

print("Para funcionar o sort irei remover tudo aquilo que não seja int:")
minha_lista.remove("python")
minha_lista.remove("rocketseat")
minha_lista.remove(False)
print("Após remover python, rocketseat, False:", minha_lista)

# Método para organizar a lista
# Sort (Só pode ser usado se tiver só números na lista, se misturar str e int, boleanos não funciona!)
minha_lista.sort()
print("Após o sort():", minha_lista)