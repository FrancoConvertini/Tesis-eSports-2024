

from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets coach"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#E3E3E3",
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

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    872.0,
    512.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    173.0,
    110.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    873.0,
    642.0,
    image=image_image_5
)

canvas.create_text(
    459.0,
    626.0,
    anchor="nw",
    text="Jugador 4\n\n",
    fill="#FFFFFF",
    font=("Roboto", 22 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    419.0,
    643.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    873.0,
    555.0,
    image=image_image_7
)

canvas.create_text(
    459.0,
    539.0,
    anchor="nw",
    text="Jugador 3\n",
    fill="#FFFFFF",
    font=("Roboto", 22 * -1)
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    419.0,
    556.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    873.0,
    468.0,
    image=image_image_9
)

canvas.create_text(
    459.0,
    452.0,
    anchor="nw",
    text="Jugador 2\n",
    fill="#FFFFFF",
    font=("Roboto", 22 * -1)
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    419.0,
    469.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    873.0,
    381.0,
    image=image_image_11
)

canvas.create_text(
    459.0,
    365.0,
    anchor="nw",
    text="Jugador 1\n",
    fill="#FFFFFF",
    font=("Roboto", 22 * -1)
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    419.0,
    382.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    489.0,
    146.0,
    image=image_image_13
)

canvas.create_rectangle(
    383.0,
    287.0,
    1359.9999389648438,
    290.0123710033819,
    fill="#000000",
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
    x=1192.0,
    y=614.0,
    width=154.0,
    height=46.0
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    873.0,
    729.0,
    image=image_image_14
)

canvas.create_text(
    459.0,
    713.0,
    anchor="nw",
    text="Jugador 5\n\n\n",
    fill="#FFFFFF",
    font=("Roboto", 22 * -1)
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    419.0,
    730.0,
    image=image_image_15
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
    x=1192.0,
    y=701.0,
    width=154.0,
    height=46.0
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
    x=1192.0,
    y=527.0,
    width=154.0,
    height=46.0
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
    x=1192.0,
    y=440.0,
    width=154.0,
    height=46.0
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
    x=1192.0,
    y=353.0,
    width=154.0,
    height=46.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=80.0,
    y=351.0,
    width=183.9990234375,
    height=59.13140869140625
)

canvas.create_text(
    807.0,
    155.0,
    anchor="nw",
    text="Equipo",
    fill="#931668",
    font=("Inter Bold", 40 * -1)
)
window.resizable(False, False)
window.mainloop()
