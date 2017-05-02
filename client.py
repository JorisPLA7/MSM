#!/usr/bin/python3.2
# -∗- coding: utf-8 -∗-
import socket # on importe le module
import threading
import time

global Sock

 #c'est temporaire, ojn va fixer ça ... désolé aux lecteurs fragiles
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on cree notre socket

class Receiver (threading.Thread) :
    def __init__(self):
        threading.Thread.__init__(self)
        self.DoListen = 1
        self.Message = False

        print('init receiver Thread qui porte mal son nom')

    def Queue(self, message):
        self.Message = message

    def run(self):
        while 1:
            if self.Message != False:
                print('envoi...  {}'.format(self.Message))
                data = bytes(self.Message, 'utf8') # on rentre des donnees
                Sock.send(data) # on envoie ces donnees
                self.Message = False

            if self.DoListen =='a':
                data = Sock.recv(1024).decode
                if not data:
                    Sock.close()
                if data :
                    print('-------serv: {}'.format(data))

        '''print("ARCHTUNG CA FUNCTIONNIERT")
        while 1:
            Sock.listen()
            data = Sock.recv(1024).decode()
            print("--------------serv : {}".format(data))

        while self.DoListen == 1:
            try:
                RequeteDuServ = Sock.recv(1024).decode() # on recoit 255 caracteres grand max
                if not RequeteDuServ: # si on ne recoit plus rien
                    if verbose : print(("ecoute stopée").format(self.Address))
                    break  # on break la boucle (sinon les bips vont se repeter)
                try:
                    exec(RequeteDuServ)# affiche les donnees
                except:
                    print("------------------ {}" .format(RequeteDuServ))
            except:
                print("Le serv {} ( {} ) n'est plus sous écoute!".format(self.Nickname, self.Address))
                """break"""
        '''


class Net ():
    def __init__(self,Host, Port, Nickname, Pass):
        self.Host = socket.gethostbyname(Host)
        self.Port = Port
        self.Nickname = Nickname
        self.NickLen = str(len(self.Nickname))
        self.Pass = Pass
        self.Connected = False
        self.Receiver = Receiver()
        self.Receiver.start()

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
        self.Receiver.Queue(msg)

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
            MyNet.SendMsg(a)

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
