#!/usr/bin/python3.2
# -∗- coding: utf-8 -∗-
import socket # on importe le module
import threading
import time

global Sock

Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on cree notre socket

class NetThread (threading.Thread) :
    def __init__(self):
        threading.Thread.__init__(self)
        self.DoListen = 1
        self.Message = 0
    def run(self):
        while 1:
            if self.Message != 0:
                Sock.send(self.Message.encode())
                data = Sock.recv(1024).decode()
                print ('Received from server: ' + data)
                message = 0



        mySocket.close()

    def SendMsg (self, msg):
        self.Message = msg

class Net ():
    def __init__(self,Host, Port, Nickname, Pass):
        self.Host = socket.gethostbyname(Host)
        self.Port = Port
        self.Nickname = Nickname
        self.NickLen = str(len(self.Nickname))
        self.Pass = Pass
        self.Connected = False
        self.NetThread = NetThread()
        self.NetThread.start()

    def Authenticate(self):
        data = bytes("AUTH" + self.NickLen + self.Nickname, 'utf8')
        try:
            Sock.connect((self.Host,self.Port)) # on se connecte sur le serveur avec les informations données
            print("Connection avec le serveur...")
            Sock.send(data)
            print("Authentification auprès du serveur...")
            time.sleep(1) #afin de donner le temps au serv d'être en écoute

            self.Connected = True

        except:
            print("Impossible de se connecter au serveur !")
            self.Connected = False

    def Connected(self):
        return self.Connected
    def Disconnect(self):
        print("Disconnected", sep=' ')

    def SendMsg(self, msg):
        data = bytes(msg, 'utf8') # on rentre des donnees
        Sock.send(data) # on envoie ces donnees

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
    Nickname = str(input("saisir un pseudo :  "))
    Pass = "lol ;')"
    global MyNet

    MyNet = Net(Host, Port , Nickname, Pass)

    MyNet.Authenticate()
    if MyNet.Connected == True :
        print("Vous êtes connecté en tant que {}".format(MyNet.WhoAmI()))
        while True:
            a = input("{} :  ".format(Nickname))
            MyNet.NetThread.SendMsg(a)

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
