#***********************************************************************************************************
#  
# Aluno: Marco Antonio Monteiro Pedro
# Data 19/12/2024
# Modulo 'Computational Logic Using Python'
#
#***********************************************************************************************************
#
# Foi usado função 'Try/Except' para evitar entrada irregular de usuario,
# evitando parar o programa por erro, tambem foi feita dentro de uma laço
# 'While True' para caso seja digitado a entrada errada o usuario pode repetir
# a tarefa .
# Codigo com comentarios explicando as linhas e funcionamentos para ajudar
# na correção e avaliação do professor:
#
#***********************************************************************************************************



# Importa a biblioteca time para usar a função sleep
import time  

# Lista que armazena o estoque de produtos
estoque = []

# Função para exibir o menu e obter a escolha do usuário
def menu():
    print("\n \n ******************************  CONTROLE DE ESTOQUE  ********************************\n Escolha sua opção:\n \n (1) Adicionar produto    (2) Atualizar produto  (3) Excluir produto\n (4) Visualizar Estoque   (5) Sair do sistema \n \n************************************************************************************")
    return int(input("Digite a opção desejada: "))  # Retorna a opção escolhida pelo usuário
      
# Função para adicionar um produto ao estoque
def adicionar_produto():
    while True:
        try:
            nome_produto = input('Qual o nome do produto? ')
            preco_produto = float(input('Qual o valor do produto? '))
            quantidade_estoque = int(input('Qual a quantidade em estoque? '))
            # Adiciona um dicionário com os detalhes do produto à lista de estoque
            estoque.append({'Nome': nome_produto, 'Preço': preco_produto, 'Quantidade': quantidade_estoque})
            print(f"Produto {nome_produto} adicionado com sucesso.\n")
            time.sleep(2)  # Pausa para exibir a mensagem por 2 segundos
            break  # Sai do loop se não houver exceção
        except ValueError:
            print('Entrada de usuário inválida. Por favor, cadastre novamente.')
            time.sleep(2)  # Pausa para exibir a mensagem por 2 segundos
   

# Função para atualizar os dados de um produto no estoque
def atualizar_produto():
    print("Estoque Atual:")
    contador = 1  # Inicializa o contador
    for produto in estoque:
        # Exibe cada produto com seu índice, nome, preço e quantidade
        print(f"{contador} -> Produto: {produto['Nome']}, Preço: R$ {produto['Preço']}, Quantidade: {produto['Quantidade']}")
        contador += 1  # Incrementa o contador
    print("\n")
    time.sleep(2)  # Pausa para exibir a mensagem por 2 segundos

    while True:
        try:
            indice = int(input('Digite o índice do produto que deseja atualizar: ')) - 1
            if 0 <= indice < len(estoque):  # Verifica se o índice é válido
                break
            else:
                print("Índice inválido. Tente novamente.\n")
        except ValueError:
            print("Entrada inválida! Por favor, digite o numero correto do produto.\n")

    while True:
        try:
            preco_produto = float(input('Qual o novo valor do produto? '))
            quantidade_estoque = int(input('Qual a quantidade atualizada em estoque? '))
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite valores numéricos válidos.\n")

    # Atualiza o preço e a quantidade do produto
    estoque[indice]['Preço'] = preco_produto
    estoque[indice]['Quantidade'] = quantidade_estoque
    print(f"Produto {estoque[indice]['Nome']} atualizado com sucesso.\n")
    time.sleep(2)  # Pausa para exibir a mensagem por 2 segundos


# Função para excluir um produto do estoque
def excluir_produto():
    print("Estoque Atual:")
    contador = 1  # Inicializa o contador
    for produto in estoque:
        # Exibe cada produto com seu índice, nome, preço e quantidade
        print(f"{contador} -> Produto: {produto['Nome']}, Preço: R$ {produto['Preço']}, Quantidade: {produto['Quantidade']}")
        contador += 1  # Incrementa o contador
    print("\n")
    time.sleep(2)  # Pausa para exibir a mensagem por 2 segundos

    while True:
        try:
            indice = int(input('Digite o índice do produto que deseja excluir: ')) - 1
            if 0 <= indice < len(estoque):  # Verifica se o índice é válido
                nome_produto = estoque[indice]['Nome']
                # Remove o produto do estoque
                del estoque[indice]
                print(f"Produto {nome_produto} excluído com sucesso.\n")
                break  # Sai do loop se o produto for excluído com sucesso
            else:
                print("Índice inválido. Tente novamente.\n")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número correto do produto.\n")
    time.sleep(2)  # Pausa para exibir a mensagem por 2 segundos


# Função para visualizar o estoque atual
def visualizar_estoque():
    print("Estoque Atual:")
    contador = 1  # Inicializa o contador
    for produto in estoque:
        # Exibe cada produto com seu índice, nome, preço e quantidade
        print(f"{contador} -> Produto: {produto['Nome']}, Preço: R$ {produto['Preço']}, Quantidade: {produto['Quantidade']}")
        contador += 1  # Incrementa o contador
    print("\n")
    time.sleep(2)  # Pausa para exibir a mensagem por 2 segundos
    while True:
        sair = input('Deseja voltar à tela inicial? (S/N): ')
        if sair.lower() == 's':
            break  # Sai do loop e volta ao menu principal
        elif sair.lower() == 'n':
            print("Opção inválida. Tente novamente.\n")
        time.sleep(2)  # Pausa para exibir a mensagem por 2 segundos

# Função para sair do sistema
def sair_do_sistema():
    print("Saindo do sistema...")
    time.sleep(2)  # Pausa para exibir a mensagem por 2 segundos
    exit()  # Encerra o programa

# Loop principal do programa
while True:
    try:
        escolha = menu()  # Exibe o menu e obtém a escolha do usuário
        if escolha == 1:
            adicionar_produto()
        elif escolha == 2:
            atualizar_produto()
        elif escolha == 3:
            excluir_produto()
        elif escolha == 4:
            visualizar_estoque()
        elif escolha == 5:
            sair_do_sistema()
        else:
            print("Opção inválida. Tente novamente.\n")
            time.sleep(2)  # Pausa para exibir a mensagem por 2 segundos
    except ValueError:
        print('Entrada de usuario invalida, digite apenas o numero da opção desejada!')
        time.sleep(2)  # Pausa para exibir a mensagem por 2 segundos
    