import juegoSopaDeLetras
import sys

var = True
k = True
tamagnio = raw_input("Tamaño de tablero:") 
while var:
    nroJugadores= raw_input("Numero de jugadores:")
    try:
        prueba = juegoSopaDeLetras.SopaDeLetras(nroJugadores,tamagnio)
        if int(prueba.nroJugadores) > 0 and  int(prueba.nroJugadores) < 3:
            var = False
    except juegoSopaDeLetras.ExcepcionJuego , e:
       print e
       
try:
    archivo= open("palabras.txt", "r")
except IOError , e:
        print "No se puede leer el archivo"
        sys.exit(0)
try:    
        prueba.getTablero()
except juegoSopaDeLetras.ExcepcionJuego , e:
        print e
try:
    prueba.cargarPalabras(archivo)
    try:    
        prueba.getTablero()
    except juegoSopaDeLetras.ExcepcionJuego , e:
        print e

    while k:
        try:
            nroJugador = raw_input("Ingrese el numero de jugador: ")
            if nroJugador not in ['1','2']:
                raise juegoSopaDeLetras.ExcepcionJuego("El juegador "+nroJugador+" no puede jugar") 
            palabra = raw_input("Ingrese la palabra: ")
            posInicio = raw_input("Ingrese la posicion inicial: ")
            posFin = raw_input("Ingrese la posicion final: ")
            valor = prueba.ingresarPalabra(nroJugador,posInicio,posFin,palabra)
            if int(valor) != 0:
                k = False
        except juegoSopaDeLetras.ExcepcionJuego , e:
            print e
    archivo.close()
except juegoSopaDeLetras.ExcepcionJuego , e:
    print e
    


