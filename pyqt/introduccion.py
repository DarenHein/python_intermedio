import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

def main():
    # Crea una instancia de QApplication
    app = QApplication(sys.argv)

    # Crea una ventana principal
    ventana = QMainWindow()
    ventana.setWindowTitle("Mi Primer Ventana")
    ventana.setGeometry(100, 100, 400, 300)  # Posición (x, y) y tamaño (ancho, alto)

    # Muestra la ventana
    ventana.show()

    # Inicia el ciclo de eventos de la aplicación
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
