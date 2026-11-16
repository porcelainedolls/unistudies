print("calculadora de media")
nota1 = float(input("Insira sua nota do primeiro trimestre: "))
nota2 = float(input("Insira sua nota do segundo trimestre: "))
nota3 = float(input("Insira sua nota do terceiro trimestre: "))
nota4 = float(input("Insira sua nota do quatro trimestre: "))
freq = int(input("Insira o numero de suas faltas neste ano: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
freqresultado = 240 - freq
freqresultadocento = (freqresultado / 240) * 100

if freqresultadocento >= 75:
    if media >= 7:
        print("sua media é:", media, "e sua frequência é", freqresultadocento, "ta aprovado neguin")
    elif media <7 and media >= 4:
        print("sua média é:", media, " e sua frequência é", freqresultadocento, "ta na final doido kkk")
    else:
        print("Reprovado por nota kkkkk mt burro")

if media >= 7:
    if freqresultadocento >= 75:
        print("sua media é:", media, "e sua frequência é", freqresultadocento, "ta aprovado viado")
    else:
        print("Reprovou por falta kkkkk carai")