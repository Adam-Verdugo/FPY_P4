from funciones import *


while True:
    pausa()
    print("""
        -----------------------------
        menu de compra
        1) Registrar producto
        2) Listar producto por stock
        3) eliminar producto por el codigo
        4) salir
        -----------------------------""")
    
    seleccion = int(input("que opcion quiere seleccionar : "))

    match seleccion:
        case 1:
            codigo = int(input("ingrese el codigo de su producto : "))
            nombre = str(input("ingrese el nombre de su producto : "))
            stock = int(input("ingrese la cantidad de stock de su producto : "))
            precio = int(input("ingrese el precio de su producto : "))
            registrarproducto(codigo, nombre, stock, precio)
        case 2:
            listarproductos()
        case 3:
            codigo = int(input("ingrese el codigo que quiere eliminar : "))
            eliminarproducto(codigo)
        case 4:
            break
        case _:
            print("opcion no valida")

