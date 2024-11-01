

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import mysql.connector
from tkinter import messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets login"



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



# Establecer una conexión a la base de datos MySQL
cnx = mysql.connector.connect(
    host="database-1.cluster-c8t9myimiwmo.us-east-1.rds.amazonaws.com",
    user="admin",
    passwd="asdasd123",
    database="tesis2024",
)

# Verificar si la conexión es exitosa
if cnx.is_connected():
    print("Conectado a la base de datos MySQL")

# Función para validar el login
def validar_login():
    user = entry_1.get()
    password = entry_2.get()

    cursor = cnx.cursor()
    query = "SELECT * FROM users WHERE idUsers = %s AND password = %s"
    cursor.execute(query, (user, password))
    resultado = cursor.fetchone()

    if resultado:
        messagebox.showinfo("Login exitoso", "Bienvenido!")
        abrir_perfil(user)

    else:
        messagebox.showerror("Error de login", "Usuario o contraseña incorrectos")

    cursor.close()


def abrir_perfil(user):
    cursor = cnx.cursor()
    idUser = user
    userLogeado = user
    userPerfil = user
    query = "SELECT name, equipo, edad, videojuego, rol FROM users WHERE idUsers = %s"
    cursor.execute(query, (idUser,))
    resultado = cursor.fetchone()
    rol=resultado[4]
    if rol=="Player":
        from ClassPerfil import PerfilApp
        window.destroy()
        new_root = Tk()
        PerfilApp(new_root, userLogeado, userPerfil)
        new_root.mainloop()
    else:
        from ClassCoach import CoachApp
        print("en login abrir coach con userLogeado: ", userLogeado, " y userPerfil: ", userPerfil)
        window.destroy()
        new_root = Tk()
        CoachApp(new_root, userLogeado, userPerfil)
        new_root.mainloop()

def abrir_coach():
    from coachprueba import CoachApp
    window.destroy()
    new_root = Tk()
    CoachApp(new_root)
    new_root.mainloop()



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

#canvas.create_text(
    #1212.0,
    #658.0,
    #anchor="nw",
    #text="Registrate",
    #fill="#2C89F7",
    #font=("Inter", 16 * -1)
#)

#canvas.create_text(
    #1046.0,
    #658.0,
    #anchor="nw",
    #text="No estas registrado?",
    #fill="#313131",
    #font=("Inter", 16 * -1)
#)

image_image_2 = PhotoImage(
    file=relative_to_assets("logo.png"))
image_2 = canvas.create_image(
    1161.0,
    300.0,
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
    120.0,
    342.0,
    anchor="nw",
    text="Cuida tu salud y mejora tu rendimiento",
    fill="#FFFFFF",
    font=("Roboto", 36 * -1)
)
canvas.create_text(
    310.0,
    442.0,
    anchor="nw",
    text="con e-Motion",
    fill="#FFFFFF",
    font=("Roboto", 36 * -1)
)
window.resizable(False, False)
window.mainloop()
