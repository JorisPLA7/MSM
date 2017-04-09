#!/usr/bin/python3.2
# -∗- coding: utf-8 -∗-
import socket # on importe le module
import threading

global Sock
class Net ():
    def __init__(self,Host, Port, Nickname, Pass):
        self.Host = socket.gethostbyname(Host)
        self.Port = Port
        self.Nickname = Nickname
        self.Pass = Pass
        self.Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on cree notre socket
        self.Sock.connect((self.Host,self.Port)) # on se connecte sur le serveur avec les informations données

    def Authenticate(self):
        data = bytes("AUT" +self.Nickname)
        self.Sock.send(data, flags=None)
    def SendMsgLoop(self, msg):
        data = bytes(msg, 'utf8') # on rentre des donnees
        self.Sock.send(data) # on envoie ces donnees

    def WhoAmI(self):
        return self.Nickname

##phase de login
Host =input("Entrez l'ip du serveur auquel se conecter; entrer '0' pour '127.0.0.1': ")
if Host == "0":
        Host ="127.0.0.1"
Port = 8082
Nickname = input("Saisissez un Pseudo: ")
Pass = input("Saisissez un mot de passe: ")

MyNet = Net(Host, Port , Nickname, Pass)
#MyNet.Authenticate()
MyNet.SendMsgLoop('print("couocu")')
MyNet.WhoAmI()
a = input()

# On est connecte, on fait une boucle infinie d'inputs pour l'envoi des messages :
