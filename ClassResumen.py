from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label, Frame
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random

class ResumenApp:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1440x1024")
        self.window.configure(bg="#2E0935")
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / "assets_resumen"
        self.setup_ui()
        self.generate_emotions_graph()
        self.generate_bars_graph()
        self.show_emotion_time()

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def setup_ui(self):
        # Configuración del canvas y botones
        self.canvas = tk.Canvas(
            self.window,
            bg="#2E0935",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Imágenes en el canvas
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(720.0, 512.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.canvas.create_image(172.0, 512.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.canvas.create_image(867.0, 512.0, image=self.image_image_3)

        # Botones en el canvas
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(x=81.0, y=349.0, width=184, height=59)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(x=81.0, y=428.0, width=184, height=59)

    def generate_emotions_graph(self):
        # Generar emociones y gráficas
        tiempo = np.linspace(0, 60, 7)
        emociones = ['Concentración', 'Feliz', 'Frustración', 'Calma', 'Enojado', 'Estresado', 'Neutral']
        emociones_dict = {'Concentración': 6, 'Feliz': 5, 'Calma': 4, 'Neutral': 3, 'Frustración': 2, 'Enojado': 1, 'Estresado': 0}
        emociones_num = [emociones_dict[emocion] for emocion in emociones]

        # Crear frame para gráfico de emociones
        frame_grafico = Frame(self.window, bg="white", width=800, height=400)
        frame_grafico.place(x=453, y=356)

        fig = Figure(figsize=(8.5, 2.71), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(tiempo, emociones_num, marker='o', linestyle='-', color='green')
        ax.set_yticks([0, 1, 2, 3, 4, 5, 6])
        ax.set_yticklabels(['Estresado', 'Enojado', 'Frustración', 'Neutral', 'Calma', 'Feliz', 'Concentración'])
        ax.set_xticks(np.arange(0, 61, 10))
        ax.set_xlabel('Tiempo (minutos)')
        ax.set_ylabel('Emociones')
        ax.grid(True, axis='y', linestyle='--', alpha=0.7)

        canvas_grafico = FigureCanvasTkAgg(fig, master=frame_grafico)
        canvas_grafico.draw()
        canvas_grafico.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def generate_bars_graph(self):
        # Crear gráfico de barras
        emociones = ['Concentración', 'Feliz', 'Frustración', 'Calma', 'Enojado', 'Estresado', 'Neutral']
        tiempo_total_emociones = [random.randint(10, 60) for _ in emociones]
        colores_barras = ['blue', 'green', 'red', 'purple', 'orange', 'pink', 'cyan']

        frame_barras = Frame(self.window, bg="white", width=800, height=400)
        frame_barras.place(x=460, y=690)

        fig_barras = Figure(figsize=(8.5, 2.71), dpi=100)
        ax_barras = fig_barras.add_subplot(111)
        ax_barras.bar(emociones, tiempo_total_emociones, color=colores_barras)
        ax_barras.set_ylabel('Tiempo Total (minutos)')
        ax_barras.grid(True, axis='y', linestyle='--', alpha=0.7)

        canvas_barras = FigureCanvasTkAgg(fig_barras, master=frame_barras)
        canvas_barras.draw()
        canvas_barras.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def show_emotion_time(self):
        # Mostrar tiempo total aleatorio
        tiempo_total_segundos = random.randint(10800, 28800)
        horas = tiempo_total_segundos // 3600
        minutos = (tiempo_total_segundos % 3600) // 60
        segundos = tiempo_total_segundos % 60
        tiempo_formateado = f"{horas:02d} h {minutos:02d} m {segundos:02d} s"

        label_emocion = Label(self.window, text=tiempo_formateado, bg="#2E0935", fg="white", font=("Arial", 24))
        label_emocion.place(x=598, y=243, anchor="center")


if __name__ == "__main__":
    window = Tk()
    app = ResumenApp(window)
    window.resizable(False, False)
    window.mainloop()
