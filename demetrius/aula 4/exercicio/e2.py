import funcao

valores = [1000, 1500, 1250, 2500]
valores_imposto = [] 

for valor in valores:
    valores_imposto.append(funcao.imposto(valor))

print(valores_imposto)