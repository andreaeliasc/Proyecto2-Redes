'''
    File name: server.py
    Author: Andrea Elías, Diego Estrada & Luis Urbina
    Date created: 10/09/2021
    Python Version: 3.7
'''

import socket, os, pickle, threading, random
from operator import itemgetter 

# Variables for rooms and conection management
# HOST = 'localhost'
# PORT = 50001

ROOMS = {}
ROOMScon = {}
startGame = {}
ROOMpiles = {}
ROOMamountDefuses = {}
ROOMpilesPlayers = {}
ROOMSturnPlayers = {}
ROOMSpreviousTurnPlayers = {}
ROOMSpostTurnPlayers = {}
ROOMSplayersAlive = {}
ROOMSusername = {}
giveCard = {}
toGiveCard = {}

# Variables for game management in a room
CARDNO = 1
CARDATACK = 2
CARDSKIP = 3
CARDFAVOR = 4
CARDSHUFFLE = 5
CARDSEEFUTURE = 6
CARDDEFUSE = 7
CARDBOMB = 8
CARDGATOBARBA = 9
CARDGATOARCOIRIS = 10
CARDGATOSANDIA = 11
CARDGATOTACO = 12
CARDGATOPAPA = 13

#!/usr/bin/env python3

# import socket

# HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
# PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)


### Funcion para el manejo y creacion de salas
## Creamos el thread cuando se quiere de la creacion de una sala
def thread_function1(port):
    banner = 0
    RPORT = port
    #print(RPORT)
    r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r.bind((HOST, RPORT))
    print('starting to listen in Room', RPORT)
    ROOMScon[port] = list()
    ROOMSplayersAlive[port] = list()
    ROOMSusername[port] = list()
    ROOMpilesPlayers[port] = {}
    startGame[port] = False
    giveCard[port] = False
    toGiveCard[port] = False
    ROOMpiles[port] = [
        1,1,1,1,1,
        2,2,2,2,
        3,3,3,3,
        4,4,4,4,
        5,5,5,5,
        6,6,6,6,6,
        9,9,9,9,
        10,10,10,10,
        11,11,11,11,
        12,12,12,12,
        13,13,13,13    
    ]
    ROOMamountDefuses[port] = 6
    ROOMSturnPlayers[port] = list()
    ROOMSpreviousTurnPlayers[port] = list()
    ROOMSpostTurnPlayers[port] = list()
    r.listen(5)
    roomThreads = list()
    while (ROOMS[RPORT] < 5):
        #print("In room loop")
        roomCon, temp = r.accept()
        rdata = roomCon.recv(4096)
        username = pickle.loads(rdata)
        #username = "User "+str(ROOMS[RPORT])
        ROOMScon[RPORT].append(roomCon)
        ROOMSusername[RPORT].append(username)
        ROOMSplayersAlive[RPORT].append(roomCon)
        ROOMS
        ROOMS[RPORT] = ROOMS[RPORT] + 1
        ROOMpilesPlayers[RPORT][roomCon] = []
        print ('Connected by ', temp, ' on room', RPORT)
        print(ROOMS)
        thread_client = threading.Thread(target = game, args=[roomCon,RPORT,username])
        thread_client.start()
        roomThreads.append(thread_client)

##Funcion donde se definiran las opciones del juego.

def game(cli_sock, port, username):
    global startGame
    while True:
        ### Sala de espera al juego
        responseP = cli_sock.recv(4096)
        print(username, " has sent a message")
        objeto = pickle.loads(responseP)

        ### Se lee el encabezado que viene como parte principal del prootocolo para definir como
        ### se leeran los siguientes parametros que se definieron como parte del protocolo
        opcionJuego = objeto['opcion']

        ### La opcion 1 es para poder iniciar la partida, dado que se debe de poder avisar
        ### a los demas jugadores que la partida esta lista cuando ya hay al menos 3 jugadores
        if opcionJuego == 1:
            if cli_sock in ROOMSplayersAlive[port]:
                if startGame[port] == False:
                    ### Se revisa que haya al menos 3 jugadores para poder empezar la partida
                    if ROOMS[port] > 2 and ROOMS[port] < 6:
                        ### Se hace un set de los elementos del juego
                        ### Se revuelve el mazo
                        random.shuffle(ROOMpiles[port])
                        random.shuffle(ROOMpiles[port])
                        random.shuffle(ROOMpiles[port])

                        ### Se le da un defuse a cada jugador
                        for player in ROOMScon[port]:
                            ROOMpilesPlayers[port][player].append(7)
                            ROOMamountDefuses[port] = ROOMamountDefuses[port] - 1
                        
                            ### Se reparten 7 cartas a cada jugador

                            for k in range(7):
                                pilaTemporal = ROOMpiles[port]
                                ROOMpilesPlayers[port][player].append(pilaTemporal.pop())
                                ROOMpiles[port] = pilaTemporal

                        ### Se agregan los defuses y bombas al mazo
                        random.shuffle(ROOMpiles[port])
                        random.shuffle(ROOMpiles[port])
                        random.shuffle(ROOMpiles[port])

                        counterBombs = 0
                        for player in ROOMScon[port]:
                            if counterBombs < len(ROOMScon[port]) - 1:
                                ### Se agrega una bomba y se revuelve
                                ROOMpiles[port].append(8)
                                random.shuffle(ROOMpiles[port])
                            counterBombs = counterBombs + 1
                            
                        for j in range(ROOMamountDefuses[port]):
                            ### Se agrega una bomba y se revuelve
                            ROOMpiles[port].append(7)
                            random.shuffle(ROOMpiles[port])

                        ### Hay que revolver bien las cartas :)
                        random.shuffle(ROOMpiles[port])

                        ### Se notifica al resto de jugadores que inicio el juego
                        mensajeInicio = {
                            'header' : 'inicio'
                        }
                        startGame[port] = True
                        mensajeInicioP = pickle.dumps(mensajeInicio)
                        for client in ROOMScon[port]:
                            client.send(mensajeInicioP)

                        ### Luego se notifica el player que va de primero
                        ROOMSturnPlayers[port].append(0)
                        mensajeTurno = {
                            'header' : 'turno',
                            'mensaje' : '\nEs el turno del User: ' + ROOMSusername[port][ROOMSturnPlayers[port][0]]
                        }
                        mensajeTurnoP = pickle.dumps(mensajeTurno)
                        for client in ROOMScon[port]:
                            client.send(mensajeTurnoP) 

                    ### En caso no haya suficientes jugadores, entonces se manda un mensaje de error
                    ### a todos los clientes
                    else:
                        mensajeInicio = {
                            'header' : 'fallo',
                            'mensaje' : '\nEl juego ha tratado de ser iniciado pero no hay suficientes jugadores aun.'
                        }
                        mensajeInicioP = pickle.dumps(mensajeInicio)
                        for client in ROOMScon[port]:
                            client.send(mensajeInicioP)
                ### En caso se quiera iniciar el juego cuando ya se ha iniciado entonces se manda un mensaje
                ### al cliente para avisarle que la partida ya esta en curso
                else:
                    mensajeInicio = {
                        'header' : 'fallo',
                        'mensaje' : '\nEl juego ya fue iniciado.'
                    }
                    mensajeInicioP = pickle.dumps(mensajeInicio)
                    cli_sock.send(mensajeInicioP)
            ### Estas fuera del juego
            else:
                mensajeInicio = {
                    'header' : 'fuera',
                    'mensaje' : '\nPerdiste, ya no puedes hacer acciones.'
                }
                mensajeInicioP = pickle.dumps(mensajeInicio)
                cli_sock.send(mensajeInicioP)

        ### La opcion 2 es para poder utilizar el Chat (Broadcast) 
        
        elif opcionJuego == 2:
            ### Verifica que la partida este iniciada para poder enviar mensajes
            if startGame[port] == True:
                broadcast_usr(username, cli_sock, objeto, port)
            ### En caso no se haya iniciado una partida se imprime un mensaje de error al cliente para indicarle que la partida
            ### aun no ha iniciado
            else:
                mensajeInicio = {
                    'header' : 'fallo',
                    'mensaje' : '\nEl juego aun no ha sido iniciado.'
                }
                mensajeInicioP = pickle.dumps(mensajeInicio)
                cli_sock.send(mensajeInicioP)      




def broadcast_usr(uname, cli_sock, objeto, port):
    try:
        data = objeto['mensaje']
        if data:
            print("{0} mando un mensaje".format(uname))
            b_usr(cli_sock, uname, data, port)
    except KeyError as e:
        raise KeyError(str(e) + ' Error')

def b_usr(cs_sock, sen_name, msg, port):
    for client in ROOMScon[port]:
        if client != cs_sock:
            objeto = { 
                'header' : 'chat',
                'nombre' : sen_name,
                'mensaje' : msg
            }
            client.send(pickle.dumps(objeto))

