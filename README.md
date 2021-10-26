# Software de Gestão de Caixa para uma Padaria

Neste exercício iremos construir um software de gestão de caixa para a padaria,  utilizando módulos. Crie um módulo de operações, este móludo deve conter o seguinte dicionário:

* valores_unitarios = {"pao": 2, "presunto": 10, "queijo": 15, "cafe":5}<br />

Este dicionário funcionará como nosso "banco de dados" dos produtos disponíveis. Ele representa o nome do item e o valor unitário. Só podem ser adicionados na compra os produtos deste dicionário. Também não será mais necessário pedir o valor unitário, uma vez que eles estão armazenados neste dicionário. Ao adicionar um item, o mesmo deve ser gravado em um outro dicionário contento o nome do item e a quantidade comprada. Pode-se retirar itens da compra até zerar a quantidade, caso a quantidade seja zerada, o item deve ser deletado do dicionário das compras. Deve-se tratar os erros com TRY/EXCEPT. O menu deve conter as seguintes opções:

0- Adicionar Item - Adiciona o item na compra
1- Retirar Item - Retira unidades/item da compra
2- Consultar Itens - Consulta os itens disponíveis para compra.
3- Consulta Total - Consulta um extrato da compra atual, exemplo de retorno:

| Opções  | Forma de Pagamento |
| ------------- |:-------------:|
| Opção 1     | Dinheiro     |
| Opção 2     | Cartão     |


| Item  | Valor Unit | Quantidade |
| ------------- |:-------------:|:-------------:|
| queijo    | 1     | R$ 15     |
| presunto    | 5    | R$ 10      |


4- Pagamento - No caso de dinheiro um desconto de 10% deverá ser adicionado no valor total e deve-se calcular o troco de acordo com o valor pago. Ao final do pagamento, deve-se zerar o dicionário de compra e o valor total para uma nova compra.

