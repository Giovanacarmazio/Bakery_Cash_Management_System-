#Criei um sistema de uma clinica veterinaria em JAVA, e confesso que esse em PYTHON foi um desafio mesmo rsrs não achei uma melhor forma de fazer
#sem um milhão de loopins for a menos a sua

opcao_selecionada = None
valor_total = 0

while True:
    if opcao_selecionada == None:
        opcao_selecionada = int(input("""Selecione a operação desejada:
                                        0- ADICIONAR ITEM
                                        1- RETIRAR ITEM
                                        2- CONSULTAR TOTAL
                                        3- PAGAMENTO
                                        4- DESLIGAR
                                        """))
    elif opcao_selecionada not in range(5):
        print("Opção inválida, tente novamente")
        opcao_selecionada = None
    elif opcao_selecionada == 0:
        nome_item = input("Insira o nome do item")
        valor_unitario = float(input("Insira o valor unitario"))
        quantidade = int(input("Insira a quantidade"))
        total_item = valor_unitario*quantidade
        valor_total = valor_total + total_item
        print(f"O item {nome_item} foi adicionado com sucesso!")
        opcao_selecionada = None
    elif opcao_selecionada == 1:
        nome_item = input("Insira o nome do item")
        valor_unitario = float(input("Insira o valor unitario"))
        quantidade = int(input("Insira a quantidade"))
        total_item = valor_unitario*quantidade
        resultado = valor_total - total_item
        if resultado < 0:
            print(f"Valor inválido, não pode ser menor que {valor_total}")
            opcao_selecionada == None
        else:
            valor_total = resultado
            print(f"O item {nome_item} foi retirado com sucesso!")
        opcao_selecionada = None
    elif opcao_selecionada == 2:
        print(f"O total é de: R${valor_total}")
        opcao_selecionada = None
    elif opcao_selecionada == 3:
        forma_pagamento = int(input("Qual a forma de pagamento? (0 - Dinheiro) (1 - Cartão)"))
        if forma_pagamento == 0:
            valor_total = valor_total*0.9
            pagamento = float(input("Qual o valor do pagamento?"))
            troco = pagamento - valor_total
            if troco < 0:
                print(f"O pagamento deve ser maior que o valor total!")
                opcao_selecionada = None
            else:
                print(f"Pagamento realizado! O troco é de {troco}")
        elif forma_pagamento == 1:
            print(f"Pagamento realizado!")
        else:
            print(f"Opção inválida!")
        opcao_selecionada = None 
    elif opcao_selecionada == 4:
        break
