import os 
def Decoradora(funcion_original):
    def modificar(*args):
        nombre = args[0]
        ruta = os.getcwd()
        extencion = nombre+".txt"
        ruta_completa = os.path.join(ruta,extencion)
        existe = os.path.exists(ruta_completa)
        if existe :
            print("La Tarea que se intenta crear ya existe \ny se enceuntra en la ruta " , ruta_completa)
        else : 
            return funcion_original(*args)
    return modificar
            
@Decoradora
def agregar(*args):
    # args[0] -> nombre de la tarea 
    #args[1] -> que es la tarea 
    #argas[2] -> fecha limite de cumplimiento de la tarea 
    ruta = os.getcwd()
    nombre_archivo = args[0]
    tarea = args[1]
    dia_cumplimiento = args[2]
    acompletar = "Tarea : " + tarea + "\nDia de Vencimiento " + dia_cumplimiento 
    try:
        nota = open(nombre_archivo+".txt" , "a")
        nota.write(acompletar)
        return print("tarea agregada con exito \nAlmacenado en -> " , ruta )
    except FileNotFoundError :
        print("No se puede Guardar la Tarea")
    pass
