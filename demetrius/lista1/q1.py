import math

print("************* Calculadora de bhaskara *************")
a = int(input("Insira o valor de A da sua equação: "))
b = int(input("Insira o valor de B da sua equação: "))
c = int(input("Insira o valor de C da sua equação: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("A sua equação não possui raizes reais")
elif delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a) 
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")