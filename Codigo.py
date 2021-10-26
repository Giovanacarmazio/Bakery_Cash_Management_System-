import operacoes as op


opcao_selecionada = None
valor_total = 0

while True:
    if opcao_selecionada == None:
        opcao_selecionada = int(input("""Selecione a operação desejada:
                                        0- ADICIONAR ITEM
                                        1- RETIRAR ITEM
                                        2- CONSULTAR TOTAL
                                        3- PAGAMENTO
                                        """))
    elif opcao_selecionada not in range(4):
        print("Opção inválida, tente novamente")
        opcao_selecionada = None
    elif opcao_selecionada == 0:
        nome_item = input("Insira o nome do item")
        valor_unitario = float(input("Insira o valor unitario"))
        quantidade = int(input("Insira a quantidade"))
        valor_total = op.adicionar_item(nome_item,valor_unitario,quantidade, valor_total)
        print(f"O item {nome_item} foi adicionado com sucesso!")
        opcao_selecionada = None
    elif opcao_selecionada == 1:
        nome_item = input("Insira o nome do item")
        valor_unitario = float(input("Insira o valor unitario"))
        quantidade = int(input("Insira a quantidade"))
        resultado = op.retirar_item(nome_item, valor_unitario, quantidade, valor_total)
        if resultado == "error!":
            print(f"Valor inválido, não pode ser menor que {valor_total}")
            opcao_selecionada == None
        else:
            valor_total = resultado
            print(f"O item {nome_item} foi retirado com sucesso!")
        opcao_selecionada = None
    elif opcao_selecionada == 2:
        print(op.consultar_total(valor_total))
        opcao_selecionada = None
    elif opcao_selecionada == 3:
        forma_pagamento = int(input("Qual a forma de pagamento? (0 - Dinheiro) (1 - Cartão)"))
        print(op.pagamento(valor_total,forma_pagamento))
        opcao_selecionada = None
