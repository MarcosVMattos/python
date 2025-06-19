def adicionar_contato(agenda, nome, telefone, email=""):
    conteudo_agenda = {"Nome" : " ", "Telefone" : " ", "email" : " ", "favoritado" : False}
    conteudo_agenda["Nome"] = nome
    conteudo_agenda["Telefone"] = telefone
    conteudo_agenda["email"] = email
    agenda.append(conteudo_agenda)
    return

def visualizar_contatos(agenda):
    if len(agenda) == 0:
        print("\nAgenda vazia")
        return
    
    for indice, contato in enumerate(agenda):
        if contato["favoritado"]:
            print(f"{indice+1}. Nome: {contato["Nome"]} | Telefone: {contato["Telefone"]} | E-mail: {contato["email"]} | Favoritado: [✓]")
        else:
            print(f"{indice+1}. Nome: {contato["Nome"]} | Telefone: {contato["Telefone"]} | E-mail: {contato["email"]}")

def editar_contatos(agenda, indice, novo_nome):
    indice_ajustado = indice - 1
    if indice_ajustado >= 0 and indice_ajustado < len(agenda):
        agenda[indice_ajustado]["Nome"] = novo_nome
        print(f"Contato atualizado para {novo_nome}")
    else:
        print("Índice inválido")
    return

def editar_numero(agenda, indice, novo_numero):
    indice_ajustado = indice - 1
    if indice_ajustado >= 0 and indice_ajustado < len(agenda):
        agenda[indice_ajustado]["Telefone"] = novo_numero
        print(f"Telefone atualizado")
    else:
        print("Índice inválido")
    return

def favoritar(agenda):
    escolha = int(input("\nQual contato deseja favoritar? "))
    indice_ajustado = escolha - 1
    agenda[indice_ajustado]["favoritado"] = True
    print("Contato favoritado")
    return

def contatos_favoritados(agenda):
    print("\nContatos favoritados:")
    encontrados = False
    for indice, contato in enumerate(agenda):
        if contato["favoritado"] == True:
            print(f"{indice+1}. Nome: {contato['Nome']} | Telefone: {contato['Telefone']} | E-mail: {contato['email']} | Favoritado: [✓]")
            encontrados = True
    if not encontrados:
        print("Nenhum contato favoritado.")
    return

def excluir_contato(agenda, indice):
    indice_ajustado = indice - 1
    excluir = agenda.pop(indice_ajustado)
    print("Contato excluído")
    return

agenda = []

while True:
    print("\n1. Adicionar contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar nome do contato")
    print("4. Editar número do contato")
    print("5. Favoritar contato")
    print("6. Contatos favoritados")
    print("7. Excluir contato")
    print("8. Sair")
    
    escolha = int(input("\nSelecione a opção desejada: "))

    if escolha == 1:
        nome = str(input("Nome: "))
        telefone = input("Telefone: ")
        email = input("E-mail (Opcional): ")
        adicionar_contato(agenda, nome, telefone, email)

    elif escolha == 2:
        visualizar_contatos(agenda)

    elif escolha == 3:
        visualizar_contatos(agenda)
        indice = int(input("Selecione o contato que deseja editar: "))
        novo_nome = input("Digite o novo nome: ")
        editar_contatos(agenda, indice, novo_nome)

    elif escolha == 4:
        visualizar_contatos(agenda)
        indice = int(input("Selecione o contato que deseja editar: "))
        novo_numero = input("Novo número: ")
        editar_numero(agenda, indice, novo_numero)

    elif escolha == 5:
        visualizar_contatos(agenda)
        favoritar(agenda)
    
    elif escolha == 6:
        contatos_favoritados(agenda)

    elif escolha == 7:
        visualizar_contatos(agenda)
        indice = int(input("Qual contato deseja excluir? "))
        excluir_contato(agenda, indice)

    elif escolha == 8:
        break
