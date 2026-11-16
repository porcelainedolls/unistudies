notas = {
    "carlos": 7.0,
    "alex": 8.5,
    "ana": 5.0,
    "lais": 10.0
}

soma = 0

for nota in notas.values():
    soma = soma + nota

media = soma / len(notas)

print(f"A media da turma é: {media}")