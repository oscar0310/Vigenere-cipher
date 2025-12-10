#alfabeto 
alphabet= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Caracteres especiales
alphSpecials = {
    'Á': 'A',
    'É' : 'E',
    'Í' : 'I',
    'Ó' : 'O',
    'Ú' : 'U',
    'Ä' : 'A',
    'Ë' : 'E',
    'Ï' : 'I',
    'Ö' : 'O',
    'Ü' : 'U',
    'Ñ' : 'GN'
}

#Tamaño del alfabeto
n=len(alphabet)

#Diccionario para  letras : índices 
chNum ={ letra: i for i, letra in enumerate(alphabet) }

#Diccionario para índices : letras
numCh ={ i: letra for i, letra in enumerate(alphabet) }