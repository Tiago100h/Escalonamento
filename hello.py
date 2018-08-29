nomeArquivoEntrada = 'arquivos/teste1.txt'
nomeArquivoSaida = 'saida.txt'

def ImprimirMatriz(matriz):
    i = 0
    j = 0
    with open(nomeArquivoSaida, 'a') as saida:
        while i < len(matriz):
            while j < len(matriz[i]):
                saida.write(str(matriz[i][j]))
                saida.write('\t')
                j = j + 1
            saida.write('\n')
            i = i + 1
            j = 0
        saida.write('\n')

def ElementoIgualX(matriz, linha, coluna, x):
    return matriz[linha][coluna] == x

def IndiceElementoXAbaixoPivo(matriz, indice, x):
    i = indice + 1
    while i < len(matriz):
        if matriz[i][indice] == x:
            return i
        i = i + 1
    return -1

def IndiceElementoXAbaixoLinha(matriz, indiceLinha, indicePivo, x):
    i = indiceLinha
    while i < len(matriz):
        if matriz[i][indicePivo] == x:
            return i
        i = i + 1
    return -1

def IndiceElementoMenosUmAcima(matriz, indice):
    i = indice - 1
    while i > 0:
        if matriz[i][indice] == -1:
            return i
        i = i - 1
    return -1

def TrocarLinha(matriz, menorIndice, maiorIndice):
    with open(nomeArquivoSaida, 'a') as saida:
        saida.write('Trocando linhas ' + str(menorIndice) + ' e ' + str(maiorIndice) + ':')
        saida.write('\n')
    auxMenorIndice = matriz[menorIndice].copy()
    auxMaiorIndice = matriz[maiorIndice].copy()
    matriz[menorIndice].append('marcador')
    matriz[maiorIndice].append('marcador')
    removerMenorIndice = matriz[menorIndice]
    removerMaiorIndice = matriz[maiorIndice]
    matriz.insert(menorIndice, auxMaiorIndice)
    matriz.remove(removerMaiorIndice)
    matriz.insert(maiorIndice, auxMenorIndice)
    matriz.remove(removerMenorIndice)
    ImprimirMatriz(matriz)

def SomarLinha(matriz, linhaPivo, linha):
    with open(nomeArquivoSaida, 'a') as saida:
        saida.write('Linha ' + str(linha) + ' = linha ' + str(linha) + ' + linha ' + str(linhaPivo) + ':')
        saida.write('\n')
    i = 0
    while i < len(matriz[linha]):
        matriz[linha][i] = matriz[linha][i] + matriz[linhaPivo][i]
        i = i + 1
    ImprimirMatriz(matriz)

def NegarLinha(matriz, linha):
    with open(nomeArquivoSaida, 'a') as saida:
        saida.write('Multiplicando linha ' + str(linha) + ' por -1:')
        saida.write('\n')
    i = 0
    while i < len(matriz[linha]):
        if not matriz[linha][i] == 0.0:
            matriz[linha][i] = matriz[linha][i] * -1
        i = i + 1
    ImprimirMatriz(matriz)

def DividirLinha(matriz, linha):
    divisor = matriz[linha][linha]
    with open(nomeArquivoSaida, 'a') as saida:
        saida.write('Dividindo linha ' + str(linha) + ' por ' + str(divisor) + ':')
        saida.write('\n')
    i = 0
    while i < len(matriz[linha]):
        dividendo = matriz[linha][i]
        if not dividendo == 0.0:
            matriz[linha][i] = dividendo / divisor
        i = i + 1
    ImprimirMatriz(matriz)

def MultiplicarSomar(matriz, elemento, linhaPivo, linhaElemento):
    with open(nomeArquivoSaida, 'a') as saida:
        saida.write('Linha ' + str(linhaElemento) + ' = (linha ' + str(linhaPivo) + ' * ' + str(-1 * elemento) + ') + linha ' + str(linhaElemento) + ':')
        saida.write('\n')
    i = linhaPivo
    while i < len(matriz[linhaPivo]):
        matriz[linhaElemento][i] = matriz[linhaPivo][i] * -1 * elemento + matriz[linhaElemento][i]
        i = i + 1
    ImprimirMatriz(matriz)

# Ler arquivo
arquivo = open(nomeArquivoEntrada, 'r')
linhas = arquivo.readlines()
arquivo.close()

# Inicializar arquivo de saída
with open(nomeArquivoSaida, 'w') as saida:
    saida.write('Início\n')

# Definir maior linha
maiorLinha = 0
for linha in linhas:
    elementos = linha.split(' ')
    if len(elementos) > maiorLinha:
        maiorLinha = len(elementos)

# Criar matriz com numéricos e zeros a esquerda
matriz = []
for linha in linhas:
    elementos = linha.split(' ')
    novaLinha = []
    i = len(elementos)
    while i < maiorLinha:
        novaLinha.append(0)
        i = i + 1
    for elemento in elementos:
        novaLinha.append(float(elemento.replace('\n', '')))
    matriz.append(novaLinha)
ImprimirMatriz(matriz)

indicePivo = 0
while indicePivo < len(matriz):
    # Igualar pivô a 1
    if not ElementoIgualX(matriz, indicePivo, indicePivo, 1):
        indiceAux = IndiceElementoXAbaixoPivo(matriz, indicePivo, 1)
        if not indiceAux == -1:
            TrocarLinha(matriz, indicePivo, indiceAux)
        else:
            indiceAux = IndiceElementoXAbaixoPivo(matriz, indicePivo, -1)
            if not indiceAux == -1:
                TrocarLinha(matriz, indicePivo, indiceAux)
                NegarLinha(matriz, indicePivo)
            else:
                DividirLinha(matriz, indicePivo)

    # Zerar linhas abaixo do pivô
    indiceLinha = indicePivo + 1
    while indiceLinha < len(matriz):
        if not ElementoIgualX(matriz, indiceLinha, indicePivo, 0):
            indiceAux = IndiceElementoXAbaixoLinha(matriz, indiceLinha, indicePivo, 0)
            if not indiceAux == -1:
                TrocarLinha(matriz, indiceLinha, indiceAux)
            else:
                indiceAux = IndiceElementoXAbaixoLinha(matriz, indiceLinha, indicePivo, -1 * matriz[indiceLinha][indicePivo])
                if not indiceAux == -1:
                    SomarLinha(matriz, indicePivo, indiceLinha)
                else:
                    MultiplicarSomar(matriz, matriz[indiceLinha][indicePivo], indicePivo, indiceLinha)
        indiceLinha = indiceLinha + 1

    indicePivo = indicePivo + 1

indicePivo = indicePivo - 1
while indicePivo > -1:
    # Zerar elementos acima pivo
    indiceLinha = indicePivo - 1
    while indiceLinha > -1:
        indiceAux = IndiceElementoMenosUmAcima(matriz, indicePivo)
        if not indiceAux == -1:
            SomarLinha(matriz, indicePivo, indiceLinha)
        else:
            MultiplicarSomar(matriz, matriz[indiceLinha][indicePivo], indicePivo, indiceLinha)
        indiceLinha = indiceLinha - 1

    indicePivo = indicePivo - 1