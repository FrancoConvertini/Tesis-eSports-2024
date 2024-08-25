from tkinter import Tk, Canvas, PhotoImage, Button, Label
from ClassEntrenamiento import ReconocimientoFacialApp


def get_analysis_results(self):
        # Simular resultados del análisis
        results = {
            'total_sessions': 10,
            'average_duration': '1h 30m',
            'max_duration': '2h 15m',
            'min_duration': '45m'
        }
        return results

class ClassResultado:
    def __init__(self, root):
        self.root = root
        self.root.title("Resultados del Análisis de Entrenamiento")
        self.canvas = Canvas(root, width=800, height=600)
        self.canvas.pack()

        self.entrenamiento = ReconocimientoFacialApp(root, contador=0)
        self.generate_results_page()

    def generate_results_page(self):
        results = self.entrenamiento.get_analysis_results()

        # Mostrar resultados en la página
        self.canvas.create_text(400, 50, text="Resultados del Análisis de Entrenamiento", font=("Roboto", 24, "bold"), fill="black")

        y_position = 150
        for key, value in results.items():
            self.canvas.create_text(400, y_position, text=f"{key.replace('_', ' ').capitalize()}: {value}", font=("Roboto", 18), fill="black")
            y_position += 50

if __name__ == "__main__":
    root = Tk()
    app = ClassResultado(root)
    root.mainloop()