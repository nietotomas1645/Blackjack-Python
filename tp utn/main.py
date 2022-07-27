"""El Juego del Blackjack [versión 2.0]

En el presente trabajo práctico se pretende replantear la solución aplicada para el juego del Blackjack implementado en el TP1, pero adecuándose a nuevas reglas:

Al inicio del juego se debe solicitar al jugador su nombre y que indique el monto que desea tener de pozo para poder jugar al Blackjack, no pudiendo ser este monto mayor a $100000. Y luego se pide implementar un programa controlado por menú de opciones en el que las opciones sean:

Apostar
Jugar una Mano
Salir

Apostar: En esta opción del menú el jugador puede sumar dinero a su pozo. El valor a sumar no puede ser negativo ni cero. Puede volver a esta opción del menú las veces que quiera.

Jugar una Mano: En esta opción del menú se debe realizar el juego tanto del jugador como del crupier. Inicialmente debe definir el monto a apostar por la mano. Si el jugador no tuviera suficiente dinero para realizar una apuesta, no podrá jugar pero el programa no finaliza porque tiene la opción de apostar en el menú principal. La apuesta debe ser múltiplo de 5 y menor o igual al dinero que posee en su pozo. Las reglas nuevas que aplican en este práctico son (Sin Split ni Rendición, para quienes averigüen del juego):

El jugador recibe dos cartas inicialmente y a partir de ese momento puede seguir pidiendo cartas hasta que decida frenar o bien logre 21 o se pase.
El valor del AS no es fijo. Cuando el jugador o el crupier lo recibe puede sumar 11 mientras no pase de 21. Si siguiera pidiendo cartas y se pasara, el valor del AS vuelve a 1.
El crupier inicialmente recibe una carta que se muestra junto con las dos primeras cartas del jugador. Su juego continúa cuando el jugador termina. Debe pedir cartas mientras tenga 16 o menos de puntaje y plantarse con 17 o más, siendo indefinida la cantidad de cartas hasta lograrlo.
El blackjack natural le gana a un blackjack conseguido con 3 cartas o más.
El ganador de la partida es quien logra 21 o el valor más próximo sin pasarse. Las posibles opciones son:
Gana el jugador: Recibe el doble de su apuesta. (si tenía 10 y apostó 5, queda con 15).
Pierde el jugador: En esta ocasión no pueden perder ambos. Si el jugador pierde y el crupier también, gana el crupier. (si tenía 10 y apostó 5, queda con 5).

Empatan: Si tanto el jugador como el crupier obtienen el mismo puntaje (21 o menos) entonces el jugador recibe su apuesta. (si tenía 10 y apostó 5, queda con 10).
En cada mano se debe mostrar:
Monto inicial del pozo (previo a la apuesta).
Monto de la apuesta.
Cartas de cada jugador y su puntaje final.
Mensaje indicando quién es el ganador.
Monto actualizado del pozo.

Salir: Cuando el usuario elige esta opción se debe mostrar su pozo actualizado y los siguientes resultados:

El porcentaje de victorias del jugador.
La racha más larga de victorias del croupier.
La cantidad de manos donde hubo un blackjack natural
El monto máximo que llegó a tener el jugador en el pozo.
El monto promedio del que dispuso el jugador para realizar apuestas.
La pérdida más grande que sufrió el jugador (si hubo alguna)"""















import random
#Creacion de variables, numeros y palos, JUGADOR Y CRUPIER.
pozo = -1
opc = 0
opc_2 = 0
numeros = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q')
palos = ('De Diamante ♦️♢', 'De Corazones ♥️♡', 'De Pica ♠️♤', 'De Trebol ♣️♧')
crupier = 0
user = 0
jugador_gano = 0
cantidad_partidas = 0
cont_BJN_totales = 0
acum_pozo = 0
mayor_pozo = 0
mayor_perdida = 0
#definicion de funciones
def porcentaje(jugador_gano, cantidad_partidas):
     porcentaje = 100 * int(jugador_gano)/int(cantidad_partidas)
     return str(porcentaje) + "%"



#Inicio del juego
print ("                                                       ##############################################" )
print ("                            BIENVENIDOS AL JUEGO DE BLACKJACK 2.0 PROGRAMADO POR ALUMNOS DE LA UTN -\
 Universidad Tecnologica Nacional")
print ("                                                       ##############################################" )

jugador = input("Ingrese el nombre del jugador: ")
while pozo > 100000 or pozo <= 0:
    pozo = int(input("Indique el monto que desea tener de pozo (NO más de 100000 o menos que 0): "))
    if pozo > 100000 or pozo <= 0:
        print("Error, el pozo no puede ser mayor a 100000 o menor que 0")



#Menu de opciones

while opc != 3: #mientras la opción sea distinta de salir
    print("\nMenú de opciones")
    print("1- Apostar")
    print("2- Jugar una mano")
    print("3- Salir")
    opc = int(input("\nIngrese su opción: "))
    while opc != 1 and opc != 2 and opc != 3:
        print("Opcion invalida.")
        opc = int(input("\nIngrese su opción: "))


#Opcion Apostar (Comprar fichas)
    if opc == 1:
        monto_extra = int(input("Indique el monto a sumar (NO puede ser 0 o negativo)  : "))
        while pozo + monto_extra > 100000 or pozo + monto_extra <= 0 or monto_extra <= 0:
            print("Error! Recuerde que, el pozo no puede ser mayor a 100000 y el monto no puede ser 0 o negativo! ")
            #pozo-=monto_extra
            monto_extra= int(input("\nIndique el monto a sumar: "))
        pozo += monto_extra
        print("\n El pozo actualizado es de: ", pozo)




#Opcion Jugar mano
    if opc == 2:
        crupier=0
        user=0
        cont_BJN_user = 0
        cont_BJN_crupier = 0


        print("\nSu pozo es:", pozo)
        acum_pozo += pozo

        apuesta = int(input("Ingrese apuesta (debe ser multiplo de 5): "))
        while apuesta > pozo or pozo < 5 or apuesta % 5 != 0:
                #print ("No posee saldo disponible para realizar apuesta minima / la apuesta debe ser multiplo de 5!")

            if apuesta % 5 != 0:
                print("\nError! La apuesta debe ser multiplo de 5.")
                apuesta = int(input("Ingrese apuesta (debe ser multiplo de 5): "))
            else:
                if pozo < 5:
                    print("Error! No posee saldo disponible para hacer apuesta minima.")
                    apuesta = int(input("Ingrese apuesta (debe ser multiplo de 5): "))
        if mayor_pozo is None or mayor_pozo < pozo:
            mayor_pozo=pozo
        pozo -= apuesta
        print("\nSu apuesta es de:", apuesta)
#primera jugada crupier
        carta = random.choice(numeros)
        palo= random.choice(palos)
        if carta in ('J', 'K', 'Q'):
            crupier += 10
        elif carta == 'A':
            crupier += 11
        else:
            crupier += carta

        print ("\nLa primera carta que le toco al crupier es:",carta,palo)
        print ("El puntaje del crupier es:",crupier)
        input("Presiona enter para continuar..")
#primera jugada user
        carta = random.choice(numeros)
        palo = random.choice(palos)
        if carta in ('J', 'K', 'Q'):
            user += 10
        elif carta == 'A':
            user += 11
        else:
            user += carta
        print ("\nLa primera carta que le toca a", jugador, "es:",carta,palo)
        print ("El puntaje de",jugador, "es:",user)
        input("Presiona enter para continuar..")
#segunda jugada user
        carta = random.choice(numeros)
        if carta in ('J', 'K', 'Q'):
            user += 10
        elif carta == 'A':
            if user + 11 <= 21:
                user += 11
            else:
                user += 1
        else:
            user += carta
        if user == 21:
            cont_BJN_user +=1

        print ("\nLa segunda carta que le toca a", jugador, "es:",carta,random.choice(palos))
        print ("El puntaje de", jugador, "es:",user)

#tercera jugada user (o cuarta, tenes que ver el ciclo por si necesita seguir pidiendo carta)
        opc_2 = (input("\nIngrese n para plantarse o s para recibir otra carta: "))
        while opc_2 != "s" and opc_2 != "n":
            print("Error! Opcion invalida")
            opc_2 = (input("\nIngrese n para plantarse o s para recibir otra carta: "))
        while opc_2 == "s":
            carta = random.choice(numeros)
            if carta in ('J', 'K', 'Q'):
                user += 10
            elif carta == 'A':
                if user + 11 <= 21:
                    user +=11
                else:
                    user +=1
            else:
                user += carta
            print ("\nLa siguiente carta que le toca a", jugador, "es:",carta,random.choice(palos))
            print ("El puntaje de", jugador, "es:",user)
            opc_2 = (input("\nIngrese n para plantarse o s para recibir otra carta: "))

        if opc_2 == "n":
            print(jugador, "se planta con ", user, "puntos")
        input("Presiona enter para continuar..")
        # segunda jugada crupier
        carta = random.choice(numeros)
        if carta in ('J', 'K', 'Q'):
            crupier += 10
        elif carta == 'A':
            if crupier + 11 <= 21:
                crupier += 11
            else:
                crupier += 1
        else:
            crupier += carta
        if crupier==21:
            cont_BJN_crupier += 1
        if cont_BJN_user + cont_BJN_crupier >= 1:
            cont_BJN_totales += 1
        print("\nLa segunda carta que le toca al crupier es:", carta, random.choice(palos))
        print("El puntaje del crupier es:", crupier)
        input("Presiona enter para continuar..")
        #tercera jugada crupier

        while crupier <= 16:
            carta = random.choice(numeros)
            if carta in ('J', 'K', 'Q'):
                crupier += 10
            elif carta == 'A':
                if crupier + 11 <= 21:
                    crupier += 11
                else:
                    crupier += 1
            else:
                crupier += carta
            print ("\n La siguiente carta que le toca al crupier es:",carta,random.choice(palos))
            print ("El puntaje del crupier es:",crupier)



        #muestra de resultados:

        print ("\n__RESULTADOS")
        if user==crupier and user <= 21 and cont_BJN_user == cont_BJN_crupier:
            print("###################################")
            print ("No hay ganador - hay un empate")
            pozo += apuesta

        elif user==crupier and user==21 and cont_BJN_user > cont_BJN_crupier:
            print("###################################")
            print("El ganador es", jugador, "por tener BJ natural!")
            pozo += apuesta*2
            jugador_gano += 1

        elif user==crupier and user==21 and cont_BJN_user < cont_BJN_crupier:
            print("###################################")
            print("El ganador es el crupier por tener BJ natural!")
            pozo += 0
            if mayor_perdida is None or mayor_perdida < apuesta:
                mayor_perdida = apuesta

        elif user>crupier and user<= 21:
            print("###################################")
            print("El ganador es", jugador, "con", user, "puntos")
            pozo += apuesta*2
            jugador_gano += 1

        elif crupier>user and crupier<= 21:
            print("###################################")
            print ("El ganador es el crupier con", crupier, "puntos")
            pozo += 0
            if mayor_perdida is None or mayor_perdida < apuesta:
                mayor_perdida = apuesta

        elif user < crupier:
            print("###################################")
            print("El ganador es", jugador, "con", user, "puntos")
            pozo += apuesta*2
            jugador_gano+=1
        elif user > 21 and crupier > 21:
            print("###################################")
            print ("No hay ganador - hay un empate")
            pozo += apuesta


        else:
            print("###################################")
            print ("El ganador es el crupier con", crupier, "puntos")
            pozo += 0
            if mayor_perdida is None or mayor_perdida < apuesta:
                mayor_perdida = apuesta


        print("\nSu apuesta fue de:", apuesta)
        print("\nSu pozo actualizado es de:", pozo)
        cantidad_partidas +=1

#monto maximo del pozo
    if mayor_pozo is None or mayor_pozo < pozo:
        mayor_pozo=pozo











    #opcion salir
    if opc == 3:
        print("\n-Su pozo actualizado es de:", pozo)
        if cantidad_partidas == 0:
            print("\n-No se jugaron partidas")
        else:
            if cantidad_partidas != 0 and jugador_gano == 0:
                print("\n-El porcentaje de victorias del jugador fue de: 0%")
            else:
                if cantidad_partidas != 0 and jugador_gano != 0:
                    porcentaje = porcentaje(jugador_gano, cantidad_partidas)
                    print("\n-El porcentaje de victorias de", jugador, "fue de: ", porcentaje)
            if cont_BJN_totales == 0:
                print("\n-No hubieron BJ naturales")
            else:
                print("\n-La cantidad de manos en las que hubo BJ natural fue de:", cont_BJN_totales)
            if acum_pozo != 0:
                promedio_pozo = acum_pozo / cantidad_partidas
                print("\n-El promedio de pozo con el que conto el jugador para apostar fue de:", promedio_pozo)
            if pozo > 0:
                print("\n-El monto maximo que llego a tener el jugador en el pozo fue de:", mayor_pozo)
            if mayor_perdida > 0:
                print("\n-La mayor perdida de", jugador, "fue de: ", mayor_perdida)









