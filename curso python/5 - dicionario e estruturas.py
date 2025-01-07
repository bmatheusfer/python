lista_produtos = ["airpid", "ipad", "iphone", "macbook"]
precos = [2000, 9000, 6000, 11000]

dic_produtos = {
    "airpod": 2000,
    "ipad": 9000,
    "iphone": 6000,
    "macbook": 11000
}

# pegar um elemento
print(dic_produtos["iphone"])

# editar um elemento
dic_produtos["iphone"] = dic_produtos["iphone"] * 1.3
print(dic_produtos["iphone"])

# quantidade de itens
print(len(dic_produtos))

# remover item da lista
dic_produtos.pop("airpod")
print(dic_produtos)

# adicionar item a lista
dic_produtos["apple watch"] = 2500
print(dic_produtos)

# verificar se item existe no dicionario
if "iphone" in dic_produtos:
    print("Produto encontrado")
else:
    print("Não encontrado")

#verificar de um valor existe no dicionario
if 9000 in dic_produtos.values():
    print("Valor encontrado")
else:
    print("Valor não encontrado")

# exercicio 1 - cadastro produto com nome e preço
dic_produtos = {
    "airpod": 2000,
    "ipad": 9000,
    "iphone": 6000,
    "macbook": 11000
}
nome_produto = input("Nome do produto: ")
preco_produto = input("Preço do produto: ")
nome_produto = nome_produto.lower()
preco_produto = float(preco_produto)

dic_produtos[nome_produto] = preco_produto
print(dic_produtos)

#exercicio 2 - atualizar o preço de todos os produtos em +10%
dic_produtos = {
    "airpod": 2000,
    "ipad": 9000,
    "iphone": 6000,
    "macbook": 11000
}

for produto in dic_produtos:
    novo_preco = dic_produtos[produto] * 1.1
    dic_produtos[produto] = novo_preco

print(dic_produtos)
