import funcao

print("************* LOJA PICA *************")
print("************* PRODUTOS *************")
print("1 - notebook (750 USD)")
print("2 - smartwatch (250 USD)")
produto = int(input("Selecione o produto"))

if produto == 1:
    conversao = funcao.dolar(750)
    print(f"Valor convertido: R$ {conversao}")
elif produto == 2:
    conversao = funcao.dolar(250)
    print(f"valor convertido: R$ {conversao}")
else:
    print("produto invalido")

print("************* Frete *************")
print("1 - BRASIL (52 USD)")
print("2 - ARGENTINA (75 USD)")
frete = int(input("Selecione o país de destino: "))

if frete == 1:
    frete_conv = funcao.dolar(52)
    print(f"valor de frete é: R$ {frete_conv} carai q pais merda da porra")
elif frete == 2:
    frete_conv = funcao.dolar(75)
    print(f"valor de frete é: R$ {frete_conv}")
else:
    print("Destino Inválido")

valortotal = conversao + frete_conv
print(f"O valor total da sua compra é: R$ {valortotal}")
