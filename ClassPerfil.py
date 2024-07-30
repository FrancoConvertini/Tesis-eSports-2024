from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Scrollbar, Frame, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class PerfilApp:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x1024")
        self.root.configure(bg="#2E0935")
        self.root.resizable(False, False)
        self.image_count = 0
        self.sesion = 1
        self.partidas=3
        self.contador = 0
       
        self.setup_ui()
        self.entrenamientos()
    def entrenamientos(self):
        i=0
        while i < self.partidas:
            self.generate_image()
            i+=1
            
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
        self.button_2 = Button(image=self.button_image_2, borderwidth=0, highlightthickness=0, command=lambda: self.switch_to_entrenamiento (self.contador), relief="flat")
        self.button_2.place(x=81.0, y=428.0, width=183.9990234375, height=59.13140869140625)

        self.button_image_3 = PhotoImage(file=relative_to_assets("MiEquipo.png"))
        self.button_3 = Button(image=self.button_image_3, borderwidth=0, highlightthickness=0, command=self.sumar, relief="flat")
        self.button_3.place(x=81.0, y=512.0, width=183.9990234375, height=59.13140869140625)

        self.button_image_4 = PhotoImage(file=relative_to_assets("Apagar.png"))
        self.button_4 = Button(image=self.button_image_4, borderwidth=0, highlightthickness=0, command=lambda: print("button_4 clicked"), relief="flat")
        self.button_4.place(x=142.0, y=912.0, width=60.1756591796875, height=67.20001220703125)
    def sumar(self):
        self.contador+=1
        print(self.contador)
        


    def switch_to_entrenamiento(self, contador):
        from ClassEntrenamiento import ReconocimientoFacialApp
        print("entre")
        self.root.destroy()
        new_root = Tk()
        ReconocimientoFacialApp(new_root, contador)
        new_root.mainloop()

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
    app = PerfilApp(root)
    root.mainloop()
