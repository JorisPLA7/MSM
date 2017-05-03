'''import socket

def Main():
        host = '127.0.0.1'
        port = 5000

        mySocket = socket.socket()
        mySocket.connect((host,port))

        message = input(" -> ")

        while message != 'q':
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()

                print ('Received from server: ' + data)

                message = input(" -> ")

        mySocket.close()

if __name__ == '__main__':
    Main()
'''

#!/usr/bin/python3.2
# -∗- coding: utf-8 -∗-
import socket # on importe le module
import threading
import time

global Sock
class Receiver (threading.Thread) :
    def __init__(self, Value):
        self.DoListen = Value
        self.ReceiverSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on cree notre socket
        self.ReceiverSock.bind("127.0.0.1","8083")

    def run(self):
        if DoListen :
            pass

class Net ():
    def __init__(self,Host, Port, Nickname, Pass):
        self.Host = socket.gethostbyname(Host)
        self.Port = Port
        self.Nickname = Nickname
        self.NickLen = str(len(self.Nickname))
        self.Pass = Pass
        self.SenderSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on cree notre socket
        self.Connected = False

    def Authenticate(self):
        data = bytes("AUTH" + self.NickLen + self.Nickname, 'utf8')
        try:
            self.SenderSock.connect((self.Host,self.Port)) # on se connecte sur le serveur avec les informations données
            print("Connection avec le serveur...")
            self.SenderSock.send(data)
            print("Authentification auprès du serveur...")
            self.Connected = True
        except:
            print("Impossible de se connecter au serveur !")
            self.Connected = False

    def Connected(self):
        return self.Connected
    def Disconnect(self):
        print("Disconnected", sep=' ')

    def SendMsg(self, msg):
        time.sleep(1) #afin de donner le temps au serv d'être en écoute
        data = bytes(msg, 'utf8') # on rentre des donnees
        self.SenderSock.send(data) # on envoie ces donnees

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
