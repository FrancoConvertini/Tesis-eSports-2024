import tkinter as tk
from tkinter import ttk, messagebox, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Frame, Label, Scrollbar
import mysql.connector
from pathlib import Path
import cv2
from PIL import Image, ImageTk
import time
import os

# Path helper function
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_db_connection():
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
        print(f"Error de conexión a la base de datos: {err}")
        return None

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("e-Motion Application")
        self.geometry("1440x1024")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.current_frame = None

        self.create_frames()
        self.show_frame("LoginFrame")
        
        print("MainApplication initialized")
        print(f"Frames created: {list(self.frames.keys())}")
        print(f"Current frame: {self.current_frame}")

    def create_frames(self):
        for F in (LoginFrame, CoachFrame, FacialRecognitionFrame, ProfileFrame):
            frame = F(self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.grid_remove()  # Hide all frames initially
            print(f"Frame {F.__name__} created and gridded")

    def show_frame(self, frame_name, user_logged=None, user_profile=None):
        print(f"Attempting to show frame: {frame_name}")
        if self.current_frame:
            self.current_frame.grid_remove()
        
        frame = self.frames[frame_name]
        if hasattr(frame, 'refresh'):
            frame.refresh(user_logged, user_profile)
        frame.grid()
        self.current_frame = frame
        print(f"Frame {frame_name} is now visible")
        self.update()  # Force an update to ensure the frame is displayed

class LoginFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.cnx = create_db_connection()
        print("LoginFrame initialized")
        self.setup_ui()
        self.grid(row=0, column=0, sticky="nsew")
    def setup_ui(self):
        print("Setting up LoginFrame UI")
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        print("Canvas created and placed")
        self.canvas.create_text(
            720, 512,
            text="Login Frame",
            fill="black",
            font=("Helvetica", 24)
        )
        print("Text added to canvas")
        try:
            self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
            self.canvas.create_image(1110.96, 512.0, image=self.image_image_1)
        except tk.TclError as e:
            print(f"Error loading image_1.png: {e}")

        try:
            self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
            self.canvas.create_image(1162.0, 455.0, image=self.entry_image_1)
        except tk.TclError as e:
            print(f"Error loading entry_1.png: {e}")
        
        self.entry_1 = Entry(self, bd=0, bg="#AEA4B0", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=998.0, y=428.0, width=328.0, height=52.0)

        try:
            self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
            self.canvas.create_image(1162.0, 539.0, image=self.entry_image_2)
        except tk.TclError as e:
            print(f"Error loading entry_2.png: {e}")

        self.entry_2 = Entry(self, bd=0, bg="#AEA5B0", fg="#000716", highlightthickness=0, show="*")
        self.entry_2.place(x=998.0, y=512.0, width=328.0, height=52.0)

        try:
            self.button_image_1 = PhotoImage(file=relative_to_assets("ingresar.png"))
            self.button_1 = Button(
                self,
                image=self.button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=self.validar_login,
                relief="flat"
            )
            self.button_1.place(x=982.0, y=588.0, width=360.0, height=48.09)
        except tk.TclError as e:
            print(f"Error loading ingresar.png: {e}")

        try:
            self.image_image_2 = PhotoImage(file=relative_to_assets("logo.png"))
            self.canvas.create_image(1161.0, 300.0, image=self.image_image_2)
        except tk.TclError as e:
            print(f"Error loading logo.png: {e}")

        try:
            self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
            self.canvas.create_image(427.0, 512.0, image=self.image_image_3)
        except tk.TclError as e:
            print(f"Error loading image_3.png: {e}")

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
        print("LoginFrame UI setup complete")

    def validar_login(self):
        user = self.entry_1.get()
        password = self.entry_2.get()

        if self.cnx is None:
            messagebox.showerror("Error de conexión", "No se pudo conectar a la base de datos")
            return

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
        rol = resultado[4] if resultado else None

        if rol == "Player":
            self.master.show_frame("ProfileFrame", user, user)
        elif rol == "Coach":
            self.master.show_frame("CoachFrame", user, user)
        else:
            messagebox.showerror("Error", "Rol de usuario no reconocido")

    def refresh(self, user_logged=None, user_profile=None):
        print("LoginFrame UI setup complete")
        self.entry_1.delete(0, tk.END)
        self.entry_2.delete(0, tk.END)

class CoachFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.userLogeado = None
        self.userPerfil = None
        self.image_count = 0
        self.setup_ui()

    def setup_ui(self):
        self.canvas = Canvas(
            self,
            bg="#E3E3E3",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.image_image_1 = PhotoImage(file=relative_to_assets("Fondo.png"))
        self.canvas.create_image(720.0, 512.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=relative_to_assets("MenuIzq.png"))
        self.canvas.create_image(172.0, 512.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=relative_to_assets("CuadradoMedio.png"))
        self.canvas.create_image(872.0, 512.0, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=relative_to_assets("Ojo.png"))
        self.canvas.create_image(173.0, 110.0, image=self.image_image_4)

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

        self.button_image_6 = PhotoImage(file=relative_to_assets("MiEquipo.png"))
        self.button_6 = Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_6_click,
            relief="flat"
        )
        self.button_6.place(x=80.0, y=351.0, width=183.999, height=59.131)

    def on_button_6_click(self):
        print("button_6 clicked")

    def get_session_data(self, userLogeado):
        cnx = create_db_connection()
        cursor = cnx.cursor()
        query_equipo = "SELECT equipo FROM users WHERE idUsers = %s"
        cursor.execute(query_equipo, (userLogeado,))
        equipos = cursor.fetchone()[0]
        
        query_users = "SELECT idUsers FROM users WHERE equipo = %s"
        cursor.execute(query_users, (equipos,))
        rows = cursor.fetchall()
        
        session_data = [{'idUsers': row[0]} for row in rows]
        cursor.close()
        cnx.close()
        return session_data

    def switch_to_perfil(self, session, userLogeado, userPerfil):
        userPerfil = session['idUsers']
        self.master.show_frame("ProfileFrame", userLogeado, userPerfil)

    def refresh(self, user_logged, user_profile):
        self.userLogeado = user_logged
        self.userPerfil = user_profile
        self.generate_image(user_logged)

    def generate_image(self, userLogeado):
        session_data = self.get_session_data(userLogeado)
        
        self.image_references = []
        self.button_references = []

        base_y_position = 400
        base_y_position2 = 333
        y_increment = 100

        for index, session in enumerate(session_data):
            y_position = base_y_position + (index * y_increment)
            y_position2 = base_y_position2 + (index * y_increment)

            image = PhotoImage(file=relative_to_assets("RectanguloNegro.png"))
            self.canvas.create_image(873.0, y_position, image=image)
            self.image_references.append(image)

            self.canvas.create_text(873.0, y_position - 30, text=f"Usuario: {session['idUsers']}", fill="white", font=("Roboto", 18, "bold"))

            button_image = PhotoImage(file=relative_to_assets("Detalles.png"))
            button = Button(
                self,
                image=button_image,
                borderwidth=0,
                highlightthickness=0,
                command=lambda s=session: self.switch_to_perfil(s, self.userLogeado, self.userPerfil),
                relief="flat"
            )
            button.place(x=1192, y=y_position2 + 40, width=154.0, height=46.0)

            self.button_references.append(button_image)
            self.button_references.append(button)

class FacialRecognitionFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.userLogeado = None
        self.userPerfil = None
        self.cronometro_activo = False
        self.tiempo_inicial = 0
        self.contador = 0
        self.setup_ui()
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def setup_ui(self):
        self.canvas = Canvas(
            self,
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
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.toggle_cronometro,
            relief="flat"
        )
        self.button_1.place(x=820.0, y=826.0, width=105.0, height=112.0)
        
        self.canvas.create_rectangle(42.0, 27.0, 304.0, 998.0, fill="#E3E3E3", outline="")
        
        self.image_image_2 = PhotoImage(file=relative_to_assets("Ojo.png"))
        self.canvas.create_image(174.0, 162.0, image=self.image_image_2)

        self.button_image_2 = PhotoImage(file=relative_to_assets("Perfil.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.abrir_perfil(self.userLogeado, self.userPerfil),
            relief="flat"
        )
        self.button_2.place(x=82.0, y=349.0, width=183.9990234375, height=59.13140869140625)

        self.button_image_3 = PhotoImage(file=relative_to_assets("Entrenar.png"))
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(x=82.0, y=428.0, width=183.9990234375, height=59.13140869140625)

        self.button_image_5 = PhotoImage(file=relative_to_assets("Apagar.png"))
        self.button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(x=143.0, y=912.0, width=60.1756591796875, height=67.20001220703125)

        self.label_camara = Label(self)
        self.label_camara.place(x=366, y=50)

        self.id_texto_cronometro = self.canvas.create_text(758.0, 673.0, anchor="nw", text="00:00", fill="#000000", font=("Inter", 96 * -1))

    def abrir_perfil(self, userLogeado, userPerfil):
        self.master.show_frame("ProfileFrame", userLogeado, userPerfil)

    def toggle_cronometro(self):
        if self.cronometro_activo:
            self.cronometro_activo = False
            self.contador += 1
            duracion = self.duracion()
            self.hora_final = time.strftime("%H:%M:%S", time.localtime())
            cnx = create_db_connection()
            cursor = cnx.cursor()
            query = "INSERT INTO entrenamientos (idUsers, duracion, hora_inicio, hora_final) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (self.userLogeado, duracion, self.hora_inicio, self.hora_final))
            cnx.commit()
            cursor.close()
            cnx.close()
        else:
            self.cronometro_activo = True
            self.tiempo_inicial = int(time.time())
            self.hora_inicio = time.strftime("%H:%M:%S", time.localtime())
            self.actualizar_cronometro()
            self.mostrar_camara()

    def duracion(self):
        tiempo_actual = int(time.time())
        duracion = tiempo_actual - self.tiempo_inicial
        return duracion

    def actualizar_cronometro(self):
        if self.cronometro_activo:
            tiempo_actual = int(time.time())
            tiempo_transcurrido = tiempo_actual - self.tiempo_inicial
            minutos, segundos = divmod(tiempo_transcurrido, 60)
            tiempo_str = f"{minutos:02d}:{segundos:02d}"
            self.canvas.itemconfig(self.id_texto_cronometro, text=tiempo_str)
            self.after(1000, self.actualizar_cronometro)

    def mostrar_camara(self):
        _, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame, (1014, 604))
        img = Image.fromarray(frame_resized)
        imgtk = ImageTk.PhotoImage(image=img)
        self.label_camara.imgtk = imgtk
        self.label_camara.configure(image=imgtk)
        if self.cronometro_activo:
            self.label_camara.after(10, self.mostrar_camara)

    def refresh(self, user_logged, user_profile):
        self.userLogeado = user_logged
        self.userPerfil = user_profile

class ProfileFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.userLogeado = None
        self.userPerfil = None
        self.image_count = 0
        self.sesion = 1
        self.show_button_3 = True
        self.setup_ui()

    def setup_ui(self):
        self.main_frame = Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.frame_sesion = Frame(self, bg="#2E0935")
        self.frame_sesion.place(x=381, y=338, width=1005, height=633)

        self.canvas = Canvas(
            self.main_frame,
            bg="#2E0935",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge",
            scrollregion=(0, 0, 0, 1024)
        )
        self.canvas.place(x=0, y=0)

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
        

        self.inner_scrollbar = Scrollbar(self.frame_sesion, orient="vertical", command=self.inner_canvas.yview)
        self.inner_scrollbar.pack(side="right", fill="y")
        self.inner_canvas.configure(yscrollcommand=self.inner_scrollbar.set)
        self.inner_canvas.configure(scrollregion=self.inner_canvas.bbox("all"))

        self.inner_canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.inner_canvas.images = []
        
        self.setup_canvas()
        self.setup_buttons()
        self.canvas.create_text(600, 100, anchor="nw", text="Nombre: ", tags="nombre_text", fill="#000000", font=("Inter", 16 * -1))
        self.canvas.create_text(600, 130, anchor="nw", text="Equipo: ", tags="equipo_text", fill="#000000", font=("Inter", 16 * -1))
        self.canvas.create_text(600, 160, anchor="nw", text="Edad: ", tags="edad_text", fill="#000000", font=("Inter", 16 * -1))
        self.canvas.create_text(600, 190, anchor="nw", text="Videojuego: ", tags="videojuego_text", fill="#000000", font=("Inter", 16 * -1))
        self.canvas.create_text(600, 220, anchor="nw", text="Rol: ", tags="rol_text", fill="#000000", font=("Inter", 16 * -1))

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

        self.image_image_5 = PhotoImage(file=relative_to_assets("logo.png"))
        self.canvas.create_image(173.0, 162.0, image=self.image_image_5)

        self.canvas.create_text(817.0, 41.0, anchor="nw", text="Perfil del jugador", fill="#931668", font=("Inter", 20 * -1))
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
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.on_profile_button_click(),
            relief="flat"
        )
        self.button_1.place(x=81.0, y=349.0, width=183.9990234375, height=59.13140869140625)

        self.button_image_2 = PhotoImage(file=relative_to_assets("Entrenar.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.switch_to_entrenamiento(self.userLogeado, self.userPerfil),
            relief="flat"
        )
        self.button_2.place(x=81.0, y=428.0, width=183.9990234375, height=59.13140869140625)

        if self.show_button_3:
            self.button_image_3 = PhotoImage(file=relative_to_assets("MiEquipo.png"))
            self.button_3 = Button(
                self,
                image=self.button_image_3,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.switch_to_coach(self.userLogeado, self.userPerfil),
                relief="flat"
            )
            self.button_3.place(x=81.0, y=512.0, width=183.9990234375, height=59.13140869140625)

        self.button_image_4 = PhotoImage(file=relative_to_assets("Apagar.png"))
        self.button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(x=142.0, y=912.0, width=60.1756591796875, height=67.20001220703125)

    def on_profile_button_click(self):
        print("Profile button clicked")
        self.refresh(self.userLogeado, self.userPerfil)


    def switch_to_coach(self, userLogeado, userPerfil):
        self.master.show_frame("CoachFrame", userLogeado, userPerfil)

    def switch_to_entrenamiento(self, userLogeado, userPerfil):
        self.master.show_frame("FacialRecognitionFrame", userLogeado, userPerfil)

    def create_button_command(self, session_name):
        return lambda: print(f"Nombre de la sesión: {session_name}")

    def generate_image(self, idUser):
        base_y_position = 10
        base_x_position = 10
        y_increment = 100

        session_data = self.get_session_data(idUser)

        for session in session_data:
            
            y_position = base_y_position + (self.image_count * y_increment)
            new_image = PhotoImage(file=relative_to_assets("rectanguloNegroPerfil.png"))
            self.inner_canvas.create_image(base_x_position, y_position, image=new_image, anchor="nw")
            self.image_count += 1
            self.inner_canvas.images.append(new_image)
            self.inner_canvas.bind("<Configure>", self.adjust_inner_canvas_size)

            session_name = f"Sesion {self.sesion}"
            self.inner_canvas.create_text(base_x_position + 100, y_position + 30, text="Sesion " + str(self.sesion), font=("Roboto", 18, "bold"), fill="white")
            self.sesion += 1

            self.inner_canvas.create_text(base_x_position + 300, y_position + 30, text=session['hora_inicio'], font=("Roboto", 18, "bold"), fill="white")
            self.inner_canvas.create_text(base_x_position + 500, y_position + 30, text=session['hora_fin'], font=("Roboto", 18, "bold"), fill="white")

            button_image_6 = PhotoImage(file=relative_to_assets("Detalles.png"))
            button_6 = Button(
                self.inner_canvas,
                image=button_image_6,
                borderwidth=0,
                highlightthickness=0,
                relief="flat",
                command=self.create_button_command(session_name)
            )
            self.inner_canvas.create_window(830, y_position + 8, anchor="nw", window=button_6, width=154.0, height=46.0)
            self.inner_canvas.images.append(button_image_6)

    def adjust_inner_canvas_size(self, event):
        self.inner_canvas.configure(scrollregion=self.inner_canvas.bbox("all"))

    def get_session_data(self, idUser):
        cnx = create_db_connection()
        cursor = cnx.cursor()
        query_sesion = "SELECT hora_inicio, hora_final, duracion FROM entrenamientos WHERE idUsers = %s"
        cursor.execute(query_sesion, (idUser,))
        rows = cursor.fetchall()
        
        session_data = [
            {
                'hora_inicio': row[0],
                'hora_fin': row[1],
                'duracion': row[2]
            } for row in rows
        ]
        cursor.close()
        cnx.close()
        return session_data

    def refresh(self, user_logged, user_profile):
        self.userLogeado = user_logged
        self.userPerfil = user_profile
        self.fetch_user_data()
        self.generate_image(user_profile)
        self.update_ui()
        

    def fetch_user_data(self):
        cnx = create_db_connection()
        cursor = cnx.cursor()
        query = "SELECT name, equipo, edad, videojuego, rol FROM users WHERE idUsers = %s"
        cursor.execute(query, (self.userLogeado,))
        self.user_data = cursor.fetchone()
        cursor.close()
        cnx.close()

    def update_ui(self):
        if self.user_data:
            self.canvas.itemconfig(self.canvas.find_withtag("nombre_text"), text=f"Nombre: {self.user_data[0]}")
            self.canvas.itemconfig(self.canvas.find_withtag("equipo_text"), text=f"Equipo: {self.user_data[1]}")
            self.canvas.itemconfig(self.canvas.find_withtag("edad_text"), text=f"Edad: {self.user_data[2]}")
            self.canvas.itemconfig(self.canvas.find_withtag("videojuego_text"), text=f"Videojuego: {self.user_data[3]}")
            self.canvas.itemconfig(self.canvas.find_withtag("rol_text"), text=f"Rol: {self.user_data[4]}")

            if self.user_data[4] != "Coach":
                self.button_3.place_forget()
                self.show_button_3 = False
            else:
                self.show_button_3 = True
                self.setup_buttons()
if __name__ == "__main__":
    print(f"Current working directory: {os.getcwd()}")
    print(f"Assets path: {ASSETS_PATH}")
    try:
        app = MainApplication()
        print("MainApplication created successfully")
        app.update()  # Force an update before entering the mainloop
        print("Initial update completed")
        print(f"Current frame after update: {app.current_frame}")
        app.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()