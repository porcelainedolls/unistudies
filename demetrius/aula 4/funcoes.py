def somar(num1, num2):
    soma = num1 + num2
    return soma

def caralho(nome):
    print(f"caralho, {nome} tu é um filho da puta")

def linguagem(tipo = "Java"):
    print(f"voce está usando {tipo}")

def alunos(*nomes):
    for nome in nomes:
        print(f"Olá {nome}")

