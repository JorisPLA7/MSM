#!/usr/bin/python3.2
# -∗- coding: utf-8 -∗-
import socket # on importe le module
import threading
global Sock
class Net ():
    def __init__(self,Host, Port, Nickname, Pass):
        self.Host = Host
        self.Port = Port
        self.Nickname = Nickname
        self.Pass = Pass
        self.Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on cree notre socket
        self.Sock.connect((self.Host,self.Port))
    def Connect(self):

        self.Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on cree notre socket


        try:
            # on se connecte sur le serveur avec les informations ci-dessus
            # assurez-vous d'avoir mis en marche le serveur !
            2*22
        except:
            print("connection au serveur {}:{} impossible".format(Host, Port))

    def SendMsgLoop(self):
        while 1:

            msg = bytes(input('{}>> '.format(Host)), 'utf8') # on rentre des donnees
            self.Sock.send(msg) # on envoie ces donnees



##phase de login
Host =input("Entrez l'ip du serveur auquel se conecter; entrer '0' pour '127.0.0.1': ")
if Host == "0":
        Host ="127.0.0.1"
Port = 8082
Nickname = input("Saisissez un Pseudo: ")
Pass = input("Saisissez un mot de passe: ")

MyNet = Net(Host, Port , Nickname, Pass)
#MyNet.Connect()
MyNet.SendMsgLoop()

# On est connecte, on fait une boucle infinie d'inputs pour l'envoi des messages :
