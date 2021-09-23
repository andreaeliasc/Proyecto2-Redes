MENU = '''
            Tienes las siguientes opciones\n
            1. Iniciar la partida
            2. Enviar Mensaje
            3. Realizar Jugada
            4. Hacer un Favor
            5. Ver estado del juego
            6. Ver cartas que tengo
            7. Ver lista de jugadores conectados
            8. Instrucciones
'''

INSTRUCCIONES = '''
    /\_____/\\
   /  o   o  \\           ,--.!,
  ( ==  ^  == )        __/   -*-
   )         (       ,d  b.  '|`
  (           )     (      )     
 ( (  )   (  ) )     `9__P'
(__(__)___(__)__)

¡Bienvenido a Exploding Kittens!\n
El objetivo del juego es ir tomando cartas del mazo y evitar sacar las cartas 
de bomba para no salir de la partida. Además de tomar cartas, tienes una serie 
de cartas para poder usar estrategicamente y ser el ultimo en pie en la partida.

Al inicio la unica opcion que se tiene es la 1, pero una vez usada esta
opcion e inciada la partida se podrán usar el resto.

Tienes las siguientes opciones:
1. Iniciar la partida
Con esta opcion podemos inciar una partida, siempre que hayan 3 a 5
jugadores en la sala. En caso no se cumpla esta condicion
se le notifica a los usuarios el intento fallido de iniciar partida.

2. Enviar Mensaje
Con esta opcion se puede mandar un mensaje a todos los usuarios de la partida.

3. Realizar Jugada
Con esta opcion podemos tener 2 opciones al hacer la jugada que son: Usar una carta, 
y tomar una carta. A partir de las acciones que se tomen el juego ira transcurriendo.

4. Hacer un Favor
Con esta opcion podemos dar una carta a otro jugador en caso nos lo hayan impuesto.

5. Ver estado del juego
Con esta opcion podemos ver el estado del juego, el cual es la informacion publica 
sobre cuantas cartas hay en el mazo restantes y cuantas tiene cada jugador en su 
propio mazo.

6. Ver cartas que tengo
Esta opcion permite ver las cartas que tienes en tu mazo

7. Ver lista de jugadores conectados
Esta opcion permite ver la lista de jugadores conectados en la sala

8. Instrucciones
Nos muestra estas instrucciones en pantalla

~ ~ CARTAS Y SUS USOS ~ ~

    CARTA DE NO
Esta carta permite saltar el turno de quien la usa, ósea no tomar carta, y darle 2 
turnos al siguiente jugador. No es acumulable los turnos si se lanzan en cadena.

    CARTA ATACK
Esta carta permite saltarse el turno, ósea no tomar carta y pasar el turno al 
siguiente jugador.

    CARTA SKIP
Esta carta permite solicitar una carta a un usuario específico, y la carta es 
la que decida el jugador al que se le solicitó el favor.

    CARTA SHUFFLE
Esta carta mezcla las cartas que están en el mazo.

    CARTA SEE THE FUTURE
Esta carta le muestra al jugador las próximas 3 cartas que vienen en el mazo,
y regresarlas en el mismo orden después de verlas.

    CARTA DEFUSE
Esta carta permite desactivar la bomba si esta le sale a un jugador. Si se intenta
usar la carta de manera independiente, se muestra un error de que esta carta no se 
puede jugar, y se devuelve al jugador.

    CARTA TIPO GATO
Esta carta permite al jugador robar cartas de otro jugador a su elección si se tienen
2 o 3 iguales de un mismo tipo de gato. Si se tienen 2 iguales y se usan, estas salen 
de la mano del usuario y este escoge una carta de su elección con respecto a posición 
en el mazo sin saber cual es y la roba. Si se elige usar 3 cartas iguales entonces se 
roba una carta especifica que pida el jugador que va a robar. En caso la tenga el 
adversario, se roba, y en caso no la tenga pues el jugador que quería robar pierde
sus 3 cartas. Si se usa la carta y no se tienen 2 o 3 iguales muestra un mensaje de 
error y pide repetir el turno.
'''