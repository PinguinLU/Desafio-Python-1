def adicionar_contato(contatos):
    nome = input("Digite o nome do contato que deseja adicionar: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")
  
    contato = {
     "nome": nome,
     "email": email,
     "telefone": telefone
    }
    
    contatos.append(contato)
    print(f"\nContato adicionado com sucesso:\n \n{nome} \n{email} \n{telefone}\n")

def ver_contatos(contatos):
    if not contatos:
        print("Nenhum contato salvo.")
        return
  
    print("\nLista de Contatos:")
    for indice, contato in enumerate(contatos, start=1):
         print(f"{indice}. {contato['nome']} - {contato['email']} - {contato['telefone']}")

def editar_contato(contatos):
    if not contatos:
        print("Nenhum contato salvo para editar.")
        return
  
    ver_contatos(contatos)
    indice = int(input("Digite o número do contato que deseja editar: ")) - 1
  
    if 0 <= indice < len(contatos):
        nome = input("Digite o novo nome (deixe em branco para manter o atual): ")
        email = input("Digite o novo email (deixe em branco para manter o atual): ")
        telefone = input("Digite o novo telefone (deixe em branco para manter o atual): ")
  
        if nome:
            contatos[indice]['nome'] = nome
        if email:
            contatos[indice]['email'] = email
        if telefone:
            contatos[indice]['telefone'] = telefone
  
        print("\nContato editado com sucesso.\n")
    else:
        print("Índice inválido. Tente novamente.")

def remover_contato(contatos):
    if not contatos:
        print("Nenhum contato salvo para remover.")
        return
  
    ver_contatos(contatos)
    indice = int(input("Digite o número do contato que deseja remover: ")) - 1
  
    if 0 <= indice < len(contatos):
        contato_removido = contatos.pop(indice)
        print(f"\nContato removido com sucesso: {contato_removido['nome']}\n")
    else:
        print("Índice inválido. Tente novamente.")
contatos = []
  
while True:
  print("-------------------------------------")
  print("\nAgenda-Lista de Contatos\n")
  print("-------------------------------------")
  print("1.Adicionar contato")
  print("2.Ver Contatos")
  print("3.Editar Contato")
  print("4.Remover Contatos")
  print("5.Favoritar Contatos")
  print("6.Encerrar programa")
  print("-------------------------------------")
  
  opcao = str(input("\nDigite uma opção: "))
  
  if opcao =="1":
    adicionar_contato(contatos)
  elif opcao =="2":
    ver_contatos(contatos)
  elif opcao =="3":
    editar_contato(contatos)  
  elif opcao =="4":
    remover_contato(contatos)
  elif opcao == "6":
    print("\nPrograma Finalizado")
    break