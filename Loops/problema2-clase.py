#Abrimos el archivo
arch = 
#Leemos la primera linea del archivo
line = 

#Preguntamos a que direccion se quiere ir el usuario
direccion = 

#Creamos los parametros iniciales
max = 
nombre_mejor_refugio = 
distancia_mejor_refugio = 
refugios_habitables = 
refugios_no_habitables = 
total_refugios = 

#Creamos un while haste que el usuario indique la palabra fin
while direccion != "fin":
    #Creamos un while para recorrer todo el archivo
    while line != "":
        #Variables del ciclo while
        lista = 
        nombre_refugio =
        distancia =
        capacidad =
        suministros =
        radiacion =
        actividad =
        
        #Actualizamos el contador de refugios
        total_refugios +=

        #Creamos una condicion para encontrar posibles refugios habitables
        if capacidad >= 20 and radiacion == "Protegido":
            factor =
            #Creamos una condicion para encontrar los refugios que son habitables
            if capacidad >= 30:
                refugios_habitables += 
            else:
                refugios_no_habitables += 
            #Creamos una condicio para encontrar el mejor refugio habitable
            if factor > max:
                max = 
                nombre_mejor_refugio = 
                distancia_mejor_refugio = 
        else:
            refugios_no_habitables += 

       
        #Leems la siguiente linea del archivo
        line =

    #Indicamos cuanto falta para llevar al destino con diferentes velocidad
    for velocidad in range(1,42,10):
        tiempo =
        horas = 
        minutos =
        print(horas, minutos, velocidad)

    print(max, nombre_mejor_refugio)
    print(refugios_habitables)
    print(refugios_no_habitables, refugios_no_habitables/total_refugios)
    direccion = input("Ingrese A para Norte o B para Sur: ")
