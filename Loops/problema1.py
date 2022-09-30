arch = open('problema1.txt')
line = arch.readline().strip()

cant_sucursal = int(line)

total_ventas_sucursal = 0
sucursal_mas_ventas = ""
valor_mas_ventas = -11111
producto_mas_caro = ""
precio_mas_caro = -1111
sucursal_de_venta = ""

for i in range(cant_sucursal):
    line = arch.readline().strip()
    lista = line.split(",")

    prod_caro = ""
    ventas = 0
    max = -11111
    total_venta = 0
    ventas_unitarias = 0
    sucursal = lista[0]
    total_productos = int(lista[1])

    if total_productos != 0:
        for i in range(int(lista[1])):
            line =arch.readline().strip()
            lista = line.split(",")
            ventas = int(lista[1])*int(lista[2])
            total_venta += ventas
            if max < ventas:
                max = ventas
                prod_caro = lista[0]
            if int(lista[1]) == 1:
                ventas_unitarias += 1
            porcentaje = ventas_unitarias/total_productos

        
        total_ventas_sucursal += total_venta
        
        if total_venta>valor_mas_ventas:
            valor_mas_ventas=total_venta
            sucursal_mas_ventas=sucursal
        if precio_mas_caro<max:
            producto_mas_caro=prod_caro
            sucursal_de_venta=sucursal
            precio_mas_caro=max

        print("Producto con mayor venta en sucursal", sucursal)
        print("es ", prod_caro, " con un total ", max)
        print("porcentaje de ventas unitarias es ", porcentaje*100,"%")

print("-"*10)
print("Total de ventas",total_ventas_sucursal)
print(sucursal_mas_ventas)
print("La sucursal con más ventas es",valor_mas_ventas)
print("con total de ventas",producto_mas_caro)
print("El producto más caro fue",sucursal_de_venta)
print("con un precio de",precio_mas_caro)
