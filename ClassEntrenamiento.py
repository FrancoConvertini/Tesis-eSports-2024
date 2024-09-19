from pathlib import Path
import subprocess
from tkinter import Label, Tk, Canvas, Button, PhotoImage
import cv2  # Add this line to import the cv2 module
from PIL import Image, ImageTk
import time
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"

# Establecer una conexión a la base de datos MySQL
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





def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ReconocimientoFacialApp:
    def __init__(self, root, userLogeado, userPerfil):
        self.root = root
        self.root.geometry("1440x1024")
        self.root.configure(bg="#2E0935")
        self.root.resizable(False, False)
        self.userLogeado = userLogeado
        self.userPerfil = userPerfil
        self.cronometro_activo = False
        self.tiempo_inicial = 0
        self.contador = 0
        self.user = "maspi@gmail.com"
        

        self.setup_ui()
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    def setup_ui(self):
        self.canvas = Canvas(
            self.root,
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
        self.button_1 = Button(image=self.button_image_1, borderwidth=0, highlightthickness=0, command=self.toggle_cronometro, relief="flat")
        self.button_1.place(x=820.0, y=826.0, width=105.0, height=112.0)
        
        self.canvas.create_rectangle(42.0, 27.0, 304.0, 998.0, fill="#E3E3E3", outline="")
        
        self.image_image_2 = PhotoImage(file=relative_to_assets("Ojo.png"))
        self.canvas.create_image(174.0, 162.0, image=self.image_image_2)

        self.button_image_2 = PhotoImage(file=relative_to_assets("Perfil.png"))
        self.button_2 = Button(image=self.button_image_2, borderwidth=0, highlightthickness=0, command=lambda: self.abrir_perfil(self.userLogeado, self.userPerfil), relief="flat")
        self.button_2.place(x=82.0, y=349.0, width=183.9990234375, height=59.13140869140625)

        self.button_image_3 = PhotoImage(file=relative_to_assets("Entrenar.png"))
        self.button_3 = Button(image=self.button_image_3, borderwidth=0, highlightthickness=0, command=lambda: print("button_3 clicked"), relief="flat")
        self.button_3.place(x=82.0, y=428.0, width=183.9990234375, height=59.13140869140625)

        self.button_image_5 = PhotoImage(file=relative_to_assets("Apagar.png"))
        self.button_5 = Button(image=self.button_image_5, borderwidth=0, highlightthickness=0, command=lambda: print("button_5 clicked"), relief="flat")
        self.button_5.place(x=143.0, y=912.0, width=60.1756591796875, height=67.20001220703125)

        self.label_camara = Label(self.root)
        self.label_camara.place(x=366, y=50)  # Ajusta la posición según necesites

        self.id_texto_cronometro = self.canvas.create_text(758.0, 673.0, anchor="nw", text="00:00", fill="#000000", font=("Inter", 96 * -1))

    def abrir_perfil(self, userLogeado, userPerfil):
        from ClassPerfil import PerfilApp
        self.root.destroy()
        new_root = Tk()
        PerfilApp(new_root, userLogeado, userPerfil)
        new_root.mainloop()

    def toggle_cronometro(self):

        if self.cronometro_activo:
            self.cronometro_activo = False
            self.contador += 1
            print(self.contador)
            duracion = self.duracion()
            self.hora_final = time.strftime("%H:%M:%S", time.localtime())
            print(f"Hora final: {self.hora_final}")
            cursor = cnx.cursor()
            query = "INSERT INTO entrenamientos (idUsers ,duracion, hora_inicio, hora_final) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (self.userLogeado, duracion, self.hora_inicio, self.hora_final))
            cnx.commit()
            
        else:
            self.cronometro_activo = True
            self.tiempo_inicial = int(time.time())
            self.hora_inicio = time.strftime("%H:%M:%S", time.localtime())
            print(f"Hora inicio: {self.hora_inicio}")
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
            self.root.after(1000, self.actualizar_cronometro)

    def mostrar_camara(self):
        _, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame, (1014, 604))  # Cambia 320x240 al tamaño deseado
        img = Image.fromarray(frame_resized)
        imgtk = ImageTk.PhotoImage(image=img)
        self.label_camara.imgtk = imgtk
        self.label_camara.configure(image=imgtk)
        if self.cronometro_activo:  # Asegúrate de que la cámara se actualice solo si el cronómetro está activo
            self.label_camara.after(10, self.mostrar_camara)

    

if __name__ == "__main__":
    root = Tk()
    app = ReconocimientoFacialApp(root)
    root.mainloop()
