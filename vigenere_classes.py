from itertools import chain, groupby  # chain lo usamos para concatenar listas y groupby para agrupar
from vigenere_alphabet import *   #importamos todo de vigenere_alphabet.py

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
        self.key_index=[chNum[k] for k in self.key] #convertimos la clave a indices usando el diccionario chNum

    def cipher(self, mode=True): #Método para cifrar o descifrar el mensaje, mode=True para cifrar, False para descifrar

        textcod = [] #almacenamos el texto cifrado o descifrado
        key_length = len(self.key_index)  #longitud de la clave

        for i, char in enumerate(self.content): #vamos pasando por cada caracter del mensaje
            index = chNum[char] #obtenemos el indice del caracter actual
            key_value =self.key_index[i % key_length] #obtenemos el valor de la clave correspondiente al caracter actual
                                                          #lo hacemos ciclico para que si el mensaje es mas largo que la clave, volvamos a empezar desde el principio de la clave

            if mode: #Comprobamos si estamos cifrando o descifrando
                new_index=(index + key_value) % n #ciframos el caracter sumando el indice del caracter y el valor de la clave
            else:
                new_index=(index - key_value) % n #desciframos el caracter restando el valor de la clave al indice del caracter

            textcod.append(numCh[new_index]) #añadimos el nuevo indice a la lista
        
        return ''.join(textcod)  #unimos la lista en un string y lo devolvemos
    
class BreakVigenere(Message): #Clase encargada de descubrir la clave 

    def __init__(self, text): #constructor de la clase
        super().__init__(text) #llamamos al constructor de la clase Message

    def _index_of_coincidence(self, seg): #Método para obtener el IC (índice de coincidencia) que probabilidad que dos letras al azar sean iguales
        N = len(seg) #Longitud del texto
        count = {char : seg.count(char) for char in alphabet} #Contamos cuantas veces aparece cada letra en el segmento
        return sum(v*(v-1) for v in count.values()) / (N*(N-1)) if N > 1 else 0 #Cálculo del IC

    def estimated_key_length(self, max_length = 20): #Método para estimar la longitud de la clave
        candidates = [] #Lista de candidatos
        for L in range(1, max_length): #Iterar sobre las posibles longitudes de clave
            segments = [self.content[i::L] for i in range(L)] #Toma el segmento desde i y va de L en L
            con_index = sum(self._index_of_coincidence(seg) for seg in segments)/L #Para cada segmento calcula su IC
            candidates.append((L, con_index)) #Lo añadimos a la lista de candidatos
        candidates.sort(key = lambda x: x[1], reverse = True) #Los ordenamos según el IC promedio más alto
        return candidates[0][0] #Seleccionamos la longitud de clave más probable

    def rfrec(self, strng): #método para calcular la frecuencia relativa de cada caracter en un string
        return {k:len(list(g))/len(strng) for k, g in groupby(''.join(sorted(strng)))} #calculamos la frecuencia relativa de cada caracter

    def chiSquared(self, strng): #método para calcular el chi cuadrado de un string
        inventory = dict.fromkeys(alphabet,0) #inicializamos el inventario de frecuencias
        inventory.update(self.rfrec(strng)) #actualizamos el inventario con las frecuencias del texto
        chDegree = [(len(strng)*(inventory[ch]-alphFreq[ch]))**2/alphFreq[ch] for ch in inventory] #calculamos el chi cuadrado
        return sum(chDegree)  #devolvemos la suma del chi cuadrado

    def _best_shift(self, segment): #método para encontrar el mejor desplazamiento para un segmento
        best_shift = 0 #almacenamos el mejor desplazamiento
        best_chi = float('inf') #inicializamos el mejor chi al infinito
        for shift in range(n): #probamos todos los desplazamientos posibles
            decrypted = ''.join(numCh[(chNum[c]-shift) % n] for c in segment) #desciframos el segmento con el desplazamiento actual
            chi = self.chiSquared(decrypted) #calculamos el chi cuadrado del segmento descifrado
            if chi < best_chi: #si el chi cuadrado es mejor que el mejor encontrado hasta ahora
                best_chi = chi #actualizamos el mejor chi
                best_shift = shift #actualizamos el mejor desplazamiento
        return best_shift #devolvemos el mejor desplazamiento encontrado

    def recover_key(self, key_length): # método para recuperara la clave
        key = [] # Clave
        for i in range(key_length): # Recorremos los segmentos con tamañaos i hasta llegar al tamaño de la clave
            segment = self.content[i::key_length] #obtenemos el segmento
            shift = self._best_shift(segment) #Calculamos el mejor desplazamiento
            key.append(numCh[shift]) #añadimos el valor del caracter
        return ''.join(key) #devolvemos la clave sin espacios

    def break_cipher(self): #método que devuelve la clave
        key_length = self.estimated_key_length() # Obtenemos la longitud de la clave
        key = self.recover_key(key_length) # Obtenemos la clave 
        return key #devolvemos la clave encontrada