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
  elif opcao == "6":
    print("\nPrograma Finalizado")
    break