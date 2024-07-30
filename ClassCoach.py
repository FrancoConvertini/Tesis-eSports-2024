from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

class CoachApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x1024")
        self.root.configure(bg="#FFFFFF")
        self.root.resizable(False, False)

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

if __name__ == "__main__":
    root = Tk()
    app = CoachApp(root)
    root.mainloop()