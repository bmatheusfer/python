# if condicao/comparacao:
    # tudo o que acontece se a condicao for verdadeira
# else:
    # tudo o que acontece se a condicao for falsa

vendas = 1500
meta = 1300

# > maior que
# < menor que
# >= maior ou igual
# <= menor ou igual
# == igual
# != diferente

if vendas > meta:
    print("Vendedor ganha bonus")
    bonus = 0.1 * vendas
    print("Bonus do vendedor:", bonus)
else:
    print("Vendedor não ganha bonus")

# 2º cenario
vendas = 1500
vendas_empresa = 10000
meta_empresa = 20000
meta1 = 1300 # ganha 10%
meta2 = 2000 # ganha 13%

if vendas >= 2000:
    bonus = 0.13 * vendas
else:
    if vendas >= 1300:
        bonus = 0.1 * vendas
    else:
        bonus = 0

if vendas >= 2000 or vendas_empresa >= meta_empresa:
    bonus = 0.13 * vendas
elif vendas >= 1300 and vendas_empresa >= meta_empresa:
    bonus = 0.1 * vendas
else:
    bonus = 0

print("Bonus:", bonus)

# listas com condições
lista_produtos = ["iphone", "airpod", "ipad", "macbook"]
produto_procurado = input("Procure um produto: ")
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
    print("Produto no estoque")
else:
    print("Não temos esse produto")