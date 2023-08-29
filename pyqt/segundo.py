import sys
from PyQt6.QtWidgets import QApplication , QMainWindow

def main():
    app = QApplication(sys.argv)
    ventana = QMainWindow()

    ventana.setWindowTitle("mi segunda Ventana")
    ventana.setGeometry(400,200,500,500)
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()