from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import pandas as pd
import random


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets_resumen"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = tk.Tk()

window.geometry("1440x1024")
window.configure(bg = "#2E0935")


canvas = tk.Canvas(
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

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    172.0,
    512.0,
    image=image_image_2
)

logo = PhotoImage(
    file=relative_to_assets("logo.png"))
image_logo = canvas.create_image(
    173.0,
    162.0,
    image=logo
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    867.0,
    512.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image.png"))
image_4 = canvas.create_image(
    862.0,
    811.0,
    image=image_image_4
)

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
    x=81.0,
    y=349.0,
    width=183.9990234375,
    height=59.13140869140625
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=81.0,
    y=428.0,
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
    x=81.0,
    y=512.0,
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
    x=142.0,
    y=912.0,
    width=60.1756591796875,
    height=67.20001220703125
)


canvas.create_rectangle(
    377.0,
    127.0,
    1353.9999389648438,
    130.01237100338187,
    fill="#000000",
    outline="")

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    410.0,
    81.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    654.0,
    91.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_mini.png"))
image_7 = canvas.create_image(
    598.0,
    230.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image.png"))
image_8 = canvas.create_image(
    862.0,
    474.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    544.0,
    343.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    532.0,
    682.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    598.0,
    243.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    497.0,
    199.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    430.0,
    199.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_mini.png"))
image_14 = canvas.create_image(
    1125.0,
    230.0,
    image=image_image_14
)

#image_image_15 = PhotoImage(
    #file=relative_to_assets("image_15.png"))
#image_15 = canvas.create_image(
    #1125.0,
    #243.0,
    #image=image_image_15
#)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    1080.0,
    199.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    439.0,
    684.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    1283.0,
    90.0,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    1183.0,
    90.0,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    434.0,
    342.0,
    image=image_image_20
)

image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    961.0,
    200.0,
    image=image_image_21
)





# Tiempo (en minutos)
tiempo = [0, 10, 20, 30, 40, 50, 60]

# Emociones asociadas a intervalos de tiempo
emociones_principal = ['Concentración', 'Frustración', 'Calma', 'Concentración', 'Frustración', 'Calma']
emociones_secundaria = ['Calma', 'Concentración', None, 'Frustración', 'Calma', None]

# Asignar un color a cada emoción
colores = {
    'Concentración': 'blue',
    'Frustración': 'red',
    'Calma': 'green'
}



# Emociones asociadas a intervalos de tiempo
emociones = ['Concentración', 'Feliz', 'Frustración', 'Calma', 'Enojado', 'Estresado', 'Neutral']

# Asignar un número a cada emoción
emociones_dict = {
    'Concentración': 6, 
    'Feliz': 5, 
    'Calma': 4, 
    'Neutral': 3, 
    'Frustración': 2, 
    'Enojado': 1,
    'Estresado': 0
}



# Tiempo en minutos para el segundo gráfico
tiempo = np.linspace(0, 60, 7)  # Intervalos de 10 minutos
emociones = ['Concentración', 'Feliz', 'Frustración', 'Calma', 'Enojado', 'Estresado', 'Neutral']
emociones_dict = {
    'Concentración': 6, 
    'Feliz': 5, 
    'Calma': 4, 
    'Neutral': 3, 
    'Frustración': 2, 
    'Enojado': 1,
    'Estresado': 0
}
emociones_num = [emociones_dict[emocion] for emocion in emociones]

# Generar un tiempo aleatorio en segundos mayor a 3 horas (10800 segundos)
tiempo_total_segundos = random.randint(10800, 28800)  # Hasta 24 horas

# Convertir el tiempo en horas, minutos y segundos
horas = tiempo_total_segundos // 3600
minutos = (tiempo_total_segundos % 3600) // 60
segundos = tiempo_total_segundos % 60

# Formatear el tiempo en el formato "XX h XX m XX s"
tiempo_formateado = f"{horas:02d} h {minutos:02d} m {segundos:02d} s"

# Mostrar la emoción en un Label en lugar de la imagen "image_11.png"
label_emocion = tk.Label(window, text= tiempo_formateado, bg="#413A43", fg="white", font=("Arial", 24))
label_emocion.place(x=598, y=243, anchor="center")

print(tiempo_formateado)


#---------------------- Grafico de lineas ----------------------#


# Generar datos aleatorios para las emociones
emociones_num = [random.randint(0, 6) for _ in range(len(tiempo))]

# Crear un frame para el gráfico
frame_grafico = tk.Frame(window, bg="white", width=800, height=400)
frame_grafico.place(x=453, y=356)

# Definir el tamaño en píxeles
ancho_pixeles = 850
alto_pixeles = 271

# Convertir el tamaño en píxeles a pulgadas (asumiendo una resolución de 100 DPI)
dpi = 100
ancho_pulgadas = ancho_pixeles / dpi
alto_pulgadas = alto_pixeles / dpi

# Crear la figura y los ejes
fig = Figure(figsize=(ancho_pulgadas, alto_pulgadas))
fig.patch.set_facecolor('#413A43')  # Cambiar el color de fondo de la figura
fig.patch.set_alpha(1)  # Ajustar la opacidad de la figura
ax = fig.add_subplot(111)
ax.set_facecolor('#413A43')
ax.patch.set_alpha(1)  # Ajustar la opacidad de los ejes

# Graficar la variabilidad emocional
ax.plot(tiempo, emociones_num, marker='o', linestyle='-', color='green')

# Etiquetas para el eje Y basadas en las emociones
ax.set_yticks([0, 1, 2, 3, 4, 5, 6])
ax.set_yticklabels(['Estresado', 'Enojado', 'Frustración', 'Neutral', 'Calma', 'Feliz', 'Concentración'])

# Etiquetas para el eje X
fig.tight_layout(pad=2.0)
ax.tick_params(axis='both', which='major', labelsize=8, colors='white')
ax.set_xticks(np.arange(0, 61, 10))  # Tiempo en intervalos de 10 minutos
ax.set_xlabel('Tiempo (minutos)', color='white')
ax.set_ylabel('Emociones', color='white')



# Añadir líneas horizontales para diferenciar las emociones
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Crear el canvas para el gráfico y añadirlo al frame
canvas_grafico = FigureCanvasTkAgg(fig, master=frame_grafico)
canvas_grafico.draw()
canvas_grafico.get_tk_widget().pack(fill=tk.BOTH, expand=True)



#---------------------- Grafico de barras ----------------------#



# Generar tiempos aleatorios para cada emoción
tiempo_total_emociones = [random.randint(10, 60) for _ in emociones]

# Encontrar el índice del tiempo más alto
indice_max_tiempo = tiempo_total_emociones.index(max(tiempo_total_emociones))

# Obtener la emoción asociada al tiempo más alto
emocion_max_tiempo = emociones[indice_max_tiempo]

# Mostrar la emoción en un Label en lugar de la imagen "image_15.png"
label_emocion = tk.Label(window, text= emocion_max_tiempo, bg="#413A43", fg="white", font=("Arial", 24))
label_emocion.place(x=1125, y=243, anchor="center")
#1125.0,
#243.0,

# Imprimir la emoción asociada al tiempo más alto
print(f'La emoción asociada al tiempo más alto es: {emocion_max_tiempo}')

# Colores para cada barra
colores_barras = ['blue', 'green', 'red', 'purple', 'orange', 'pink', 'cyan']

# Crear un frame para el gráfico de barras
frame_barras = tk.Frame(window, bg="white", width=800, height=400)
frame_barras.place(x=460, y=690)

# Crear la figura y los ejes para el gráfico de barras
fig_barras = Figure(figsize=(ancho_pulgadas, alto_pulgadas))
fig_barras.tight_layout(pad=2.0)
fig_barras.patch.set_facecolor('#413A43')  # Cambiar el color de fondo de la figura
fig_barras.patch.set_alpha(1)  # Ajustar la opacidad de la figura
ax_barras = fig_barras.add_subplot(111)
ax_barras.set_facecolor('#413A43')
ax_barras.patch.set_alpha(0.8157)  # Ajustar la opacidad de los ejes

fig_barras.subplots_adjust(left=0.1, right=0.97, top=0.9, bottom=0.1)
# Graficar el tiempo total de cada emoción
ax_barras.bar(emociones, tiempo_total_emociones, color=colores_barras)

# Etiquetas para el eje X e Y
#ax_barras.set_xlabel('Emociones', color='white')
ax_barras.set_ylabel('Tiempo Total (minutos)', color='white')




# Cambiar el color de las etiquetas de los ticks
ax_barras.tick_params(axis='both', which='major', labelsize=8, colors='white')

# Crear el canvas para el gráfico de barras y añadirlo al frame
canvas_barras = FigureCanvasTkAgg(fig_barras, master=frame_barras)
canvas_barras.draw()
canvas_barras.get_tk_widget().pack(fill=tk.BOTH, expand=True)





window.resizable(False, False)
window.mainloop()