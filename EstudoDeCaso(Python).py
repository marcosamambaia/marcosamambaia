import time

estoque = {}

while True:
    print("\n \n ******************************  CONTROLE DE ESTOQUE  ********************************\n Escolha sua opção:\n \n (1) Adicionar produto    (2) Atualizar produto  (3) Excluir produto\n (4) Visualizar Estoque   (5) Sair do sistema \n \n************************************************************************************")
    
    Escolha_opcao = int(input("Digite a opcao desejada: "))

    if Escolha_opcao == 1:
        Nome_produto = input('Qual o nome do produto? ')
        Preco_Produto = float(input('Qual o valor do produto? '))
        Quantidade_Estoque = int(input('Qual a quantidade em estoque? '))
        # Adicionando o produto ao dicionário de estoque
        estoque[Nome_produto] = {'Preço': Preco_Produto, 'Quantidade': Quantidade_Estoque}
        print(f"Produto {Nome_produto} adicionado com sucesso.\n")
        time.sleep(2)

    elif Escolha_opcao == 2:
        Nome_produto = input('Qual o nome do produto que deseja atualizar? ')
        if Nome_produto in estoque:
            Preco_Produto = float(input('Qual o novo valor do produto? '))
            Quantidade_Estoque = int(input('Qual a quantidade atualizada em estoque? '))
            # Atualizando o produto no dicionário de estoque
            estoque[Nome_produto] = {'Preço': Preco_Produto, 'Quantidade': Quantidade_Estoque}
            print(f"Produto {Nome_produto} atualizado com sucesso.\n")
        else:
            print(f"O produto {Nome_produto} não existe no estoque.\n")
        time.sleep(2)

    elif Escolha_opcao == 3:
        Nome_produto = input('Qual produto deseja excluir? ')
        if Nome_produto in estoque:
            del estoque[Nome_produto]
            print(f"Produto {Nome_produto} excluído com sucesso.\n")
        else:
            print(f"O produto {Nome_produto} não existe no estoque.\n")
        time.sleep(2)

    elif Escolha_opcao == 4:
        print("Estoque Atual:")
        for produto, detalhes in estoque.items():
            print(f"Produto: {produto}, Preço: R$ {detalhes['Preço']}, Quantidade: {detalhes['Quantidade']}")
        print("\n")
        time.sleep(2)
        
        # Pausa para aguardar entrada do usuário antes de voltar ao menu inicial
        while True:
            sair = input('Deseja voltar à tela inicial? (S/N): ')
            if sair.lower() in ['s', 'n']:
                if sair.lower() == 's':
                    break
                else:
                    print("Opção inválida. Tente novamente.\n")
            time.sleep(2)
    
    elif Escolha_opcao == 5:
        print("Saindo do sistema...")
        time.sleep(2)
        break

    else:
        print("Opção inválida. Tente novamente.\n")
        time.sleep(2)
