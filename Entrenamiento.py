
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import subprocess
from tkinter import Image, Label, Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from PIL import Image, ImageTk
import time

import cv2
#from Perfil import run_perfil  # Asegúrate de que la ruta de importación sea correcta

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets entrenamiento"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#2E0935")

def abrir_perfil():
    subprocess.Popen(["python", "Perfil.py"])
    window.destroy()


canvas = Canvas(
    window,
    bg = "#2E0935",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    720.0,
    512.0,
    image=image_image_1
)

canvas.create_rectangle(
    343.0,
    27.0,
    1402.0,
    998.0,
    fill="#E3E3E3",
    outline="")

canvas.create_text(
    666.0,
    233.0,
    anchor="nw",
    text="RECONOCIMIENTO FACIAL",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    366.0,
    53.0,
    1380.0,
    657.0,
    fill="#888181",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=820.0,
    y=826.0,
    width=105.0,
    height=112.0
)

"""canvas.create_text(
    758.0,
    673.0,
    anchor="nw",
    text="xx:xx",
    fill="#000000",
    font=("Inter", 96 * -1)
)"""

canvas.create_rectangle(
    42.0,
    27.0,
    304.0,
    998.0,
    fill="#E3E3E3",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    174.0,
    162.0,
    image=image_image_2
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=abrir_perfil,
    relief="flat"
    
)
button_2.place(
    x=82.0,
    y=349.0,
    width=183.9990234375,
    height=59.13140869140625
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=82.0,
    y=428.0,
    width=183.9990234375,
    height=59.13140869140625
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=80.0,
    y=507.0,
    width=183.9990234375,
    height=59.13140869140625
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=143.0,
    y=912.0,
    width=60.1756591796875,
    height=67.20001220703125
)
window.resizable(False, False)

label_camara = Label(window)
label_camara.place(x=366, y=50)  # Ajusta la posición según necesites

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def mostrar_camara():
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize(frame, (1014, 604))  # Cambia 320x240 al tamaño deseado
    img = Image.fromarray(frame_resized)
    imgtk = ImageTk.PhotoImage(image=img)
    label_camara.imgtk = imgtk
    label_camara.configure(image=imgtk)
    if cronometro_activo:  # Asegúrate de que la cámara se actualice solo si el cronómetro está activo
        label_camara.after(10, mostrar_camara)

    
# Variables globales para el cronómetro
cronometro_activo = False
tiempo_inicial = 0
id_texto_cronometro = None

def toggle_cronometro():
    global cronometro_activo, tiempo_inicial
    if cronometro_activo:
        cronometro_activo = False
    else:
        cronometro_activo = True
        tiempo_inicial = int(time.time())
        actualizar_cronometro()
        mostrar_camara()

def actualizar_cronometro():
    if cronometro_activo:
        tiempo_actual = int(time.time())
        tiempo_transcurrido = tiempo_actual - tiempo_inicial
        minutos, segundos = divmod(tiempo_transcurrido, 60)
        tiempo_str = f"{minutos:02d}:{segundos:02d}"
        canvas.itemconfig(id_texto_cronometro, text=tiempo_str)
        window.after(1000, actualizar_cronometro)

# Modificar el comando del botón 1 para iniciar/detener el cronómetro
button_1.configure(command=toggle_cronometro)

# Identificador del texto del cronómetro en el canvas
id_texto_cronometro = canvas.create_text(
    758.0,
    673.0,
    anchor="nw",
    text="00:00",
    fill="#000000",
    font=("Inter", 96 * -1)
)


window.mainloop()


