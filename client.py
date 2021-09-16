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