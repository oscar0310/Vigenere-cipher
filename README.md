# Vigenere-cipher
Repositorio para realizar la tarea de la asignatura de SPSI de la codificación de Vigenere


## Instalación UV:
 Para instalar uv tenemos dos opciones: 

 - Linux: 
 >curl -LsSf https://astral.sh/uv/install.sh | sh

 - Windows:
 >powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

 Una vez instalado lo actualizamos a la última versión:
 >uv self update
 
 Instalamos la versión que vamos a usar para el proyecto:
 >uv python install 3.14

 Si te da un warning ejecuta el comando que te ofrece y reinicia la terminal.

 Para comprobar que se ha instalado:
 >python3.14 --version

## Inicializar un Proyecto con UV:
 Solo se hace para inicializar el proyecto, descrito de modo informativo. **¡¡¡ NOO HACER !!!**.

 Para inicializarlo se usa el siguiente comando:
 > uv init
 
 Esto crea:
 - **pyproject.toml**: Este es el corazón del proyecto se definen las dependencias ( librerías ).
 - **.python-version**: La versión de este proyecto. ( Última versión estable **3.14.0**).
 - **.gitignore**: lo actualiza para incluir la carpeta del entorno virtual (**.venv**).

## Guia de uso:

 ### Pasos iniciales

Una vez instalado uv ( Estoy suponiendo que teneis git configurado en vuestro ordenador), clonais el repositorio:
>git clone https://github.com/oscar0310/Vigenere-cipher.git

Accedemos al repositorio en nuestro ordenador y dentro de el ejecutamos:
>uv sync

Con esto ya tendríamos el repositorio listo para trabajar.


 ### Ejecutar y Añadir librerías.
Para ejecutar el código:
>uv run archivo.py

Para añadir librerías:

1º La instalamos con uv para que quede constancia de la versión para que todos tengamos la misma:
>uv add librería

2ºLa añadimos ya en el código.

En caso de de querer borrarla:
>uv remove librería




## CRIPTOSISTEMA DE VIGENÈRE:

El cifrado de Vigenère es un cifrado que se desarrolló para mejorar el cifrado de César. El texto plano se cifra mediante una clave. Para cifrarlos funciona de la siguiente manera.

### MÉTODO DE CIFRADO DE VIGENÈRE:
 
 - Primero se introduce el texto plano con una clave.
 - Segundo se repite la clave tantas veces como haga falta para tener la misma longitud del texto.
 - Tercero Cada letra del texto plano se desplaza con la letra correspondiente de la palabra clave. El desplazamiento será positivo y se le sumará cuantas posiciones hay que desplazarse para la letra de la clave correspondiente.
 
 Con estos paso obtendríamos el texto plano codificado.

### EJEMPLO:
- Texto plano: Hola mundo.
- Clave: sol.
 
**CIFRADO DE VIGÈNERE**

|H|O|L|A|M|U|N|D|O|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|S|O|L|S|O|L|S|O|L|
|+18|+14|+11|+18|+14|+11|+18|+14|+11|
|Z|C|W|S|A|F|F|R|Z|

- Texto codificado: ZCWSAFFRZ.