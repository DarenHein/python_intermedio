import sys # para interacturar con el interprete de python 
from PyQt6.QtWidgets import QApplication, QMainWindow

#-> PyQt6.QtWidgets importamos de ese modulo QApplication y QMainWindow sirven prar los eventos y el mejo de widgets 

def main(): #-> hacemos una funcion main 
    app = QApplication(sys.argv)
    ventana = QMainWindow()
    ventana.setWindowTitle("Mi primer ventana") #-> titulo de la ventana 
    ventana.setGeometry(400,400,400,400) #-> x,y,ancho,largo
    ventana.show()# -> muestra la ventana 
    sys.exit(app.exec()) #-> asegura que la venatan este abierta hasta que nosotros la cerremos 

if __name__ == "__main__":
    main()
