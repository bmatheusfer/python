lista_precos = [1500, 1000, 800, 3000]

# imposto
# aliquota1 - IR = 0.2, se o preço do produto for maior que 2000 então será 0.5
# aliquota2 - ISS = 0.15
# aliquota3 - CSLL = 0.05

for preco in lista_precos:
    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_iss = 0.15 * preco
        imposto_csll = 0.05 * preco
        imposto_total = imposto_ir + imposto_csll + imposto_iss
print(f"Imposto total sobre os produtos de R${preco}: R${imposto_total}")

# criar função para calcular o importo total
def calcula_imposto_total(preco):
    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco
    imposto_iss = 0.15 * preco
    impostocsll = 0.05 * preco
    imposto_total = imposto_ir + imposto_iss + impostocsll
    return imposto_total

for preco in lista_precos:
    imposto_total = calcula_imposto_total(preco)
    print(f"Imposto total sobre os produtos de R${preco}: R${imposto_total}")

nova_lista_produtos = [3000, 5000, 6000, 7000]

for preco in nova_lista_produtos:
    imposto_total = calcula_imposto_total(preco)
    print(f"Imposto total sobre os produtos de R${preco}: R${imposto_total}")