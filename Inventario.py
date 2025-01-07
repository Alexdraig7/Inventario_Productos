Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00, 5:240.00}
Stock = {1:50, 2:45, 3:30, 4:15, 5:23}

def agregar(producto, precio, stock):
    #Obtenemos todas las claves.
    items = list(Productos.keys())
    #Obtenemos la ultima clave y le sumamos uno.
    item = items[-1] + 1
    #Agregamos el nuevo Producto.
    Productos[item] = producto
    Precios[item] = precio
    Stock[item] = stock
    return "====> Producto "+producto+" agregado."

def eliminar(producto):
    #Buscamos la clave del diccionario segun el valor (Producto) ingresado.
    clave = list(Productos.keys())[list(Productos.values()).index(producto)]
    #Eliminamos el producto indicado.
    del Productos[clave]
    #Creamos una lista provisional para guardar los valores del diccionario Producto.
    list_productos = list(Productos.values())
    #Limpiamos el diccionario Productos
    Productos.clear()
    #Creamos nuevamente el diccionario Productos con las claves ordenadas y completas (1,2,3,...).
    i = 1
    for prod in list_productos:
        Productos[i] = prod
        i=i+1

    del Precios[clave]
    list_precios = list(Precios.values())
    Precios.clear()
    i = 1
    for prec in list_precios:
        Precios[i] = prec
        i=i+1
    
    del Stock[clave]
    list_stk = list(Stock.values())
    Stock.clear()
    i = 1
    for stk in list_stk:
        Stock[i] = stk
        i=i+1
    return "===> Producto "+producto+" eliminado."

def modificar(prod_aux):
    print("========================================")
    print("Ingrese los datos a modificar:")
    producto = input("Nombre del Producto: ")
    #Validamos que el campo precio solo sea un valor numerico positivo.
    valid = True
    while valid is True:
        try:
            precio = float(input("Indique el Precio: "))
            if (precio < 0):
                print('El valor debe ser mayor a 0.')
            else:
                valid = False
        except:
            print('Debe ingresar un dato numérico.')
    #Validamos que el campo stock solo sea un valor entero positivo.
    valid = True
    while valid is True:
        try:
            stock = int(input("Indique el Stock: "))
            if (stock < 0):
                print('El valor debe ser mayor a 0.')
            else:
                valid = False
        except:
                print('Debe ingresar un dato entero.')
    clave = list(Productos.keys())[list(Productos.values()).index(prod_aux)]
    Productos[clave] = producto
    Precios[clave] = precio
    Stock[clave] = stock
    return "===> Producto "+prod_aux+" modificado."

while True:
    print('========================================')
    print('Lista de Productos:')
    print('========================================')
    for i in Productos:
        print(f"{str(i).ljust(5)} {Productos[i].ljust(15)} {str(Precios[i]).ljust(10)} {str(Stock[i]).ljust(5)}")
    print('========================================')
    print('[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir')
    opcion = input("Elija opción: ")
    if opcion == "1":
        print('========================================')
        print('Agregar Producto:')
        print('========================================')
        producto = input("Nombre del Producto: ")
        #Con el metodo capitelize hacemos que el producto inicie con mayuscula y lo demas sea minuscula para evitar problemas con ese estandar.
        producto = producto.capitalize()
        valid = True
        while valid is True:
            try:
                precio = float(input("Indique el Precio: "))
                if (precio < 0):
                    print('El valor debe ser mayor a 0.')
                else:
                    valid = False
            except:
                print('Debe ingresar un dato numérico.')
        
        valid = True
        while valid is True:
            try:
                stock = int(input("Indique el Stock: "))
                if (stock < 0):
                    print('El valor debe ser mayor a 0.')
                else:
                    valid = False
            except:
                print('Debe ingresar un dato entero.')

        mensaje = agregar(producto, precio, stock)
        print(mensaje)
        print("")
        
    elif opcion == "2":
        print('========================================')
        print('Eliminar Producto:')
        print('========================================')
        valid = True
        while valid is True:
            try:
                producto = input("Indique el nombre del Producto: ")
                producto = producto.capitalize()
                mensaje = eliminar(producto)
                print(mensaje)
                print("")
                valid = False
            except:
                print('El Producto no es válido.')
    
    elif opcion == "3":
        print('========================================')
        print('Modificar Producto:')
        print('========================================')
        valid = True
        while valid is True:
            try:
                prod_aux = input("Indique el nombre del Producto: ")
                prod_aux = prod_aux.capitalize()
                mensaje = eliminar(prod_aux)
                print(mensaje)
                print("")
                valid = False
            except:
                print('El Producto no es válido.')
        
    elif opcion == "4":
        print("¡Gracias por su visita!")
        break
    else:
        print("La opcion no es válida, intente nuevamente")