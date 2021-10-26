import operacoes_bonus as op

itens={}
valor_total=0.0
opcao_selecionada = None

while True:
    if opcao_selecionada == None:
        print(""" 
__________________
MENU:
0- ADICIONAR ITEM
1- RETIRAR ITEM
2- CONSULTAR ITENS
3- CONSULTAR TOTAL
4- PAGAMENTO
__________________
""")
        try:
            opcao_selecionada = int(input("Selecione a operação desejada:"))
        except ValueError as err:
            print("Por favor, insira um número")
            opcao_selecionada = None
    elif opcao_selecionada not in range(5):
        print("Opção inválida, tente novamente")
        opcao_selecionada = None
    elif opcao_selecionada == 0:
        print("Opção selecionada: Adicionar Item")
        nome_item = input("Insira o nome do item")
        quantidade = int(input("Insira a quantidade"))
        try:
            itens, valor_total = op.adicionar_item(nome_item,quantidade, valor_total, itens)
        except Exception as err:
            print(err)
            opcao_selecionada = None
        else:
            print(f"O item {nome_item} foi adicionado com sucesso!")
            opcao_selecionada = None
    elif opcao_selecionada == 1:
        nome_item = input("Insira o nome do item")
        quantidade = int(input("Insira a quantidade"))
        try:
            itens, valor_total = op.retirar_item(nome_item, quantidade, valor_total, itens)
        except Exception as err:
            print(err)
            opcao_selecionada = None
        else:
            print(f"Foi retirado {quantidade} unidade(s) do item {nome_item}  com sucesso!")
        opcao_selecionada = None
    elif opcao_selecionada == 2:
        op.consultar_itens()
        opcao_selecionada = None
    elif opcao_selecionada == 3:
        op.consultar_total(valor_total,itens)
        opcao_selecionada = None
    elif opcao_selecionada == 4:
        forma_pagamento = int(input("Qual a forma de pagamento? (0 - Dinheiro) (1 - Cartão)"))
        try:
            itens, valor_total = op.pagamento(valor_total,forma_pagamento)
        except Exception as err:
            print(err)
            opcao_selecionada = None
        else:
            print("pagamento Realizado!")
        opcao_selecionada = None
    
