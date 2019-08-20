comandos = list(input("Digite a sequência de comandos aqui: "))
lista_F = []
lista_T = []

for e in comandos:
    if e == "F":
        lista_F.append(e)
    else:
        lista_T.append(e)

posicao = len(lista_F) - len(lista_T)

print(posicao)


