'''
    File name: client.py
    Author: Andrea Elías, Diego Estrada & Luis Urbina
    Date created: 10/09/2021
    Python Version: 3.7
'''

import socket
import threading
import pickle

inicioPartida = False

# Variables for game management in a room
CARDNO = 1
CARDATACK = 2
CARDSKIP = 3
CARDFAVOR = 4
CARDSHUFFLE = 5
CARDSEEFUTURE = 6
CARDDEFUSE = 7
CARDBOMB = 8


#!/usr/bin/env python3

# import socket

# HOST = '127.0.0.1'  # The server's hostname or IP address
# PORT = 65432        # The port used by the server

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'Hello, world')
#     data = s.recv(1024)

# print('Received', repr(data))

def send():
    global inicioPartida
    while True:
        print(
            '''
            \nTienes las siguientes opciones
            \n1. Iniciar la partida
            \n2. Enviar Mensaje
            \n3. Realizar Jugada
            \n4. Hacer un Favor
            \n5. Ver estado del juego
            \n6. Ver cartas que tengo
            \n7. Ver lista de jugadores conectados
            \n8. Instrucciones
            '''
        )
        opcion = int(input('\nIngresa el numero de opcion > '))
        if opcion == 1:
            if inicioPartida == False:
                objeto = {
                    'opcion': opcion
                }
                data_string = pickle.dumps(objeto)
                cli_sock.send(data_string) 
            else:
                print('La partida ya fue iniciada.')
        elif opcion == 2:
            if inicioPartida == True:
                msg = input('\nYo > ')
                objeto = {
                    'opcion' : opcion,
                    'mensaje': msg 
                }
                data_string = pickle.dumps(objeto)
                cli_sock.send(data_string)
            else:
                print('La partida aun no ha sido iniciada.')

        elif opcion == 3:
            if inicioPartida == True:
                jugada = int(input('\nElige una jugada: \n1. Usar carta\n2. Tomar carta\n> '))
                if jugada == 1:
                    objeto = {
                        'opcion' : 5
                    }
                    data_string = pickle.dumps(objeto)
                    cli_sock.send(data_string)
                    objeto = {
                        'opcion' : 6
                    }
                    data_string = pickle.dumps(objeto)
                    cli_sock.send(data_string)
                    carta = int(input('\nElige el numero de carta a usar > '))
                    objeto = {
                        'opcion' : 7
                    }
                    data_string = pickle.dumps(objeto)
                    cli_sock.send(data_string)
                    favor = int(input('''
                        \nSi la carta es un favor o un gato elija el numero de Usuario a pedir la carta (si no lo es ingrese cualquier numero)  > 
                    '''))
                    gatos = int(input('''
                        \nSi la carta es un tipo de gato elija una de las siguientes opciones (si no lo es ingrese cualquier numero)
                        \n1. Usar 2 gatos iguales
                        \n2. Usar 3 gatos iguales
                        \n> 
                    '''))
                    cartaPedir = ''
                    if gatos == 1:
                        cartaPedir = int(input('\nIngrese la posicion de la carta quitar (desde posicion 1 al numero de cartas del jugador): '))
                    elif gatos == 2:
                        print('''
                            \n1. Carta NO
                            \n2. Carta ATACK
                            \n3. Carta SKIP
                            \n4. Carta FAVOR
                            \n5. Carta SHUFFLE
                            \n6. Carta SEE FUTURE
                            \n7. Carta DEFUSE
                            \n8. Carta GATO BARBA
                            \n9. Carta GATO ARCOIRIS
                            \n10. Carta GATO SANDIA
                            \n11. Carta GATO TACO
                            \n12. Carta GATO PAPA
                        ''')
                        cartaPedir = int(input('\nIngrese la carta que desea quitar: '))
                    objeto = {
                        'opcion' : opcion,
                        'jugada' : jugada,
                        'carta' : carta,
                        'favor' : favor,
                        'gatos' : gatos,
                        'cartaPedir' : cartaPedir
                    }
                    data_string = pickle.dumps(objeto)
                    cli_sock.send(data_string)
                elif jugada == 2:
                    objeto = {
                        'opcion' : opcion,
                        'jugada' : jugada
                    }
                    data_string = pickle.dumps(objeto)
                    cli_sock.send(data_string)
                else: 
                    print('Opcion invalida.')
            else:
                print('La partida aun no ha sido iniciada.')  

        elif opcion == 4:
            if inicioPartida == True:
                objeto = {
                    'opcion' : 5
                }
                data_string = pickle.dumps(objeto)
                cli_sock.send(data_string)
                carta = int(input('\nElija el numero de carta de su mazo a dar > '))
                objeto = {
                    'opcion' : opcion,
                    'carta' : carta
                }
                data_string = pickle.dumps(objeto)
                cli_sock.send(data_string)
            else:
                print('La partida aun no ha sido iniciada.')    

        elif opcion == 5:
            if inicioPartida == True:
                objeto = {
                    'opcion' : opcion
                }
                data_string = pickle.dumps(objeto)
                cli_sock.send(data_string)
            else:
                print('La partida aun no ha sido iniciada.') 

## Receive messages
def receive():
    global inicioPartida
    while True:
        responseP = cli_sock.recv(4096)
        objeto = pickle.loads(responseP)

        if objeto['header'] == 'chat':
            sen_name = objeto['nombre']
            data_string = objeto['mensaje']

            print('\n' + str(sen_name) + ' > ' + str(data_string))
            print('\n> ')

        if objeto['header'] == 'inicio':
            inicioPartida = True
            print('\nEl juego ha sido iniciado')
            print('\n> ')

        if objeto['header'] == 'fallo':
            mensajeFallo = objeto['mensaje']
            print(mensajeFallo)
            print('\n> ')

        if objeto['header'] == 'turno':
            mensajeTurno = objeto['mensaje']
            print(mensajeTurno)
            print('\n> ')

        if objeto['header'] == 'estado':
            mensajeTurno = objeto['mensaje']
            print(mensajeTurno)
            print('\n> ')

        if objeto['header'] == 'estadoPropio':
            mensajeTurno = objeto['mensaje']
            print(mensajeTurno)
            print('\n> ')

        if objeto['header'] == 'response':
            mensajeTurno = objeto['mensaje']
            print(mensajeTurno)
            print('\n> ')

        if objeto['header'] == 'fuera':
            mensajeTurno = objeto['mensaje']
            print(mensajeTurno)
            print('\n> ')

        if objeto['header'] == 'futuro':
            mensajeTurno = objeto['mensaje']
            print(mensajeTurno)
            print('\n> ')

        if objeto['header'] == 'usoCarta':
            mensajeTurno = objeto['mensaje']
            print(mensajeTurno)
            print('\n> ')

        if objeto['header'] == 'listaJugadores':
            mensajeTurno = objeto['mensaje']
            print(mensajeTurno)
            print('\n> ')

        if objeto['header'] == 'ganar':
            mensajeTurno = objeto['mensaje']
            print(mensajeTurno)
            print('\n> ')

