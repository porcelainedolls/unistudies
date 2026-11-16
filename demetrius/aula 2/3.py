valor = int(input("Valor: "))

for i in range(valor + 1):
    for j in range(i):
        print(j, end=" ")
    print(i)