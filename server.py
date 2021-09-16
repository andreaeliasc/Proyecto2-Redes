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

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
