from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets coach"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class CoachApp:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x1024")
        self.root.configure(bg="#FFFFFF")
        self.root.resizable(False, False)

        self.setup_ui()

    def setup_ui(self):
        # Creación del Canvas
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

        # Configurar las imágenes
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.canvas.create_image(720.0, 512.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.canvas.create_image(172.0, 512.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.canvas.create_image(872.0, 512.0, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        self.canvas.create_image(173.0, 110.0, image=self.image_image_4)

        self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        self.canvas.create_image(873.0, 642.0, image=self.image_image_5)

        self.canvas.create_text(
            459.0,
            626.0,
            anchor="nw",
            text="Jugador 4\n\n",
            fill="#FFFFFF",
            font=("Roboto", 22 * -1)
        )

        self.image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        self.canvas.create_image(419.0, 643.0, image=self.image_image_6)

        self.image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        self.canvas.create_image(873.0, 555.0, image=self.image_image_7)

        self.canvas.create_text(
            459.0,
            539.0,
            anchor="nw",
            text="Jugador 3\n",
            fill="#FFFFFF",
            font=("Roboto", 22 * -1)
        )

        self.image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
        self.canvas.create_image(419.0, 556.0, image=self.image_image_8)

        self.image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
        self.canvas.create_image(873.0, 468.0, image=self.image_image_9)

        self.canvas.create_text(
            459.0,
            452.0,
            anchor="nw",
            text="Jugador 2\n",
            fill="#FFFFFF",
            font=("Roboto", 22 * -1)
        )

        self.image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
        self.canvas.create_image(419.0, 469.0, image=self.image_image_10)

        self.image_image_11 = PhotoImage(file=relative_to_assets("image_11.png"))
        self.canvas.create_image(873.0, 381.0, image=self.image_image_11)

        self.canvas.create_text(
            459.0,
            365.0,
            anchor="nw",
            text="Jugador 1\n",
            fill="#FFFFFF",
            font=("Roboto", 22 * -1)
        )

        self.image_image_12 = PhotoImage(file=relative_to_assets("image_12.png"))
        self.canvas.create_image(419.0, 382.0, image=self.image_image_12)

        self.image_image_13 = PhotoImage(file=relative_to_assets("image_13.png"))
        self.canvas.create_image(489.0, 146.0, image=self.image_image_13)

        self.canvas.create_rectangle(
            383.0,
            287.0,
            1359.9999389648438,
            290.0123710033819,
            fill="#000000",
            outline=""
        )

        self.image_image_14 = PhotoImage(file=relative_to_assets("image_14.png"))
        self.canvas.create_image(873.0, 729.0, image=self.image_image_14)

        self.canvas.create_text(
            459.0,
            713.0,
            anchor="nw",
            text="Jugador 5\n\n\n",
            fill="#FFFFFF",
            font=("Roboto", 22 * -1)
        )

        self.image_image_15 = PhotoImage(file=relative_to_assets("image_15.png"))
        self.canvas.create_image(419.0, 730.0, image=self.image_image_15)

        self.canvas.create_text(
            807.0,
            155.0,
            anchor="nw",
            text="Equipo",
            fill="#931668",
            font=("Inter Bold", 40 * -1)
        )

        # Crear botones
        self.setup_buttons()

    def setup_buttons(self):
        # Crear los botones con comandos
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_1_click,
            relief="flat"
        )
        self.button_1.place(x=1192.0, y=614.0, width=154.0, height=46.0)

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_2_click,
            relief="flat"
        )
        self.button_2.place(x=1192.0, y=701.0, width=154.0, height=46.0)

        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_3_click,
            relief="flat"
        )
        self.button_3.place(x=1192.0, y=527.0, width=154.0, height=46.0)

        self.button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_4_click,
            relief="flat"
        )
        self.button_4.place(x=1192.0, y=440.0, width=154.0, height=46.0)

        self.button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_5_click,
            relief="flat"
        )
        self.button_5.place(x=1192.0, y=353.0, width=154.0, height=46.0)

        self.button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_6_click,
            relief="flat"
        )
        self.button_6.place(x=80.0, y=351.0, width=183.999, height=59.131)

    # Definir acciones de los botones
    def on_button_1_click(self):
        print("button_1 clicked")

    def on_button_2_click(self):
        print("button_2 clicked")

    def on_button_3_click(self):
        print("button_3 clicked")

    def on_button_4_click(self):
        print("button_4 clicked")

    def on_button_5_click(self):
        print("button_5 clicked")

    def on_button_6_click(self):
        print("button_6 clicked")


if __name__ == "__main__":
    root = Tk()
    app = CoachApp(root)
    root.mainloop()
