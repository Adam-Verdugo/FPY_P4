from os import system
from msvcrt import getch

productos = []

def buscarcodigo(codigo : int):
    for i in range(len(productos)):
        if productos[i]["codigo"] == codigo:
            return i
    return -1

def registrarproducto(codigo, nombre, stock, precio):
    if buscarcodigo(codigo) == -1:
        if len(nombre) >= 3 :
            if stock >= 0 :
                if precio > 0:
                    date = {
                        "codigo" : codigo,
                        "nombre" : nombre,
                        "stock" : stock,
                        "precio" : precio
                    }
                    productos.append(date)
                    print("producto registrado con exito")
                else:
                    print("precio debe ser mayor a 0 ")
            else:
                print("stock no valido")
        else:
            print("nombre no valido ")
    else:
        print("codigo ya esta registrado")
    return False

def listarproductos():
    if len(productos) >= 0:
        for i in range(len(productos)):
            if productos[i]["stock"] > 0:
                print(f"{i+1} | codigo : {productos[i]["codigo"]} nombre : {productos[i]["nombre"]} stock : {productos[i]["stock"]} precio : {productos[i]["precio"]} |")
            else:
                print("no se encontro un producto con stock")
    else:
        print("aun no hay ningun producto registrado")




def eliminarproducto(codigo):
    for i in range(len(productos)):
        pass
    if len(productos) >= 0:
        if productos[i]["codigo"] == codigo:
            del productos[i]
            print("producto eliminado con exito")
        else:
            print("no se encontro producto con ese codigo")
    else:
        print("no codigo registrados")

def pausa():
    print("presione para continuar")
    getch()
    system("cls")
