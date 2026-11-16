def idade(nome, ano):
    tamanho = len(nome)
    idade = (2026 - ano)
    return(tamanho, idade)

def dolar(valor):
    conversao = valor * 5.09
    return conversao

def imposto(valor):
    return valor * 1.1