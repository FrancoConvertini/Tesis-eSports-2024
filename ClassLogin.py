from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import mysql.connector


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        self.cnx = self.connect_db()

    def setup_ui(self):
        self.root.geometry("1440x1024")
        self.root.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.root,
            bg="#FFFFFF",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(1110.96, 512.0, image=self.image_image_1)

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(1162.0, 455.0, image=self.entry_image_1)
        
        self.entry_1 = Entry(self.root, bd=0, bg="#AEA4B0", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=998.0, y=428.0, width=328.0, height=52.0)

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.canvas.create_image(1162.0, 539.0, image=self.entry_image_2)

        self.entry_2 = Entry(self.root, bd=0, bg="#AEA5B0", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=998.0, y=512.0, width=328.0, height=52.0)

        self.button_image_1 = PhotoImage(file=self.relative_to_assets("ingresar.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.validar_login,
            relief="flat"
        )
        self.button_1.place(x=982.0, y=588.0, width=360.0, height=48.09)

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("logo.png"))
        self.canvas.create_image(1161.0, 300.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.canvas.create_image(427.0, 512.0, image=self.image_image_3)

        self.canvas.create_text(
            120.0,
            342.0,
            anchor="nw",
            text="Cuida tu salud y mejora tu rendimiento",
            fill="#FFFFFF",
            font=("Roboto", 36 * -1)
        )
        self.canvas.create_text(
            310.0,
            442.0,
            anchor="nw",
            text="con e-Motion",
            fill="#FFFFFF",
            font=("Roboto", 36 * -1)
        )

        self.root.resizable(False, False)

    @staticmethod
    def relative_to_assets(path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / "assets"
        return ASSETS_PATH / Path(path)

    @staticmethod
    def connect_db():
        try:
            cnx = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="tesis2024",
                auth_plugin='mysql_native_password'
            )
            if cnx.is_connected():
                print("Conectado a la base de datos AWS MySQL")
            return cnx
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def validar_login(self):
        user = self.entry_1.get()
        password = self.entry_2.get()

        cursor = self.cnx.cursor()
        query = "SELECT * FROM users WHERE idUsers = %s AND password = %s"
        cursor.execute(query, (user, password))
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showinfo("Login exitoso", "Bienvenido!")
            self.abrir_perfil(user)
        else:
            messagebox.showerror("Error de login", "Usuario o contraseña incorrectos")

        cursor.close()

    def abrir_perfil(self, user):
        cursor = self.cnx.cursor()
        query = "SELECT name, equipo, edad, videojuego, rol FROM users WHERE idUsers = %s"
        cursor.execute(query, (user,))
        resultado = cursor.fetchone()
        rol = resultado[4]

        if rol == "Player":
            from ClassPerfil import PerfilApp
            self.root.destroy()
            new_root = Tk()
            PerfilApp(new_root, user, user)
            new_root.mainloop()
        else:
            from ClassCoach import CoachApp
            self.root.destroy()
            new_root = Tk()
            CoachApp(new_root, user, user)
            new_root.mainloop()


if __name__ == "__main__":
    window = Tk()
    app = LoginApp(window)
    window.mainloop()
