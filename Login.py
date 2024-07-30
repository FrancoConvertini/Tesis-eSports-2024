# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import mysql.connector
from tkinter import messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Test TK\build\assets\frame0")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



# Establecer una conexión a la base de datos MySQL
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="tesis2024",
    auth_plugin='mysql_native_password'
)

# Verificar si la conexión es exitosa
if cnx.is_connected():
    print("Conectado a la base de datos MySQL")

# Función para validar el login
def validar_login():
    user = entry_1.get()
    password = entry_2.get()

    cursor = cnx.cursor()
    query = "SELECT * FROM users WHERE user = %s AND password = %s"
    cursor.execute(query, (user, password))
    resultado = cursor.fetchone()

    if resultado:
        messagebox.showinfo("Login exitoso", "Bienvenido!")
    else:
        messagebox.showerror("Error de login", "Usuario o contraseña incorrectos")

    cursor.close()



window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
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
    1110.9613037109375,
    512.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1162.0,
    455.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#AEA4B0",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=998.0,
    y=428.0,
    width=328.0,
    height=52.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1162.0,
    539.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#AEA5B0",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=998.0,
    y=512.0,
    width=328.0,
    height=52.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=validar_login,
    relief="flat"
)
button_1.place(
    x=982.0,
    y=588.0,
    width=360.0,
    height=48.09337615966797
)

canvas.create_text(
    1212.0,
    658.0,
    anchor="nw",
    text="Registrate",
    fill="#2C89F7",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    1046.0,
    658.0,
    anchor="nw",
    text="No estas registrado?",
    fill="#313131",
    font=("Inter", 16 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1161.0,
    351.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    427.0,
    512.0,
    image=image_image_3
)

canvas.create_text(
    166.0,
    342.0,
    anchor="nw",
    text="Pajeate Mejor con e-Motion",
    fill="#FFFFFF",
    font=("Roboto", 36 * -1)
)
window.resizable(False, False)
window.mainloop()
