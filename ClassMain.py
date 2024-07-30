from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Button, PhotoImage, Scrollbar, Frame, Label
from PIL import Image, ImageTk
import time
import cv2
import tkinter as tk
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x1024")
        self.root.configure(bg="#FFFFFF")
        self.root.resizable(False, False)
        

        self.perfil_app = PerfilApp (root, self.switch_to_main)
        self.perfil_app.pack()
        self.reconocimiento_app = ReconocimientoFacialApp (root, self.switch_to_main)
        self.reconocimiento_app.pack_forget()
       
        

class CoachApp(Frame):
    print("entre en coachapp")
    def __init__(self, root, switch_callback):
        Frame.__init__(self, root)
        self.root = root
        self.switch_callback = switch_callback
        
        self.canvas = Canvas(
            self.root,
            bg="#E3E3E3",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.ASSETS_PATH = Path(__file__).parent / "assets"
        self.load_images()
        self.create_widgets()

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def load_images(self):
        self.image_1 = PhotoImage(file=self.relative_to_assets("Fondo.png"))
        self.image_2 = PhotoImage(file=self.relative_to_assets("MenuIzq.png"))
        self.image_3 = PhotoImage(file=self.relative_to_assets("CuadradoMedio.png"))
        self.image_4 = PhotoImage(file=self.relative_to_assets("Ojo.png"))
        self.image_5 = PhotoImage(file=self.relative_to_assets("RectanguloNegro.png"))
        self.image_6 = PhotoImage(file=self.relative_to_assets("iconoUsuario.png"))
        self.image_7 = PhotoImage(file=self.relative_to_assets("RectanguloNegro.png"))
        self.image_8 = PhotoImage(file=self.relative_to_assets("iconoUsuario.png"))
        self.image_9 = PhotoImage(file=self.relative_to_assets("RectanguloNegro.png"))
        self.image_10 = PhotoImage(file=self.relative_to_assets("iconoUsuario.png"))
        self.image_11 = PhotoImage(file=self.relative_to_assets("RectanguloNegro.png"))
        self.image_12 = PhotoImage(file=self.relative_to_assets("iconoUsuario.png"))
        self.image_13 = PhotoImage(file=self.relative_to_assets("Team.png"))
        self.image_14 = PhotoImage(file=self.relative_to_assets("RectanguloNegro.png"))
        self.image_15 = PhotoImage(file=self.relative_to_assets("iconoUsuario.png"))
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("Detalles.png"))
        self.button_image_2 = PhotoImage(file=self.relative_to_assets("Detalles.png"))
        self.button_image_3 = PhotoImage(file=self.relative_to_assets("Detalles.png"))
        self.button_image_4 = PhotoImage(file=self.relative_to_assets("Detalles.png"))
        self.button_image_5 = PhotoImage(file=self.relative_to_assets("Detalles.png"))
        self.button_image_6 = PhotoImage(file=self.relative_to_assets("MiEquipo.png"))

    def create_widgets(self):
        self.canvas.create_image(720.0, 512.0, image=self.image_1)
        self.canvas.create_image(172.0, 512.0, image=self.image_2)
        self.canvas.create_image(872.0, 512.0, image=self.image_3)
        self.canvas.create_image(173.0, 110.0, image=self.image_4)
        self.canvas.create_image(873.0, 642.0, image=self.image_5)
        self.canvas.create_text(459.0, 626.0, anchor="nw", text="Jugador 4\n\n", fill="#FFFFFF", font=("Roboto", 22 * -1))
        self.canvas.create_image(419.0, 643.0, image=self.image_6)
        self.canvas.create_image(873.0, 555.0, image=self.image_7)
        self.canvas.create_text(459.0, 539.0, anchor="nw", text="Jugador 3\n\n", fill="#FFFFFF", font=("Roboto", 22 * -1))
        self.canvas.create_image(419.0, 556.0, image=self.image_8)
        self.canvas.create_image(873.0, 468.0, image=self.image_9)
        self.canvas.create_text(459.0, 452.0, anchor="nw", text="Jugador 2\n\n", fill="#FFFFFF", font=("Roboto", 22 * -1))
        self.canvas.create_image(419.0, 469.0, image=self.image_10)
        self.canvas.create_image(873.0, 381.0, image=self.image_11)
        self.canvas.create_text(459.0, 365.0, anchor="nw", text="Jugador 1\n\n", fill="#FFFFFF", font=("Roboto", 22 * -1))
        self.canvas.create_image(419.0, 382.0, image=self.image_12)
        self.canvas.create_image(489.0, 146.0, image=self.image_13)
        self.canvas.create_image(873.0, 729.0, image=self.image_14)
        self.canvas.create_text(459.0, 713.0, anchor="nw", text="Jugador 5\n\n\n", fill="#FFFFFF", font=("Roboto", 22 * -1))
        self.canvas.create_image(419.0, 730.0, image=self.image_15)

        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(x=1192.0, y=614.0, width=154.0, height=46.0)

        self.button_2 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(x=1192.0, y=701.0, width=154.0, height=46.0)

        self.button_3 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(x=1192.0, y=527.0, width=154.0, height=46.0)

        self.button_4 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(x=1192.0, y=440.0, width=154.0, height=46.0)

        self.button_5 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(x=1192.0, y=353.0, width=154.0, height=46.0)

        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.button_6.place(x=80.0, y=351.0, width=184.0, height=59.0)

        self.canvas.create_text(807.0, 155.0, anchor="nw", text="Equipo", fill="#931668", font=("Inter Bold", 40 * -1))

class ReconocimientoFacialApp(Frame):
    print("entre en reconocimientofacialapp")
    def __init__(self, root, switch_callback):
        Frame.__init__(self, root)
        self.root = root
        self.switch_callback = switch_callback
        self.cronometro_activo = False
        self.tiempo_inicial = 0
        self.contador = 0

        self.setup_ui()
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def setup_ui(self):
        self.canvas = Canvas(
            self.root,
            bg="#2E0935",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        
        self.image_image_1 = PhotoImage(file=relative_to_assets("fondo.png"))
        self.canvas.create_image(720.0, 512.0, image=self.image_image_1)

        self.canvas.create_rectangle(343.0, 27.0, 1402.0, 998.0, fill="#E3E3E3", outline="")
        self.canvas.create_text(666.0, 233.0, anchor="nw", text="RECONOCIMIENTO FACIAL", fill="#000000", font=("Inter", 12 * -1))
        self.canvas.create_rectangle(366.0, 53.0, 1380.0, 657.0, fill="#888181", outline="")

        self.button_image_1 = PhotoImage(file=relative_to_assets("Play.png"))
        self.button_1 = Button(image=self.button_image_1, borderwidth=0, highlightthickness=0, command=self.toggle_cronometro, relief="flat")
        self.button_1.place(x=820.0, y=826.0, width=105.0, height=112.0)
        
        self.canvas.create_rectangle(42.0, 27.0, 304.0, 998.0, fill="#E3E3E3", outline="")
        
        self.image_image_2 = PhotoImage(file=relative_to_assets("Ojo.png"))
        self.canvas.create_image(174.0, 162.0, image=self.image_image_2)

        self.button_image_2 = PhotoImage(file=relative_to_assets("Perfil.png"))
        self.button_2 = Button(image=self.button_image_2, borderwidth=0, highlightthickness=0, command=self.abrir_perfil, relief="flat")
        self.button_2.place(x=82.0, y=349.0, width=183.9990234375, height=59.13140869140625)

        self.button_image_3 = PhotoImage(file=relative_to_assets("Entrenar.png"))
        self.button_3 = Button(image=self.button_image_3, borderwidth=0, highlightthickness=0, command=lambda: print("button_3 clicked"), relief="flat")
        self.button_3.place(x=82.0, y=428.0, width=183.9990234375, height=59.13140869140625)

        self.button_image_4 = PhotoImage(file=relative_to_assets("MiEquipo.png"))
        self.button_4 = Button(image=self.button_image_4, borderwidth=0, highlightthickness=0, command=lambda: print("button_4 clicked"), relief="flat")
        self.button_4.place(x=80.0, y=507.0, width=183.9990234375, height=59.13140869140625)

        self.button_image_5 = PhotoImage(file=relative_to_assets("Apagar.png"))
        self.button_5 = Button(image=self.button_image_5, borderwidth=0, highlightthickness=0, command=lambda: print("button_5 clicked"), relief="flat")
        self.button_5.place(x=143.0, y=912.0, width=60.1756591796875, height=67.20001220703125)

        self.label_camara = Label(self.root)
        self.label_camara.place(x=366, y=50)  # Ajusta la posición según necesites

        self.id_texto_cronometro = self.canvas.create_text(758.0, 673.0, anchor="nw", text="00:00", fill="#000000", font=("Inter", 96 * -1))

    def abrir_perfil(self):
        subprocess.Popen(["python", "Perfil.py"])
        self.root.destroy()

    def toggle_cronometro(self):
        if self.cronometro_activo:
            self.cronometro_activo = False
            self.contador += 1
            print(self.contador)
        else:
            self.cronometro_activo = True
            self.tiempo_inicial = int(time.time())
            self.actualizar_cronometro()
            self.mostrar_camara()

    def actualizar_cronometro(self):
        if self.cronometro_activo:
            tiempo_actual = int(time.time())
            tiempo_transcurrido = tiempo_actual - self.tiempo_inicial
            minutos, segundos = divmod(tiempo_transcurrido, 60)
            tiempo_str = f"{minutos:02d}:{segundos:02d}"
            self.canvas.itemconfig(self.id_texto_cronometro, text=tiempo_str)
            self.root.after(1000, self.actualizar_cronometro)

    def mostrar_camara(self):
        _, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame, (1014, 604))  # Cambia 320x240 al tamaño deseado
        img = Image.fromarray(frame_resized)
        imgtk = ImageTk.PhotoImage(image=img)
        self.label_camara.imgtk = imgtk
        self.label_camara.configure(image=imgtk)
        if self.cronometro_activo:  # Asegúrate de que la cámara se actualice solo si el cronómetro está activo
            self.label_camara.after(10, self.mostrar_camara)

class PerfilApp(Frame):
    print("entre en perfilapp")
    def __init__(self, root, switch_callback):
        Frame.__init__(self, root)
        self.root = root
        self.switch_callback = switch_callback
      

        self.image_count = 0
        self.sesion = 1
        self.setup_ui()

    def setup_ui(self):
        # Crear un Frame para contener el Canvas y la Scrollbar
        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Crear el frame secundario que será desplazable
        self.frame_sesion = Frame(self.root, bg="#2E0935")
        self.frame_sesion.place(x=381, y=338, width=1005, height=633)

        self.canvas = Canvas(
            self.main_frame,
            bg="#2E0935",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge",
            scrollregion=(0, 0, 0, 1024)  # Ajustar según el contenido
        )
        self.canvas.place(x=0, y=0)

        # Crear un Canvas dentro de frame_sesion
        self.inner_canvas = Canvas(
            self.frame_sesion,
            bg="#E3E3E3",
            height=633,
            width=1005,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.inner_canvas.pack(fill="both", expand=True, side="left")

        # Crear la Scrollbar y asociarla con el Canvas
        self.inner_scrollbar = Scrollbar(self.frame_sesion, orient="vertical", command=self.inner_canvas.yview)
        self.inner_scrollbar.pack(side="right", fill="y")
        self.inner_canvas.configure(yscrollcommand=self.inner_scrollbar.set)
        self.inner_canvas.configure(scrollregion=self.inner_canvas.bbox("all"))

        self.inner_canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        # Asegúrate de que inner_canvas tenga una lista para almacenar referencias de imágenes
        self.inner_canvas.images = []

        # Configurar el Canvas principal
        self.setup_canvas()

        # Botones
        self.setup_buttons()

    def _on_mousewheel(self, event):
        self.inner_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def setup_canvas(self):
        self.image_image_1 = PhotoImage(file=relative_to_assets("Fondo.png"))
        self.canvas.create_image(720.0, 512.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=relative_to_assets("MenuIzq.png"))
        self.canvas.create_image(172.0, 512.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=relative_to_assets("CuadradoMedio.png"))
        self.canvas.create_image(867.0, 512.0, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=relative_to_assets("fotoUser.png"))
        self.canvas.create_image(477.0, 162.0, image=self.image_image_4)

        self.image_image_5 = PhotoImage(file=relative_to_assets("Ojo.png"))
        self.canvas.create_image(173.0, 162.0, image=self.image_image_5)

        self.canvas.create_text(817.0, 41.0, anchor="nw", text="Perfil del jugador", fill="#931668", font=("Inter", 20 * -1))
        self.canvas.create_text(591.0, 98.0, anchor="nw", text="Nombre:", fill="#921568", font=("Inter", 20 * -1))
        self.canvas.create_text(591.0, 135.0, anchor="nw", text="Edad:", fill="#931668", font=("Inter", 20 * -1))
        self.canvas.create_text(591.0, 170.0, anchor="nw", text="Videojuego:", fill="#931668", font=("Inter", 20 * -1))
        self.canvas.create_text(591.0, 205.0, anchor="nw", text="Equipo:", fill="#931668", font=("Inter", 20 * -1))

        self.canvas.create_rectangle(383.0, 286.0, 1359.9999389648438, 289.0123710033819, fill="#000000", outline="")

        self.image_image_6 = PhotoImage(file=relative_to_assets("rectanguloNegroPerfil.png"))
        self.canvas.create_image(881.0, 376.0, image=self.image_image_6)

        self.canvas.create_text(453.0, 362.0, anchor="nw", text="Sesion 1", fill="#FFFFFF", font=("Roboto", 22 * -1))
        self.canvas.create_text(654.0, 359.0, anchor="nw", text="xx:xx", fill="#FFFFFF", font=("Roboto", 22 * -1))
        self.canvas.create_text(848.0, 359.0, anchor="nw", text="xx:xx", fill="#FFFFFF", font=("Roboto", 22 * -1))

        self.image_image_7 = PhotoImage(file=relative_to_assets("Reloj.png"))
        self.canvas.create_image(772.0, 309.0, image=self.image_image_7)

        self.image_image_8 = PhotoImage(file=relative_to_assets("Reloj.png"))
        self.canvas.create_image(955.0, 309.0, image=self.image_image_8)

        self.canvas.create_text(611.0, 297.0, anchor="nw", text="Hora de Inicio", fill="#000000", font=("Inter", 20 * -1))
        self.canvas.create_text(820.0, 297.0, anchor="nw", text="Hora de fin", fill="#000000", font=("Inter", 20 * -1))

        self.image_image_9 = PhotoImage(file=relative_to_assets("Juego.png"))
        self.canvas.create_image(1094.0, 371.0, image=self.image_image_9)

    def setup_buttons(self):
        self.button_image_1 = PhotoImage(file=relative_to_assets("Perfil.png"))
        self.button_1 = Button(image=self.button_image_1, borderwidth=0, highlightthickness=0, command=self.generate_image, relief="flat")
        self.button_1.place(x=81.0, y=349.0, width=183.9990234375, height=59.13140869140625)

        self.button_image_2 = PhotoImage(file=relative_to_assets("Entrenar.png"))
        self.button_2 = Button(image=self.button_image_2, borderwidth=0, highlightthickness=0, command= self.switch_callback, relief="flat")
        self.button_2.place(x=81.0, y=428.0, width=183.9990234375, height=59.13140869140625)
        
        self.button_image_3 = PhotoImage(file=relative_to_assets("MiEquipo.png"))
        self.button_3 = Button(image=self.button_image_3, borderwidth=0, highlightthickness=0, command=lambda: print("hola"), relief="flat")
        self.button_3.place(x=81.0, y=512.0, width=183.9990234375, height=59.13140869140625)

        self.button_image_4 = PhotoImage(file=relative_to_assets("Apagar.png"))
        self.button_4 = Button(image=self.button_image_4, borderwidth=0, highlightthickness=0, command=lambda: print("button_4 clicked"), relief="flat")
        self.button_4.place(x=142.0, y=912.0, width=60.1756591796875, height=67.20001220703125)

    def generate_image(self):
        base_y_position = 10
        base_x_position = 10
        y_increment = 100
        y_position = base_y_position + (self.image_count * y_increment)
        new_image = PhotoImage(file=relative_to_assets("rectanguloNegroPerfil.png"))
        self.inner_canvas.create_image(base_x_position, y_position, image=new_image, anchor="nw")
        self.image_count += 1
        self.inner_canvas.images.append(new_image)
        self.inner_canvas.bind("<Configure>", self.adjust_inner_canvas_size)

        # Generar nombre de la sesión
        self.inner_canvas.create_text(base_x_position + 100, y_position + 30, text="Sesion " + str(self.sesion), font=("Roboto", 18, "bold"), fill="white")
        self.sesion += 1

        # Generar hora de inicio
        self.inner_canvas.create_text(base_x_position + 300, y_position + 30, text="xx:xx", font=("Roboto", 18, "bold"), fill="white")

        # Generar hora de fin
        self.inner_canvas.create_text(base_x_position + 500, y_position + 30, text="xx:xx", font=("Roboto", 18, "bold"), fill="white")

        # Generar botones
        button_image_6 = PhotoImage(file=relative_to_assets("Detalles.png"))
        button_6 = Button(self.inner_canvas, image=button_image_6, borderwidth=0, highlightthickness=0, relief="flat")
        self.inner_canvas.create_window(830, y_position + 8, anchor="nw", window=button_6, width=154.0, height=46.0)
        self.inner_canvas.images.append(button_image_6)

    def adjust_inner_canvas_size(self, event):
        self.inner_canvas.configure(scrollregion=self.inner_canvas.bbox("all"))

    
if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()