# Project 2: Card Game 
[![Build Status](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)](https://www.python.org/)

## Goals
- 🌐 Apply TCP concepts to keep the internal states of different clients of an application synchronized. 🌐
- 😊 Develop an eye-catching card game. Make it easy to play. 😊

## Features to develop

- Support 3+ players.
- Allow strategy, not pure luck.
- Player must have public and private state.
- Turn based.
- Open chat
- Players can decide a nickname when joining the game.
- Has to be able to manage multiple rooms. Support simultaneous games.

## Selected game was: Exploding Kittens 🐱💣💥
Rules and instructions can be found here: https://www.explodingkittens.com/pages/rules-kittens-party

## Requirements
The tools used for development and use were:
```sh
Python 3.7+
socket
threading
os
random
operator
```
You can install them by running
```sh
pip install -r requirements.txt 
```

## Getting Started
```sh
python server.py
```
In this program you type the port, for example 5000.
```sh
python client.py
```
In the client program you must use 'localhost' as the ip address and type the port used in the server program, in this case 5000.

And now you can start playing the game!!! Have fun! 😼😼

## Members:
Andrea Elías https://github.com/andreaeliasc
Diego Estrada https://github.com/diegoestradaXO
Luis Urbina https://github.com/virtualmonkey
