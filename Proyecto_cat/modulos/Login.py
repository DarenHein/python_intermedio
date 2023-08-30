from modulos.Menu import menu
def login(contraseña):
    if contraseña == "5882" :
        print("acceso permitido")
        menu()
    else :
        print("Acceso denegado")