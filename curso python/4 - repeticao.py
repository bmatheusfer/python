lista_vendas = [1500, 800, 800, 1500, 2000, 2300]

meta = 1200
percentual_bonus = 0.1

for venda in lista_vendas:
    if venda >= meta:
        bonus = percentual_bonus * venda
    else:
        bonus = 0

    print(bonus)        

# lista de repetição
for i in range(10):
    print("Lista de repeticao")

# printa os itens da lista_vendas
for item in lista_vendas:
    print(item)

# fora do for

