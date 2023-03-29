import sys
from dados import funcoes as es

def main(instancia):
    matriz = es.matriz(instancia)
    es.resultado(instancia, matriz)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python programa.py <instancia>")
    else:
        instancia = sys.argv[1]
        main(instancia)