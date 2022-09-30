arch = open("problema1.txt")
line = arch.readline().strip()

cantidad_sucursales = int(line)

total_ventas = 0
sucursal_mas_venta = ""
ventas_de_sucursal_mas_ventas = -999
producto_mas_caro = ""
precio_producto_mas_caro = -999
sucursal_de_venta = ""

for i in range(cantidad_sucursales):
    line = arch.readline().strip()
    partes = line.split(",")

    nombre_producto_caro = ""
    venta_producto_caro = -9999
    ventas_unitarias = 0
    ventas_sucursal = 0


    nombre_sucursal = partes[0]
    cantidad_productos = int(partes[1])

    if cantidad_productos != 0:
        for j in range(cantidad_productos):
            line = arch.readline().strip()
            partes = line.split(",")
            nombre_producto = partes[0]
            cantidad_producto = int(partes[1])
            precio_producto = int(partes[2])
            venta_producto = cantidad_producto * precio_producto

            if venta_producto > venta_producto_caro:
                venta_producto_caro = venta_producto
                nombre_producto_caro = nombre_producto
            
            if cantidad_producto == 1:
                ventas_unitarias += 1
            porcentaje = ventas_unitarias/cantidad_productos
            ventas_sucursal += venta_producto
    
        total_ventas += ventas_sucursal

        if ventas_de_sucursal_mas_ventas < ventas_sucursal:
            ventas_de_sucursal_mas_ventas = ventas_sucursal
            sucursal_mas_ventas = nombre_sucursal
        
        if precio_producto_mas_caro < venta_producto_caro:
            precio_producto_mas_caro = venta_producto_caro
            producto_mas_caro = nombre_producto_caro
            sucursal_de_venta = nombre_sucursal

        print("Producto con mayor venta en sucursal", nombre_sucursal)
        print("es ", nombre_producto_caro, " con un total ", venta_producto_caro)
        print("porcentaje de ventas unitarias es ", porcentaje*100,"%")

print("-"*10)
print("Total de ventas",total_ventas)
print("La sucursal con más ventas es",sucursal_mas_ventas)
print("con total de ventas", ventas_de_sucursal_mas_ventas)
print("El producto más caro fue",producto_mas_caro)
print("vendido en la sucursal",sucursal_de_venta)
print("con un precio de",precio_producto_mas_caro)

