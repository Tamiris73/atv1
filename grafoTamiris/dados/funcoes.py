import igraph as ip
import numpy as np

def matriz(instancia):
    path = 'C:\Users\User\Downloads\grafoTamiris\grafoTamiris/Instancias/{}.txt'.format(instancia)
    with open(path, 'rb') as f:
        data = np.genfromtxt(f, dtype=np.int64)
    return data

def resultado(instancia, matriz):
    print('NOME DA INSTÂNCIA:', instancia)
    linhas, colunas = matriz.shape
    print("A matriz tem dimensões: {}x{}".format(linhas, colunas))
    path = 'C:\Users\User\Downloads\grafoTamiris\grafoTamiris/resultados.txt'
    with open(path, "a+") as arquivo:
        arquivo.write("{} {}\n".format(linhas, colunas))