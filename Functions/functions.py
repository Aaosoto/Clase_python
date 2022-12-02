def revisar(numeros, sorteados):
    c = 0
    for i in numeros:
        for j in sorteados:
            if i == j:
                c+=1
    return c

def millonario(aciertos, sorteados,juego):
    if aciertos == sorteados:
        print('Felicidades ha ganado el ',juego,', es millonario')
    else:
        print('Usted obtuvo ',aciertos,' aciertos.')

jugar = 'si'
while jugar != 'no':
    #Leemos el archivo del jugador
    juego = input('¿Qué juego desea revisar?: ').lower()
    juegos = ['kino','kino5','loto']

    #Control de error para que solo se ingresen juegos permitidos
    if juego not in juegos:
        while juego not in juegos:
            juego = input('¿Qué juego desea revisar?: ').lower()

    arch = open(juego+'.txt')

    #Leemos el archivo de los sorteados
    arch_sorteado = open('sorteados.txt')
    line_sort = arch_sorteado.readline().strip()
    partes = line_sort.split(',')

    #Buscar juego en archivo sorteados.txt
    while partes[0] != juego:
        line_sort = arch_sorteado.readline().strip()
        partes = line_sort.split(',')

    #Leemos los numeros sorteados del juego
    numeros_sort = list()
    for i in range(int(partes[1])):
        line_sort = arch_sorteado.readline().strip()
        partes = line_sort.split(',')
        numeros_sort.append(int(partes[0]))

    #Leemos los numeros del jugador
    numeros = list()
    line = arch.readline().strip()
    while line != "":
        numeros.append(int(line))
        line = arch.readline().strip()
    
    #Revisar numeros
    aciertos = revisar(numeros,numeros_sort)
    millonario(aciertos,len(numeros_sort),juego)
    

    #Control de error para que solo indique si o no
    opciones = ['si','no']
    jugar = input('¿Desea revisar otro juego? (Si - No): ').lower()
    if jugar not in opciones:
        while jugar not in opciones:
            print('Opción inválida')
            jugar = input('¿Desea revisar otro juego? (Si - No): ').lower()