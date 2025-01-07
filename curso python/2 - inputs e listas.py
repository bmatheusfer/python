# inputs
email = input("Escreva seu e-mail: ")
nome = input("Seu primeiro nome: ")

print(nome, email)

print(f"{nome}, verifique seu email: {email} que enviamos um link de confirmação")

faturamento = float(input("Escreva o faturamento: ")) #sempre definir o tipo de dado que está sendo inputado
imposto = faturamento * 0.1
print(imposto) 

# listas 
vendas = [100, 50, 14, 20, 30, 700]

# soma dos elementos
total_vendas = sum(vendas)
print(total_vendas)

# tamanho da lista
quantidade_vendas = len(vendas)
print(quantidade_vendas)

# valores maximos e minimos
print(max(vendas))
print(min(vendas))

# pegar posição
print(vendas[0])

# procurar determinado produto na lista
lista_produtos = ["iphone", "airpod", "ipad", "macbook"]

produto_procurado = input("Pesquise pelo nome do produto: ")
produto_procurado = produto_procurado.lower()

print(produto_procurado in lista_produtos)

# adicionar item a lista
lista_produtos.append("apple watch")
print(lista_produtos)

# remover item da lista
lista_produtos.remove("apple watch")
print(lista_produtos)

lista_produtos.pop(1) # remove o indice 1 da lista

# editar um item da lista
precos = [1000, 1500, 3500]
precos[0] = 6000
print(precos)

# contar quantidade de item na lista
lista_produtos = ["iphone", "airpod", "ipad", "macbook", "iphone", "airpod", "ipad", "macbook", "iphone", "airpod", "ipad", "macbook"]
lista_produtos.count("iphone")

# ordenar uma lista
lista_produtos = ["iphone", "airpod", "ipad", "macbook", "iphone", "airpod", "ipad", "macbook", "iphone", "airpod", "ipad", "macbook"]
lista_produtos.sort() # pode passar parametro dentro do parentes