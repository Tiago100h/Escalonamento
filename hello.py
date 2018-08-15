# Lendo arquivo
arquivo = open('arquivos/teste.txt', 'r')
linhas = arquivo.readlines()

maiorLinha = 0
for linha in linhas :
    elementos = linha.split(' ')
    if len(elementos) > maiorLinha :
        maiorLinha = len(elementos)

print(maiorLinha)

arquivo.close()