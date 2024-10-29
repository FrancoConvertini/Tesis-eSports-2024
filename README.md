# Tesis-eSports-2024

Este proyecto es una aplicacion de reconocimiento facial y emociones en tiempo real.

# Requisitos

- Python 3.8 o superior
- MySQL Server
- Librerías de Python (ver más abajo)

# Instalación

Clonar este repositorio en tu máquina local:

git clone https://github.com/FrancoConvertini/Tesis-eSports-2024.git

cd Tesis-eSports-2024.git

Configura un entorno virtual (opcional, pero recomendado):

-creacion del entorno virtual:

    python -m venv env

-activavion del entorno virtual

    source env/bin/activate  # En Mac/Linux

    env\Scripts\activate     # En Windows

Instalar dependecias:

pip install mysql-connector-python

pip install Pillow

pip install opencv-python

pip install mediapipe

pip install numpy

pip install pandas

pip install matplotlib

pip install tkinter

Configura la cámara: Verifica que la cámara esté configurada correctamente y que el puerto de acceso sea el correcto (por defecto, el puerto es 0).Podes cambiarlo en el código si tu cámara está en otro puerto:
-Extracto del codigo donde se especifica el puerto
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

Base de datos:
    La base de datos utilizada a lo largo del desarrollo es un MySQL, se hosteo esta misma base en un servidor AWS al cual tenemos que brindar acceso de forma manual.
    En caso de que esto no sea posible crear la base de datos de forma manual:

    CREATE DATABASE tesis2024;
    USE tesis2024;

    CREATE TABLE users (
        idUsers INT PRIMARY KEY,
        name VARCHAR(255),
        equipo VARCHAR(255),
        edad INT,
        videojuego VARCHAR(255),
        rol VARCHAR(255),
        password VARCHAR(255)
    );

    CREATE TABLE emociones (
        idSesion INT,
        emocion VARCHAR(255)
    );

    CREATE TABLE entrenamientos (
        idUsers INT,
        hora_inicio TIME,
        hora_final TIME,
        duracion INT,
        idSesion INT,
        idSesionUsuario INT
    );

    Importante destacar que el login se realiza mediante el campo idUsers.

Flujo de la aplicacion:
1) Ejecutar Login.py
2) En caso de ser jugador o coach habran 2 opciones:
3) Si se logea con un usuario coach lo primero que vera es la pantalla mi equipo y podra acceder a los datos de los jugadores del equipo
4) Si se logea con un usuario player podra ver el perfil, generar sesiones de entrenamiento y ver los reportes.