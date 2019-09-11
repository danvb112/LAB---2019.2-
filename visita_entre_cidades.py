# Exemplo de entrada:
#4 2 4
#1 2 10
#2 3 11
#3 4 12

#Exemplo de grafo:

# grafo = {
#          "1": {"2": 10},
#          "2": {"3": 11},
#          "3": {"4": 12} }

def adicionar_ao_grafo(P,Q,D):
    grafo = {}
    
    grafo[P] = []
    grafo[P].append((Q,D))
    
    print(grafo.items())
    print(grafo.keys())



print("""Digite 3 Valores sendo o primeiro:
            N: Para o número total de cidades
            A: Para a cidade de origem
            B: Para a cidade de destino\n""")

N, A, B = input("Digite os Valores aqui: ").split()

N = int(N)

print("""Agora digite mais 3 valores P,Q e D indicando indicando que:
existe uma estrada ligando diretamente as cidades P e Q, com distância D.\n""")

for x in range(N-1):
    P, Q, D = input("Digite os valores aqui:").split()

    adicionar_ao_grafo(P,Q,D)


