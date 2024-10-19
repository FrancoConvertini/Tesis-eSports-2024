from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Scrollbar
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class CoachApp:

    def __init__(self, root, userLogeado, userPerfil):
        self.root = root
        self.root.geometry("1440x1024")
        self.root.configure(bg="#FFFFFF")
        self.root.resizable(False, False)
        self.image_count = 0
        self.userLogeado = userLogeado
        self.userPerfil = userPerfil
        print("en class coach antes de ir a perfil con userLogeado: ", userLogeado, " y userPerfil: ", userPerfil)
        self.setup_ui()
        self.generate_image(userLogeado)

    def get_session_data(self, userLogeado):
        
        cnx = mysql.connector.connect(
            #host="database-1.cluster-c8t9myimiwmo.us-east-1.rds.amazonaws.com",
            #user="admin",
            #passwd="asdasd123",
            #database="tesis2024",
            host="localhost",
            user="root",
            passwd="1234",
            database="tesis2024",
            auth_plugin='mysql_native_password'
        )
        cursor2 = cnx.cursor()
        cursor3 = cnx.cursor()
        # Ejecutar la consulta
        idUser = userLogeado
        query_equipo = "SELECT equipo FROM users WHERE idUsers = %s"
        cursor2.execute(query_equipo, (idUser,))
        resultado = cursor2.fetchone()
        equipos = resultado[0]
        print(equipos)
        query_users= "SELECT idUsers FROM users WHERE equipo = %s"
        cursor3.execute(query_users, (equipos,))
        rows = cursor3.fetchall()
        session_data = []
        for row in rows:
            session_data.append({
                    'idUsers': row[0],
                })
            
        return session_data 

    def switch_to_perfil(self, session, userLogeado, userPerfil):
        from ClassPerfil import PerfilApp
        print("en class coach dentro de switch_to_perfil con userLogeado: ", userLogeado, " y userPerfil: ", userPerfil)
        userPerfil = session['idUsers']
        self.root.destroy()
        new_root = Tk()
        PerfilApp(new_root, userLogeado, userPerfil)
        new_root.mainloop()
    

    def generate_image(self, userLogeado):
        idUser = userLogeado
        session_data = self.get_session_data(idUser)
        
        # Lista para almacenar las referencias a las imágenes y botones
        self.image_references = []
        self.button_references = []

        # Posición inicial y espaciado entre imágenes
        base_y_position = 400  # Ajusta según el layout
        base_y_position2 = 333
        y_increment = 100  # Espacio entre las imágenes

        for index, session in enumerate(session_data):
            # La posición Y se incrementa para cada imagen
            y_position = base_y_position + (index * y_increment)
            y_position2 = base_y_position2 + (index * y_increment)

            # Generar la imagen en la posición adecuada
            image = PhotoImage(file=relative_to_assets("RectanguloNegroPerfil.png"))
            self.canvas.create_image(873.0, y_position, image=image)

            # Agregar la imagen a la lista para que no desaparezca
            self.image_references.append(image)

            # Generar el texto sobre la imagen
            self.canvas.create_text(873.0, y_position - 5, text=f"{session['idUsers']}", fill="white", font=("Roboto", 16, "bold"))

            # Crear el botón "Detalles" para cada imagen
            button_image = PhotoImage(file=relative_to_assets("Detalles.png"))
            button = Button(self.root, image=button_image, borderwidth=0, highlightthickness=0, command=lambda s=session: self.switch_to_perfil(s, self.userLogeado, self.userPerfil), relief="flat")
            button.place(x=1192, y=y_position2 + 40, width=154.0, height=46.0)  # Ajusta la posición y tamaño del botón

            # Guardar la referencia del botón y su imagen
            self.button_references.append(button_image)
            self.button_references.append(button)

    def show_details(self, session):
        # Aquí puedes definir la lógica para mostrar los detalles de la sesión
        print(f"Mostrando detalles para el usuario: {session['idUsers']}")


    def setup_ui(self):
        

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
        self.image_image_1 = PhotoImage(file=relative_to_assets("Fondo.png"))
        self.canvas.create_image(720.0, 512.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=relative_to_assets("MenuIzq.png"))
        self.canvas.create_image(172.0, 512.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=relative_to_assets("CuadradoMedio.png"))
        self.canvas.create_image(872.0, 512.0, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=relative_to_assets("logo.png"))
        self.canvas.create_image(173.0, 162.0, image=self.image_image_4)


        self.image_image_13 = PhotoImage(file=relative_to_assets("Team.png"))
        self.canvas.create_image(489.0, 146.0, image=self.image_image_13)

        self.canvas.create_rectangle(
            383.0,
            287.0,
            1359.9999389648438,
            290.0123710033819,
            fill="#000000",
            outline=""
        )

        
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

        self.button_image_6 = PhotoImage(file=relative_to_assets("MiEquipo.png"))
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
