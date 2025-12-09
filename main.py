import sys
from vigenere_classes import *  
"""
    Programa principal para cifrar y descifrar mensajes usando el cifrado Vigenere.
    uv run main.py <fichero_entrada> <clave> <modo>
    donde <fichero_entrada> es el fichero que contiene el mensaje a cifrar o descifrar,
    <clave> es la clave a usar para el cifrado/descifrado,
    y <modo> es 'true' para cifrar o 'false' para descifrar
"""

def readTxt(fichero):
    with open(fichero,'r') as f:
        lines = f.readlines()
    accum = [k[:-1] for k in lines]
    return ''.join(accum)


if __name__ == "__main__":

    T=readTxt(sys.argv[1])  #leemos el fichero de entrada
    if len(sys.argv) == 4:
        P=Encipher(T, sys.argv[2])  #creamos el objeto Encipher con el texto y la clave
        mode =bool(int(sys.argv[3]))  #convertimos el modo a booleano
        E=P.cipher(mode)  #ciframos o desciframos el mensaje
        print(E)
