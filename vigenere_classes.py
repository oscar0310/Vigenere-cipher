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
    
class Encipher(Message):
    
    def __init__(self, text, key): #constructor de la clase Encipher recibe el texto y la clave
        super().__init__(text)  #llamamos al contructor de Message para normalizar el texto
        self.key = ''.join(self._normalize(key))  #normalizamos la clave usando el metodo heredado de Message y lo unios en un solo string por si tuviera varias palabras la clave
        self.key_indices=[chNum[k] for k in self.key] #convertimos la clave a indices usando el diccionario chNum

    def cipher(self, mode=True): #Método para cifrar o descifrar el mensaje, mode=True para cifrar, False para descifrar

        textcod = [] #almacenamos el texto cifrado o descifrado
        key_length = len(self.key_indices)  #longitud de la clave

        for i, char in enumerate(self.content): #vamos pasando por cada caracter del mensaje
            indice =chNum[char] #obtenemos el indice del caracter actual
            valor_clave =self.key_indices[i % key_length] #obtenemos el valor de la clave correspondiente al caracter actual
                                                          #lo hacemos ciclico para que si el mensaje es mas largo que la clave, volvamos a empezar desde el principio de la clave

            if mode: #Comprobamos si estamos cifrando o descifrando
                new_indice=(indice + valor_clave) % n #ciframos el caracter sumando el indice del caracter y el valor de la clave
            else:
                new_indice=(indice - valor_clave) % n #desciframos el caracter restando el valor de la clave al indice del caracter

            textcod.append(numCh[new_indice]) #añadimos el nuevo indice a la lista
        
        return ''.join(textcod)  #unimos la lista en un string y lo devolvemos