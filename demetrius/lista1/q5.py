print("********** organizador de numeros **********")
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

numeros = [numero1, numero2, numero3]
numeros.sort()

print("Numeros em ordem crescente:", numeros)