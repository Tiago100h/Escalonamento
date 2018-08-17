# Função para imprimir matriz
def ImprimirMatriz(matriz):
    i = 0
    j = 0
    while i < len(matriz):
        while j < len(matriz[i]):
            print(matriz[i][j], end=' ')
            j = j + 1
        print()
        i = i + 1
        j = 0
    print()

# Ler arquivo
arquivo = open('arquivos/teste.txt', 'r')
linhas = arquivo.readlines()
arquivo.close()

# Definir maior linha
maiorLinha = 0
for linha in linhas:
    elementos = linha.split(' ')
    if len(elementos) > maiorLinha:
        maiorLinha = len(elementos)

# Criar matriz com inteiros e zeros a esquerda
matriz = []
for linha in linhas:
    elementos = linha.split(' ')
    novaLinha = []
    i = len(elementos)
    while i < maiorLinha:
        novaLinha.append(0)
        i = i + 1
    for elemento in elementos:
        novaLinha.append(int(elemento.replace('\n', '')))
    matriz.append(novaLinha)

ImprimirMatriz(matriz)