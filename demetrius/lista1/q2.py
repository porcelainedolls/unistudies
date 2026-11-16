import time

print("Coleta de dados completamente moral e que não será vendida para a china")

nome = input("Seu nome: ")
idade = int(input("Quantos anos você têm: "))
genero = input("Seu Genero (M/F): ")
anoatual = time.localtime().tm_year
anonasc = anoatual - idade

if idade < 1:
    print("Verifique se sua idade foi inserida corretamente")
else:
    print(f"Você nasceu em {anonasc}")