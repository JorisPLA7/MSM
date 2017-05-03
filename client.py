#!/usr/bin/python3.2
# -∗- coding: utf-8 -∗-
import socket # on importe le module
import threading
import time
global Sock

Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on cree notre socket
Sock.settimeout(2.0)

class NetThread (threading.Thread) :
    '''Classe-Thread chargé de l'envoi & récéption de donnée via le socket une fois le client authentifié.
    N'est pas censé être manipulé par Mes camarades, il s'occupe de la partie "veille" de la classe Net.
    Voir help(Net())
    Par Joris Placette
    '''
    def __init__(self):
        threading.Thread.__init__(self)
        self.Message = 0

    def run(self):

        while 1:
            if self.Message != 0:
                Sock.send(self.Message.encode())
                self.Message = 0

            try :
                data = Sock.recv(1024).decode()
                print('Received from server: ' + data)
            except:
                pass


class Net ():
    '''Classe interactive (API) pour mes camarades, se charge de mettre en forme les interactions client-serveurr pour une utilisation simplifiée des fonctionnallités socket.
    Par Joris Placette
    '''
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
        '''Envoie une requette d'authentification.
        Necessaire coté serveur c'est la première chose à faire après avoir initialisé Net.
        Par Joris Placette
        '''
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
        '''Affiche le statut du client vis à vis du serveur
        Par Joris Placette
        '''
        return self.Connected
    def Disconnect(self):
        '''Force la fermeture de la connexion, rends impossible l'entrée et la sortie de données.
        Par Joris Placette
        '''
        Sock.close()
        print("Disconnected", sep=' ')

    def SendMsg(self,typed):
        '''Permet de transmettre une chaine de caractères brute au serveur.

        Version DEV :
            Svp pay attention :) .
            Si la Chaine est reconnue comme une ligne de code python alors elle est EXECUTEE.
        Par Joris Placette
        '''
        self.NetThread.Message = typed

    def WhoAmI(self):
        '''Renvoie le Pseudonyme déclaré au serveur lors de l'__init__()
        Par Joris Placette
        '''
        return self.Nickname

def debug():
    '''Saisir du code en cours de route, ça peut toujours servir... :)
    Par Joris Placette
    '''
    print("Fonction de débuggage...")
    while 1 :

        try :
            exec(input(">>>")) #sorte d'invite de commande en cas de lancement interactif sur le serveur
        except:
            pass


def login():
    '''Fct de démonstration et de test.
    c'est un cadeau pour toi Arth <3 ^^
    Par Joris Placette
    '''
    ##phase de login
    Host = "0"
    if Host == "0":
            Host ="127.0.0.1"
    Port = 8082
    print("Saisir 'q' pour obtenir un terminal de commande")
    Nickname = str(input("saisir un pseudo :  "))
    if Nickname == 'q':
        debug()
    Pass = "lol ;')"
    global MyNet

    MyNet = Net(Host, Port , Nickname, Pass)

    MyNet.Authenticate()
    if MyNet.Connected == True :
        print("Vous êtes connecté en tant que {}".format(MyNet.WhoAmI()))
        while True:
            Typed = input("{} :  ".format(Nickname))
            MyNet.SendMsg(Typed)

while 1 :
    login()

# On est connecte, on fait une boucle infinie d'inputs pour l'envoi des messages :
