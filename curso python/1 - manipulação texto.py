faturamento = 1000
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento

print("O Lucro da emrpesa foi de",lucro)

print ("Faturamento da empresa: {}, Custo: {}, Lucro: {}".format(faturamento, custo, lucro))

print(f"Faturamento da empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}")

# manipulação de Texto

email_client = "qualquercoisa@gmail.com"

# maiscula
email_client = email_client.upper()
print(email_client)

# minuscula
email_client = email_client.lower()
print(email_client)

# encontrar um caracter no texto
print(email_client.find("@")) # =1 quando não encontrar

# tamanho do texto
print (len(email_client))

# pegar um caractere
print(email_client[0])

# pegar pedaço do texto
print(email_client[:4])

# substituir pedaço do texto
novo_email = email_client.replace("gmail.com", "hotmail.com")
print(novo_email)

# primeiras letras maisculas
nome = "matheus fernando"
print(nome.capitalize()) # primeira letra maiscula
print(nome.title()) # primeira letra de cada palavra maiscula

# pegar servidor do email
posicao_arroba = email_client.find("@") # +1 para não incluir o @
servidor = email_client[posicao_arroba:]
print(servidor)

# pegar 1º nome
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]
print(primeiro_nome)

# pegar sobrenome
sobrenome = nome[posicao_espaco+1:]
print(sobrenome)

# casos especiais - formatações numericas em texto
margem_lucro = round(margem_lucro, 2)
print(f"Faturamento da empresa: R${faturamento:.2f}, Custo: R${custo:.2f}, Lucro: R${lucro:.2f}, Margem: {margem_lucro:.0%}")
