

from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Scrollbar, Frame, Label
##import Entrenamiento
##contador = Entrenamiento.contador

# Conectar con la base de datos

import mysql.connector




OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets_perfil"


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

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("1440x1024")
window.configure(bg = "#2E0935")


cursor = cnx.cursor()
idUser = 2 
query = "SELECT name, equipo, edad, videojuego FROM users WHERE idUsers = %s"
cursor.execute(query, (idUser,))
resultado = cursor.fetchone()
nombre = resultado[0]
equipo = resultado[1]
edad = resultado[2]
videojuego = resultado[3]


# Crear un Frame para contener el Canvas y la Scrollbar
main_frame = Frame(window)
main_frame.pack(fill="both", expand=True)


# Crear el frame secundario que será desplazable
frame_sesion = Frame(window, bg="#2E0935")
frame_sesion.place(x=381,y=338, width=1005, height=633)

canvas = Canvas(
    main_frame,
    bg="#2E0935",
    height=1024,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge",
    scrollregion=(0, 0, 0, 1024)  # Ajustar según el contenido
)
canvas.place(x=0, y=0)

# Primero, crea un Canvas dentro de frame_sesion
inner_canvas = Canvas(
    frame_sesion,
    bg="#E3E3E3",
    height=633,
    width=1005,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)                 
inner_canvas.pack(fill="both", expand=True, side="left")  # Ajusta el canvas para que llene frame_sesion


# Crear la Scrollbar y asociarla con el Canvas
inner_scrollbar = Scrollbar(frame_sesion, orient="vertical", command=inner_canvas.yview)
inner_scrollbar.pack(side="right", fill="y")
inner_canvas.configure(yscrollcommand=inner_scrollbar.set)
inner_canvas.configure(scrollregion=inner_canvas.bbox("all")) 


def _on_mousewheel(event):
    inner_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
inner_canvas.bind_all("<MouseWheel>", _on_mousewheel)


# Asegúrate de que inner_canvas tenga una lista para almacenar referencias de imágenes
inner_canvas.images = []

image_count = 0  # Contador para las imágenes generadas

# Ajusta el tamaño del inner_canvas según el contenido
def adjust_inner_canvas_size(event):
    inner_canvas.configure(scrollregion=inner_canvas.bbox("all"))   
    
# Llama a adjust_inner_canvas_size cuando sea necesario, por ejemplo, después de agregar imágenes

sesion= 1


def generate_image():
    global image_count , sesion
    base_y_position = 10  # Posición inicial de Y para image_6
    base_x_position = 10
    y_increment = 100  # Incremento en Y para cada nueva imagen
    y_position =  base_y_position + (image_count * y_increment)  # Calcula la nueva posición en Y
    new_image = PhotoImage(file=relative_to_assets("image_6.png"))  # Asegúrate de tener esta imagen
    # Dibuja la imagen en el inner_canvas en lugar del canvas principal
    inner_canvas.create_image(base_x_position, y_position, image=new_image, anchor="nw")
    image_count += 1
    # Importante: Guardar una referencia de la imagen para evitar que sea recolectada por el recolector de basura
    inner_canvas.images.append(new_image)
    inner_canvas.bind("<Configure>", adjust_inner_canvas_size)

    #Generar nombre de la sesion
    inner_canvas.create_text(base_x_position + 100, y_position + 30,text="Sesion "+str(sesion),font=("Roboto", 18, "bold"),fill="white")
    sesion=int(sesion)
    sesion= sesion+1

    #Generar hora de inicio
    inner_canvas.create_text(base_x_position + 300, y_position + 30,text="xx:xx",font=("Roboto", 18, "bold"),fill="white")

    #Generar hora de fin
    inner_canvas.create_text(base_x_position + 500, y_position + 30,text="xx:xx",font=("Roboto", 18, "bold"),fill="white")

    #Generar botones
    button_image_6 = PhotoImage(file=relative_to_assets("button_5.png"))
    button_6 = Button(inner_canvas, image=button_image_6, borderwidth=0, highlightthickness=0, relief="flat")
    inner_canvas.create_window(830, y_position + 8, anchor="nw", window=button_6, width=154.0, height=46.0)
    inner_canvas.images.append(button_image_6)



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
    867.0,
    512.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    477.0,
    162.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    173.0,
    162.0,
    image=image_image_5
)

canvas.create_text(
    817.0,
    41.0,
    anchor="nw",
    text="Perfil del jugador",
    fill="#931668",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    591.0,
    98.0,
    anchor="nw",
    text=f"Nombre: {nombre}",
    fill="#921568",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    591.0,
    135.0,
    anchor="nw",
    text=f"Edad: {edad}",
    fill="#931668",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    591.0,
    170.0,
    anchor="nw",
    text=f"Videojuego: {videojuego}",
    fill="#931668",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    591.0,
    205.0,
    anchor="nw",
    text=f"Equipo:{equipo}",
    fill="#931668",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    383.0,
    286.0,
    1359.9999389648438,
    289.0123710033819,
    fill="#000000",
    outline="")

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    881.0,
    376.0,
    image=image_image_6
)

canvas.create_text(
    453.0,
    362.0,
    anchor="nw",
    text="Sesion 1",
    fill="#FFFFFF",
    font=("Roboto", 22 * -1)
)

canvas.create_text(
    654.0,
    359.0,
    anchor="nw",
    text="xx:xx",
    fill="#FFFFFF",
    font=("Roboto", 22 * -1)
)

canvas.create_text(
    848.0,
    359.0,
    anchor="nw",
    text="xx:xx",
    fill="#FFFFFF",
    font=("Roboto", 22 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    772.0,
    309.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    955.0,
    309.0,
    image=image_image_8
)

canvas.create_text(
    611.0,
    297.0,
    anchor="nw",
    text="Hora de Inicio",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    820.0,
    297.0,
    anchor="nw",
    text="Hora de fin",
    fill="#000000",
    font=("Inter", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: generate_image(),
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

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    1094.0,
    371.0,
    image=image_image_9
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

##canvas.create_text(
    ##680.0,
    ##98.0,
    ##anchor="nw",
    ##text="Franco Convertini",
    ##fill="#000000",
    ##font=("Inter", 20 * -1)
##)

##canvas.create_text(
    ##654.0,
    ##135.0,
    ##anchor="nw",
    ##text="24",
    ##fill="#000000",
    ##font=("Inter", 20 * -1)
##)

##canvas.create_text(
    ##715.0,
    ##170.0,
    ##anchor="nw",
    ##text="League of Legends",
    ##fill="#000000",
    ##font=("Inter", 20 * -1)
##)

##canvas.create_text(
    ##673.0,
    ##205.0,
    ##anchor="nw",
    ##text="9z",
    ##fill="#000000",
    ##font=("Inter", 20 * -1)
##)


# button_image_5 = PhotoImage(
#     file=relative_to_assets("button_5.png"))
# button_5 = Button(
#     image=button_image_5,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_5 clicked"),
#     relief="flat"
# )
# button_5.place(
#     x=1206.0,
#     y=348.0,
#     width=154.0,
#     height=46.0
# )

i=0
##for i in range (contador):
    ##generate_image()
    ##print(f"Iteración {i+1}")

window.resizable(False, False)
window.mainloop()
