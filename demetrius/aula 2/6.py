lista = []

lista.append("lenovo")
lista.append("Acer")
lista.append("Samsung")
lista.append("Asus")
lista.append("Dell")
lista.pop(3)
lista.append("Positivo")
lista.insert(2, "Apple")
print(lista)

for i in range(len(lista)):
    print(lista[i])