direccion = input("Ingrese A para Norte o B para Sur: ")

while direccion != "fin":
    if direccion.upper() == "A" or direccion.upper() == "B":
        max = -11111
        nombre_mejor_refugio = ""
        distancia_mejor_refugio = 0
        refugios_habitables = 0
        refugios_no_habitables = 0
        total_refugios = 0
        if direccion.upper() == "A":
            arch = open("/Users/agustin/Documents/Clase-python/Loops/A.txt", encoding="utf-8")
        else:
            arch = open("/Users/agustin/Documents/Clase-python/Loops/B.txt", encoding="utf-8")
        line = arch.readline().strip()
        while line != "":
            lista = line.split(",")
            nombre_refugio = lista[0]
            if direccion.upper() == "A":
                distancia = int(lista[1])-200
            else:
                distancia = int(lista[1])+200
            capacidad = int(lista[2])
            suministros = int(lista[3])
            radiacion = lista[4]
            actividad = lista[5]
            
            total_refugios += 1

            if capacidad >= 20 and radiacion == "Protegido":
                factor = (1800/distancia) + ((12*suministros)/90)
                if capacidad >= 30:
                    refugios_habitables += 1
                else:
                    refugios_no_habitables += 1
                if factor > max:
                    max = factor
                    nombre_mejor_refugio = nombre_refugio
                    distancia_mejor_refugio = distancia
            else:
                refugios_no_habitables += 1

        

            line = arch.readline().strip()

        for velocidad in range(1,42,10):
            tiempo = distancia_mejor_refugio/velocidad
            horas = int(tiempo)
            minutos = int((tiempo - int(tiempo))*60)
            print(horas, minutos, velocidad)

        print(max, nombre_mejor_refugio)
        print(refugios_habitables)
        print(refugios_no_habitables, refugios_no_habitables/total_refugios)
        direccion = input("Ingrese A para Norte o B para Sur: ")
    else:
        direccion = input("Error, Ingrese A para Norte o B para sur: ")