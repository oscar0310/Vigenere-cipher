from itertools import chain   #lo usamos para concatenar listas
from vigenere_alphabet import *   # importamos todo de vigenere_alphabet.py

class Message:
    def _flatten(self,listOfLists):   #convierte una lista de listas en una sola lista
        return list(chain.from_iterable(listOfLists))
    
    def _rBlanks(self, strng):   #Elimina los espacios en blanco de un string y lo convierte a mayusculas
        return ''.join(strng.split()).upper()
    
    def _normalize(self, strng):   #normaliza el string: elimina espacios, convierte a mayusculas y reemplaza caracteres especiales
        s = self._rBlanks(strng)  #convertimos a mayusculas y eliminamos espacios
        accum = []
        for ch in s:
            if ch in alphSpecials:
                accum.append(alphSpecials[ch]) #reemplazamos caracteres especiales
            else:
                accum.append(ch)  #dejamos el caracter tal cual

        return list(filter(lambda x: x in alphabet, self._flatten(accum)))  #filtramos solo los caracteres que estan en el alfabeto
    
    def __init__(self, strng):  #constructor de la clase Message
        x=self._normalize(strng)  #normalizamos el string
        self.content = ''.join(x)  #unimos la lista de caracteres en un string
        self.length = len(self.content)  #longitud del mensaje

    def __str__(self):  # mensaje como string
        return self.content
    
