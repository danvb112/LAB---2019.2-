
def grafo():
    n,inicio,fim = map(lambda i: int(i), input().split(' '))
    grafo = [[] for a in range(n)]
    for a in range(n-1):
        c1,c2,d = map(lambda i: int(i), input().split(' '))
        grafo[c1-1].append((c2-1,d))
        grafo[c2-1].append((c1-1,d))

    calcular_distancia(grafo, inicio-1, fim-1)

def calcular_distancia(grafo, vertice_atual ,B):
    visitados = []
    for a in range(len(grafo)):
        visitados.append(0)
    visitados[vertice_atual] = 1
    Lista_dos_vizinhos = []
    for vizinhos in grafo[vertice_atual]:
        visitados[vizinhos[0]] = 1
        Lista_dos_vizinhos.append(vizinhos)
    vertice_atual = Lista_dos_vizinhos.pop(0)
    while vertice_atual[0] != B:
        for i in grafo[vertice_atual[0]]:
            if visitados[i[0]] == 0:
                visitados[i[0]] = 1
                distancia_total = (i[0], i[1] + vertice_atual[1])
                Lista_dos_vizinhos.append(distancia_total)
        vertice_atual = Lista_dos_vizinhos.pop(0)
    return print(vertice_atual[1])

grafo()





