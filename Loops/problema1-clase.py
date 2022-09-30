#Abrir archivo y leer linea
arch = open('problema1.txt')
line = arch.readline().strip()

#Crear parametros iniciales
cant_sucursal = int(line)
total_ventas_sucursales = 0
valor_max_ventas = -999
producto_mas_caro = ""
precio_mas_caro = -999
sucursal_max_ventas = ""

#Creacion del for loop para entrar a cada sucursal
for i in range(cant_sucursal):
    #Leemos la siguiente linea del archivo
    line = arch.readline().strip()
    #Separamos las lineas por cada coma que tenga
    partes = line.split(",")
    #Creamos las variables del for loop
    prod_caro = "" #nombre del producto mas caro
    ventas = 0 #las ventas de cada producto
    max = -999 #el producto que tuvo mas ventas
    total_venta = 0  #total de ventas de cada sucursal
    ventas_unitarias = 0 #cantidad de ventas unitarias
    sucursal = partes[0] #nombre de sucursal
    total_productos =  int(partes[1]) #total de productos de la sucursal

    #Creamos una condicion en caso que la sucursal tenga productos
    if total_productos != 0:
        #Creamos un for loop para leer cada producto
        for i in range(total_productos):
            #Leemos la siguiente linea del archivo
            line = arch.readline().strip()
            #Separamos la linea con las comas
            partes = line.split(",")
            #indicamos el valor de las ventas multiplicando la cantidad y precio del producto
            nombre_producto = partes[0]
            cantidad_producto = int(partes[1])
            valor_producto = int(partes[2])

            ventas = cantidad_producto * valor_producto
            #Actualizamos la variable total_ventas
            total_venta += ventas
            #Creamos la condicion para encontrar el producto que deja mas utilidades en la sucursal
            if max < ventas:
                max = ventas
                prod_caro = nombre_producto
            #Creamos la condicion para identificar si el producto se ha vendido solo una vez
            if cantidad_producto == 1:
                #Actualizamos el contador de ventas unitarias
                ventas_unitarias += 1
            #Indicamos el porcentaje de ventas unitarias de la sucursal
            porcentaje = ventas_unitarias/total_productos
        
        #Actualizamos la varible de total de ventas de las sucursales
        total_ventas_sucursales += total_venta

        #Creamos la condicion para encontrar la sucursal con mas ventas
        if valor_max_ventas < total_venta:
            valor_max_ventas = total_venta
            sucursal_max_ventas = sucursal
        #Creamos la condicion para encontrar el producto mas caro de todas las sucursales
        if precio_mas_caro < max:
            producto_mas_caro =  prod_caro
            sucursal_de_venta = sucursal
            precio_mas_caro = max

        print("Producto con mayor venta en sucursal", sucursal)
        print("es ", prod_caro, " con un total ", max)
        print("porcentaje de ventas unitarias es ", porcentaje*100,"%")

print("-"*10)
print("Total de ventas",total_ventas_sucursales)
print(sucursal_max_ventas)
print("La sucursal con más ventas es",valor_max_ventas)
print("con total de ventas",producto_mas_caro)
print("El producto más caro fue",sucursal_de_venta)
print("con un precio de",precio_mas_caro)


