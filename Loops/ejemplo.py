arch = open("problema1.txt")
linea = arch.readline().strip()
linea = arch.readline().strip()
partes = linea.split(",")
nombre_sucursal = partes[0]
cantidad_productos = int(partes[1])

total_ventas = 57

for i in range(5):
    linea = arch.readline().strip()
    partes = linea.split(",")
    nombre_producto = partes[0]
    cantidad_producto = int(partes[1])
    valor_producto = int(partes[2])
    ventas_producto = cantidad_producto * valor_producto
    
    total_ventas = total_ventas + 1
print(total_ventas)