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
 Solo se hace para inicializar el proyecto, descrito de modo informativo.

 Para inicializarlo se usa el siguiente comando:
 > uv init
 
 Esto crea:
 - **pyproject.toml**: Este es el corazón del proyecto se definen las dependencias ( librerías ).
 - **.python-version**: La versión de este proyecto. ( Última versión estable **3.14.0**).
 - **.gitignore**: lo actualiza para incluir la carpeta del entorno virtual (**.venv**).
