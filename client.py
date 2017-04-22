#!/usr/bin/python3.2
# -∗- coding: utf-8 -∗-
import socket # on importe le module
import threading
import time

global Sock
class Net ():
    def __init__(self,Host, Port, Nickname, Pass):
        self.Host = socket.gethostbyname(Host)
        self.Port = Port
        self.Nickname = Nickname
        self.NickLen = str(len(self.Nickname))
        self.Pass = Pass
        self.Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on cree notre socket

    def Authenticate(self):
        data = bytes("AUTH" + self.NickLen + self.Nickname, 'utf8')
        self.Sock.connect((self.Host,self.Port)) # on se connecte sur le serveur avec les informations données
        self.Sock.send(data)

    def Disconnect(self):
        print("Disconnected", sep=' ')

    def SendMsg(self, msg):
        time.sleep(1) #afin de donner le temps au serv d'être en écoute
        data = bytes(msg, 'utf8') # on rentre des donnees
        self.Sock.send(data) # on envoie ces donnees

    def Execute(self):
        pass
    def WhoAmI(self):
        return self.Nickname

    def ListRooms(self):
        return (salle1, salle2, salle3)

def login():
    ##phase de login
    Host = "0"
    if Host == "0":
            Host ="127.0.0.1"
    Port = 8082
    Nickname = str(input("saisir un pseudo"))
    Pass = "lol ;')"
    global MyNet

    MyNet = Net(Host, Port , Nickname, Pass)

    MyNet.Authenticate()
    MyNet.SendMsg("ça croustille")
    print(MyNet.WhoAmI())
    a = input()
    """
    data = self.Client.recv(64) # on recoit x caracteres grand max
    RequeteDuClient = data.decode()
    RequeteDuClient = str(object=RequeteDuClient)
    print(RequeteDuClient)
    a = input()
"""

while 1 :
    login()

# On est connecte, on fait une boucle infinie d'inputs pour l'envoi des messages :
