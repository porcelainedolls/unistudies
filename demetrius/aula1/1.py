print("************ CALCULADORA FODA ************")
print("1 - somar")
print("2 - subtrair")
print("3 - multiplicar")
print("4 - dividir")
opcao = input("Escolha uma opção: ")
num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("Informe o segundo valor: "))

if opcao == "1":
    print(num1 + num2)
if opcao == "2":
    print(num1 - num2)
if opcao == "3":
    print(num1 * num2)
if opcao == "4":
    print(num1 / num2)
else:
    print("Erro na Operação")