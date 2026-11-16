import math

print("************* Calculador de area *************")
raio = float(input("informe o raio da circunferência desejada: "))

pi = math.pi
areacirc = pi * raio**2

if raio <= 0:
    print("Verifique se o raio inserido está correto")
else:
    print(f"a sua Area é: {areacirc:.2f}")