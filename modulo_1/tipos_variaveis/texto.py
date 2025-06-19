# Declaração
nome_completo = "Marcos Mattos"
#Dessa maneira, mesmo que escreva o primeiro nome na primeira linha e o segundo nome na segunda linha eles serão mostrados na mesma linha.

nome_completo_aspas = """Marcos
Mattos"""
#Com as 3 aspas antes e depois podemos quebrar linhas.(Podem ser aspas duplas ou simples, o importante é ter 3 antes e 3 depois)

nome_completo_quebra = "Marcos \
Mattos"
#Mesmo resultado do nome_completo

nome = "Marcos"
sobrenome = "Mattos"

#Formatação
print("Nome completo", nome_completo) #1a forma
print("Nome completo" + nome_completo) #2a forma
print("Nome completo %s" % nome_completo) #3a forma
print("Nome completo %s %s" % (nome, sobrenome)) #4a forma
print(f"Nome completo {nome} {sobrenome}") #5a forma

print(nome_completo.replace("M", "p"))