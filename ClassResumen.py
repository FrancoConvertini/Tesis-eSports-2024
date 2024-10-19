from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label, Frame
import tkinter as tk
import random
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sys
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets_resumen"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class EmocionesApp:
    def __init__(self, root, idSesionUsuario):
        self.root = root
        self.root.geometry("1440x1024")
        self.root.configure(bg="#2E0935")
        self.canvas = Canvas(self.root, bg="#2E0935", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.idSesionUsuario = idSesionUsuario
        print("idSesionUsuario recibido", idSesionUsuario)
        # Cargar imágenes y botones
        self.load_images()
        self.create_buttons()
        self.place_images()
        # Crear gráficos
        self.create_tiempo_label()
        self.create_line_graph()
        self.create_bar_graph()
        # Crear el label de emoción
        self.create_emotion_label()

        self.root.resizable(False, False)
    
    def load_images(self):
        """Carga las imágenes de la interfaz."""
        self.images = {
            "image_1": PhotoImage(file=relative_to_assets("image_1.png")),
            "image_2": PhotoImage(file=relative_to_assets("image_2.png")),
            "logo": PhotoImage(file=relative_to_assets("logo.png")),
            "image_3": PhotoImage(file=relative_to_assets("image_3.png")),
            "image_4": PhotoImage(file=relative_to_assets("image.png")),
            "image_4repeat": PhotoImage(file=relative_to_assets("image.png")),
            "button_1": PhotoImage(file=relative_to_assets("button_1.png")),
            "button_2": PhotoImage(file=relative_to_assets("button_2.png")),
            "button_3": PhotoImage(file=relative_to_assets("button_3.png")),
            "button_4": PhotoImage(file=relative_to_assets("button_4.png")),
            "image_5": PhotoImage(file=relative_to_assets("image_5.png")),
            "image_6": PhotoImage(file=relative_to_assets("image_6.png")),
            "image_7": PhotoImage(file=relative_to_assets("image_mini.png")),
            "image_8": PhotoImage(file=relative_to_assets("image_mini.png")),
            "image_9": PhotoImage(file=relative_to_assets("image_9.png")),
            "image_10": PhotoImage(file=relative_to_assets("image_10.png")),
            "image_11": PhotoImage(file=relative_to_assets("image_11.png")),
            "image_12": PhotoImage(file=relative_to_assets("image_12.png")),
            "image_13": PhotoImage(file=relative_to_assets("image_13.png")),
            "image_16": PhotoImage(file=relative_to_assets("image_16.png")),
            "image_17": PhotoImage(file=relative_to_assets("image_17.png")),
            "image_18": PhotoImage(file=relative_to_assets("image_18.png")),
            "image_19": PhotoImage(file=relative_to_assets("image_19.png")),
            "image_20": PhotoImage(file=relative_to_assets("image_20.png")),
            "image_21": PhotoImage(file=relative_to_assets("image_21.png"))
        }

    def place_images(self):
        """Coloca todas las imágenes en el canvas."""
        self.canvas.create_image(720.0, 512.0, image=self.images["image_1"])  # Main image
        self.canvas.create_image(172.0, 512.0, image=self.images["image_2"])  # Side image
        self.canvas.create_image(173.0, 162.0, image=self.images["logo"])      # Logo
        self.canvas.create_image(867.0, 512.0, image=self.images["image_3"])  # Right side image
        self.canvas.create_image(862.0, 811.0, image=self.images["image_4"])  # Bottom image
        self.canvas.create_image(862.0, 474.0, image=self.images["image_4repeat"])  # Bottom image
        self.canvas.create_image(410.0, 81.0, image=self.images["image_5"])   # Adjusted position for image_5
        self.canvas.create_image(654.0, 91.0, image=self.images["image_6"])   # Adjusted position for image_6
        self.canvas.create_image(598.0, 230.0, image=self.images["image_7"])  # Adjusted position for image_7
        self.canvas.create_image(1125.0, 230.0, image=self.images["image_8"]) # Adjusted position for image_8
        self.canvas.create_image(544.0, 343.0, image=self.images["image_9"])  # Adjusted position for image_9
        self.canvas.create_image(532.0, 682.0, image=self.images["image_10"]) # Adjusted position for image_10
        self.canvas.create_image(598.0, 243.0, image=self.images["image_11"]) # Adjusted position for image_11
        self.canvas.create_image(497.0, 199.0, image=self.images["image_12"]) # Adjusted position for image_12
        self.canvas.create_image(430.0, 199.0, image=self.images["image_13"]) # Adjusted position for image_13
        self.canvas.create_image(1080.0, 199.0, image=self.images["image_16"]) # Adjusted position for image_16
        self.canvas.create_image(439.0, 684.0, image=self.images["image_17"])  # Adjusted position for image_17
        self.canvas.create_image(1283.0, 90.0, image=self.images["image_18"])  # Adjusted position for image_18
        self.canvas.create_image(1183.0, 90.0, image=self.images["image_19"])  # Adjusted position for image_19
        self.canvas.create_image(434.0, 342.0, image=self.images["image_20"])  # Adjusted position for image_20
        self.canvas.create_image(961.0, 200.0, image=self.images["image_21"])   # Adjusted position for image_21

    def create_buttons(self):
        """Crea los botones de la interfaz."""
        self.button_1 = Button(image=self.images["button_1"], borderwidth=0, highlightthickness=0, relief="flat",
                               command=lambda: print("Button 1 clicked"))
        self.button_1.place(x=81.0, y=349.0, width=184, height=59)

        self.button_2 = Button(image=self.images["button_2"], borderwidth=0, highlightthickness=0, relief="flat",
                               command=lambda: print("Button 2 clicked"))
        self.button_2.place(x=81.0, y=428.0, width=184, height=59)

        self.button_3 = Button(image=self.images["button_3"], borderwidth=0, highlightthickness=0, relief="flat",
                               command=lambda: print("Button 3 clicked"))
        self.button_3.place(x=81.0, y=512.0, width=184, height=59)

        self.button_4 = Button(image=self.images["button_4"], borderwidth=0, highlightthickness=0, relief="flat",
                               command=lambda: print("Button 4 clicked"))
        self.button_4.place(x=142.0, y=912.0, width=60, height=67)

    def create_tiempo_label(self):
        """Crea un label para mostrar el tiempo formateado aleatoriamente."""
        tiempo_total_segundos = random.randint(10800, 28800)  # 3 a 8 horas en segundos
        horas = tiempo_total_segundos // 3600
        minutos = (tiempo_total_segundos % 3600) // 60
        segundos = tiempo_total_segundos % 60
        tiempo_formateado = f"{horas:02d} h {minutos:02d} m {segundos:02d} s"

        label_tiempo = Label(self.root, text=tiempo_formateado, bg="#413A43", fg="white", font=("Arial", 24))
        label_tiempo.place(x=598, y=243, anchor="center")
        print(tiempo_formateado)

    def create_emotion_label(self):
        """Crea un label para mostrar la emoción asociada al tiempo más alto."""
        emociones = ['Concentración', 'Feliz', 'Frustración', 'Calma', 'Enojado', 'Estresado', 'Neutral']
        tiempo_total_emociones = [random.randint(10, 60) for _ in emociones]
        indice_max_tiempo = tiempo_total_emociones.index(max(tiempo_total_emociones))
        emocion_max_tiempo = emociones[indice_max_tiempo]

        label_emocion = Label(self.root, text=emocion_max_tiempo, bg="#413A43", fg="white", font=("Arial", 24))
        label_emocion.place(x=1125, y=243, anchor="center")
        print(f'La emoción asociada al tiempo más alto es: {emocion_max_tiempo}')

    def create_line_graph(self):
        """Crea un gráfico de líneas para visualizar las emociones a lo largo del tiempo."""
        tiempo = np.linspace(0, 60, 7)  # Intervalos de 10 minutos
        emociones_num = [random.randint(0, 6) for _ in range(len(tiempo))]

        frame_grafico = Frame(self.root, bg="white", width=800, height=400)
        frame_grafico.place(x=453, y=356)

        fig = Figure(figsize=(8.5, 2.71))
        fig.patch.set_facecolor('#413A43')
        ax = fig.add_subplot(111)
        ax.set_facecolor('#413A43')

        ax.plot(tiempo, emociones_num, marker='o', linestyle='-', color='green')
        ax.set_yticks([0, 1, 2, 3, 4, 5, 6])
        ax.set_yticklabels(['Estresado', 'Enojado', 'Frustración', 'Neutral', 'Calma', 'Feliz', 'Concentración'])
        ax.tick_params(axis='both', which='major', labelsize=8, colors='white')
        ax.set_xticks(np.arange(0, 61, 10))
        ax.set_xlabel('Tiempo (minutos)', color='white')
        ax.set_ylabel('Emociones', color='white')
        ax.grid(True, axis='y', linestyle='--', alpha=0.7)

        canvas_grafico = FigureCanvasTkAgg(fig, master=frame_grafico)
        canvas_grafico.draw()
        canvas_grafico.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def create_bar_graph(self):
        """Crea un gráfico de barras para mostrar el tiempo total de cada emoción."""
        emociones = ['Concentración', 'Feliz', 'Frustración', 'Calma', 'Enojado', 'Estresado', 'Neutral']
        tiempo_total_emociones = [random.randint(10, 60) for _ in emociones]
        colores_barras = ['blue', 'green', 'red', 'purple', 'orange', 'pink', 'cyan']

        frame_barras = Frame(self.root, bg="white", width=800, height=400)
        frame_barras.place(x=460, y=690)

        fig_barras = Figure(figsize=(8.5, 2.71))
        fig_barras.patch.set_facecolor('#413A43')
        ax_barras = fig_barras.add_subplot(111)
        ax_barras.set_facecolor('#413A43')

        ax_barras.bar(emociones, tiempo_total_emociones, color=colores_barras)
        ax_barras.set_ylabel('Tiempo Total (minutos)', color='white')
        ax_barras.tick_params(axis='both', which='major', labelsize=8, colors='white')

        canvas_barras = FigureCanvasTkAgg(fig_barras, master=frame_barras)
        canvas_barras.draw()
        canvas_barras.get_tk_widget().pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = Tk()
    # Recuperar el argumento de línea de comando
    if len(sys.argv) > 1:
        idSesionUsuario = sys.argv[1]
    else:
        idSesionUsuario = None  # Manejo de error si no se pasa un argumento

    app = EmocionesApp(root, idSesionUsuario)
    root.mainloop()