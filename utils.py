'''
    File name: utils.py
    Author: Andrea Elías, Diego Estrada & Luis Urbina
    Date created: 10/09/2021
    Python Version: 3.7
'''

from random import sample

Mazo=[]
MP1=[]
MP2=[]
MP3=[]
MP4=[]
MP5=[]
Carta1="Va a ser que no"
Carta2="Ataque"
Carta3="Pasar"
Carta4="Favor"
Carta5="Barajar"
Carta6="Ver el futuro"
Carta7="Gato1"
Carta8="Gato2"
Carta9="Gato3"
Carta10="Gato4"
Carta11="Salvacion"
Carta12="Bomba"

def MazoPrincipal():
    #Se agrega al mazo la carta "Va a ser que no"
    for i in range(5):
        Mazo.append(Carta1)
    #Se agrega al mazo la carta "Ataque"
    for i in range(4):
        Mazo.append(Carta2)
    #Se agrega al mazo la carta "Pasar"
    for i in range(4):
        Mazo.append(Carta3)
    #Se agrega al mazo la carta "Favor"
    for i in range(4):
        Mazo.append(Carta4)
    #Se agrega al mazo la carta "Barajar"
    for i in range(4):
        Mazo.append(Carta5)
    #Se agrega al mazo la carta "Ver el futuro"
    for i in range(5):
        Mazo.append(Carta6)
    #Se agrega al mazo la carta "Gato1"
    for i in range(4):
        Mazo.append(Carta7)
    #Se agrega al mazo la carta "Gato2"
    for i in range(4):
        Mazo.append(Carta8)
    #Se agrega al mazo la carta "Gato3"
    for i in range(4):
        Mazo.append(Carta9)
    #Se agrega al mazo la carta "Gato4"
    for i in range(4):
        Mazo.append(Carta10)
    return Mazo
def MazoJugadores(Njugadores,Mazo):
    rando=sample(Mazo,k=len(Mazo))
    #####################################Dos Jugadores#####################################################
    if Njugadores=="2":
        for i in range(7):
            MP1.append(rando[0])
            rando.pop(0)
            MP2.append(rando[0])
            rando.pop(0)
        MP1.append(Carta11)
        MP2.append(Carta11)
        for i in range(4):
            rando.append(Carta11)
        for i in range(1):
            rando.append(Carta12)
    #####################################Tres Jugadores#####################################################
    if Njugadores=="3":
        for i in range(7):
            MP1.append(rando[0])
            rando.pop(0)
            MP2.append(rando[0])
            rando.pop(0)
            MP3.append(rando[0])
            rando.pop(0)
        MP1.append(Carta11)
        MP2.append(Carta11)
        MP3.append(Carta11)
        for i in range(3):
            rando.append(Carta11)
        for i in range(2):
            rando.append(Carta12)
    rando=sample(rando,k=len(rando))
    return MP1,MP2,MP3,MP4,MP5,rando






