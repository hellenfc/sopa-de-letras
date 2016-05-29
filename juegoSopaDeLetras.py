# -*- coding: cp1252 -*-
import random
import copy
class SopaDeLetras(object):
	def __init__(self, nroJugadores, tamagnio):
		self.nroJugadores= nroJugadores
		self.tamagnio= tamagnio
		self.tablero = []
		self.lineas = []
		self.palabras = []
		self.J1Puntaje = 0
		self.J2Puntaje = 0
		self.palabraEncontrada = []
                if int(self.nroJugadores) > 0 and int(self.nroJugadores) < 3:
                       print " "                           
                else:
                        raise ExcepcionJuego("El juego es de 1 o 2 jugadores.")
                        
        

	def cargarPalabras(self, archivo):
                
                self.archivo=archivo
                linea = []
                for j in range(int(self.tamagnio)):
                        linea.append(" ")
                for i in range(int(self.tamagnio)):
                        self.tablero.append(copy.deepcopy(linea))
                self.lineas = archivo.readlines()
                for i in self.lineas:
                        if i != self.lineas[-1]:
                                i = i[:-1]
                        self.palabras.append(i)
                        linea1= i.split(", ")                       
                        palabra = linea1[0]
                        if len(palabra) > int(self.tamagnio):
                                raise ExcepcionJuego("El Tama�o de la sopa de letras es insuficiente para almacenar las palabras")
                        pos_ini_fil = int(linea1[1])
                        pos_ini_col = int(linea1[2])
                        pos_fin_fil = int(linea1[3])
                        pos_fin_col = int(linea1[4])
                        if pos_ini_col == pos_fin_col:
                                #print "es vertical"
                                k = 0
                                for i in range(pos_ini_fil - 1,pos_fin_fil ):
                                        l = self.tablero[i]
                                        l[pos_ini_col - 1] = palabra[k]
                                        k = k + 1
                        if pos_ini_fil == pos_fin_fil:
                                #Horizontal
                                #print "es horizontal"
                                l = self.tablero[pos_ini_fil - 1]
                                k = pos_ini_col - 1
                                for i in palabra:
                                        l[k] = i
                                        k = k + 1
                        if pos_ini_fil != pos_fin_fil and pos_ini_col != pos_fin_col:
                                #Diagonal 1
                                if pos_ini_fil < pos_fin_fil and pos_ini_col < pos_fin_col:
                                        k = 0
                                        pos_col = pos_ini_col - 1
                                        for i in range(pos_ini_fil - 1,pos_fin_fil):
                                            l = self.tablero[i]
                                            l[pos_col] = palabra[k]
                                            k = k + 1
                                            pos_col = pos_col + 1
                                #Diagonal 2
                                if pos_ini_fil > pos_fin_fil and pos_ini_col > pos_fin_col:
                                        li = palabra[::-1]
                                        k = 0
                                        pos_col = pos_fin_col - 1
                                        for i in range(pos_fin_fil - 1,pos_ini_fil):
                                            l = self.tablero[i]
                                            l[pos_col] = li[k]
                                            k = k + 1
                                            pos_col = pos_col + 1
                                #Diagonal 3
                                if pos_ini_fil > pos_fin_fil and pos_ini_col < pos_fin_col:
                                        k = 0
                                        pos_col = pos_ini_col - 1
                                        pos_fil = pos_ini_fil - 1
                                        while k != int(len(palabra)):
                                                l = self.tablero[pos_fil]
                                                l[pos_col] = palabra[k]
                                                pos_fil = pos_fil - 1
                                                pos_col = pos_col + 1
                                                k = k + 1
                                #Diagonal 4
                                if pos_ini_fil < pos_fin_fil and pos_ini_col > pos_fin_col:
                                        li = palabra[::-1]
                                        k = 0
                                        pos_col = pos_fin_col - 1
                                        pos_fil = pos_fin_fil - 1
                                        while k != int(len(palabra)):
                                                l = self.tablero[pos_fil]
                                                l[pos_col] = li[k]
                                                pos_fil = pos_fil - 1
                                                pos_col = pos_col + 1
                                                k = k + 1
                                             
                        
                                
                
		'''
		Lee todos las palabras que de un archivo el formato del archivo es el
		siguiente:
			<palabra1>, <pos-fila-ini>, <pos-col-ini>, <pos-fila-fin>, <pos-col-fin>
			<palabra2>, <pos-fila-ini>, <pos-col-ini>, <pos-fila-fin>, <pos-col-fin>
		Por ejemplo un archivo podría contener tres palabras:
			hola, 1, 2, 1, 4
			adios, 1, 1, 5, 1
			hello 1, 2, 5, 5
		Y debería de generar una sopa de letras como la siguiente:

		+---+---+---+---+---+---+
		| a | h | o | l | a |   |
		+---+---+---+---+---+---+
		| d |   | e |   | a |   |
		+---+---+---+---+---+---+
		| i |   |   | l |   |   |
		+---+---+---+---+---+---+
		| o |   |   |   | l |   |
		+---+---+---+---+---+---+
		| s |   |   |   |   | o |
		+---+---+---+---+---+---+
		|   |   |   |   |   |   |
		+---+---+---+---+---+---+


		Las posiciones en el archivo se representan del 1 en adelante.
		El resto de las posiciones del arreglo se llenan con letras al azar.

		Parametros
		archivo: se envía solamente el nombre del archivo ej.: "palabras.txt " 
				 se asume que dicho archivo está ubicado en el mismo directorio 
				 donde se ubica el módulo.

		Retorna
		Por razones de revisión, este método retorna una lista con las palabras
		leídas del archivo.

		Excepciones
		ExcepcionJuego "No se puedo leer el archivo".
		ExcepcionJuego "El tamaño de la sopa de letras es insuficiente para 
						almacenar las palabras".
		'''
		pass

	def getTablero(self):
                if self.tablero == [] :
                        raise ExcepcionJuego("No se han cargado las palabras.")
                
                letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
                a = 0
                esp=0
                for i in range(int(self.tamagnio)):
                        l = self.tablero[i]
                        a = 0
                        for j in l:
                                if j == " ":
                                        l[a] = random.choice(letras)
                                        esp=esp + 1                                                       
                                a = a + 1
                        
        
                k = 0
                while k != int(self.tamagnio):
                        for i in range(int(self.tamagnio)):
                                print "+---+",
                        print ""
                        l = self.tablero[k]
                        for j in l:
                                print "| "+j+" |",
                        print ""
                        k = k + 1
                for i in range(int(self.tamagnio)):
                        print "+---+",
                print ""
                
		'''
		Retorna
		El tablero lleno como una lista que contiene listas, cada lista interna 
		representa una fila del tablero.

		Excepciones
		ExcepcionJuego "No se ha cargado las palabras", en el caso de que se
			intente llamar a este método sin haber llamado primero 
			al método cargarPalabras.

		'''
		pass

	def ingresarPalabra(self, nroJugador, posInicio, posFin, palabra):
                self.nroJugador = nroJugador
                self.posInicio = posInicio.strip()
                self.posFin = posFin.strip()
                self.palabra = palabra.strip()
                

                if int(self.nroJugadores) == 1:
                        if int(nroJugador) != 1:
                                raise ExcepcionJuego("El juegador "+nroJugador+" no puede jugar")

                if int(self.nroJugadores) == 2:
                        if int(nroJugador) not in [1,2]:
                                raise ExcepcionJuego("El juegador "+nroJugador+" no puede jugar")
                        
                tup = palabra+", "+posInicio[:1]+", "+posInicio[2]+", "+posFin[:1]+", "+posFin[2]
                juegoTerminado = 0
                numPal = len(self.palabras)
                palultima=self.palabras[numPal-1].strip()
                nuevaLista=[]
                for i in self.palabras:
                        nuevaLista.append(i)
                del nuevaLista[numPal-1]
                nuevaLista.append(palultima)                
                if tup in nuevaLista:
                        if tup not in self.palabraEncontrada:
                                self.palabraEncontrada.append(tup)
                                if int(nroJugador) == 1:
                                        self.J1Puntaje = self.J1Puntaje + 1
                                        print "Punto para el jugador 1."
                                elif int(nroJugador) == 2:
                                        self.J2Puntaje = self.J2Puntaje + 1
                                        print "Punto para el jugador 2."
                                                                      
                        else:
                                raise ExcepcionJuego("La palabra ingresada ya ha sido seleccionada.")
                else:
                        raise ExcepcionJuego("Palabra no encotrada.")
                 
                self.getPuntajesJugadores()
                
                juegoTerminado = int(self.J1Puntaje) + int(self.J2Puntaje)  
                if int(juegoTerminado) == len(nuevaLista):
                        if self.J1Puntaje > self.J2Puntaje:
                                return 1
                        elif self.J1Puntaje < self.J2Puntaje:
                                return 2
                        elif self.J1Puntaje == self.J2Puntaje:
                                return -1
                else:
                        return 0
                
                

		'''
		Parámetros
		nroJugador: número del jugador que está indicando una palabra.
		posInicio: es una tupla que tiene dos enteros con la posicion inicial
			de la palabra en la sopa de letras.

		Excepciones	
		ExcepcionJuego "El juego es de un sólo jugador el jugador 2 no puede 
						jugar", en caso que no coincida con el número de 
						jugadores del juego.
		ExcepcionJuego "No se encontró la palabra en la posicion indicada",
						en caso de posInicio o posFin sean incorrectas o que
						la palabra no esté en dichas posiciones.
		ExcepcionJuego "La palabra ingresada ya había sido seleccionada".
		ExcepcionJuego "No se ha cargado las palabras", en el caso de que se
						intente llamar a este método sin haber llamado primero 
						al método cargarPalabras.

		Retorna
		Un número de entero indicando el jugador ganador, el ganador será el 
		jugador con mayor puntaje al momento de ingresar la última palabra, si
		la actual no es la última palabra se retorna 0, indicando que todavía no
		hay un ganador.
		'''
		pass

	def getPuntajesJugadores(self):
                print "Puntaje"
                print "Jugador 1 = ", self.J1Puntaje, " ","Jugador 2 = ", self.J2Puntaje
		'''
		Retorna
		Una tupla con los puntajes de los jugadores en las posiciones 
		correspondientes ej.: (3,0) indica que al momento el jugador 1 ha 
		encontrado 3 palabras y el jugador 2 ninguna.
		'''
		pass


                
                

class ExcepcionJuego(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return "Error " + str(self.valor)
	
