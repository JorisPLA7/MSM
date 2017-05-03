# -∗- coding: utf-8 -∗-

import socket
import threading
import time
from threading import Thread


verbose = 0
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host = '127.0.0.1' # l'ip locale de l'ordinateur
Port = 8082 # choix d'un port

global MyClient
MyClient = []
global ClientList
ClientList = {}
global NicknameList
NicknameList = []
# on bind notre socket :
Sock.bind((Host,Port))

class ServerNet():
    '''Classe Serveur, sert d'interface entre certains threads et mes collègues
    Joris Placette
    '''
    def __init__(self): #initiallisation du thread de reception des nouveaux clients
        self.ReceptionistThread = Receptionist(1, "ReceptionistThread")


    def Listen(self,Toogler):
        if Toogler == True:
            self.ReceptionistThread.start()





class Guest(threading.Thread) :
    '''Classe de gestion de Client individuellement.
    Joris Placette
    '''
    def __init__(self, GuestID, Client, Address): #initiallisation des variables de l'objet nouvellement crée
        threading.Thread.__init__(self)
        self.GuestID = GuestID
        self.Client = Client
        self.Address = Address
        self.Authenticated = False
        self.Nickname = None
        self.NickLen = None
        self.AuthenticationThread = 0
        self.Authenticated = 0
        self.DoListen = 0



    def SetNickname(self, NewNick):
        self.Nickname = NewNick
        self.NickLen = len(self.Nickname)

    def GetAuth(self):
        while not self.Authenticated :
            data = self.Client.recv(32) # on recoit x caracteres grand max
            RequeteDuClient = data.decode()
            RequeteDuClient = str(object=RequeteDuClient)
            if verbose : print("RequeteDuClient : '{}'".format(RequeteDuClient))
            print(RequeteDuClient[0:4])
            if RequeteDuClient[0:4] == 'AUTH':
                ReceivedNickLen = int(RequeteDuClient[4])
                if verbose : print("ReceivedNicklen = {}".format(ReceivedNickLen))
                self.Nickname = RequeteDuClient[5:5+ReceivedNickLen]
                self.Authenticated = True
                me = (self.Client)
                ClientList[self.Nickname]= (True,me) ## True, pour indiquer que le client est connecté
                NicknameList.append((time.asctime(),self.Nickname))
                print("Historique des clients : {}".format(NicknameList))
                print("Client {} authentifié !".format(self.Nickname))

    def Listen(self,value):
        self.DoListen = value
        while self.DoListen == 1:
            try:
                RequeteDuClient = self.Client.recv(1024).decode() # on recoit 255 caracteres grand max
                if not RequeteDuClient: # si on ne recoit plus rien
                    if verbose : print(("L'adresse {} vient de se déconnecter!").format(self.Address))
                    break  # on break la boucle (sinon les bips vont se repeter)
                try:
                    exec(RequeteDuClient)# affiche les donnees
                except:
                    print("------------------{} ({}) :  {}" .format(self.Nickname, self.Address, RequeteDuClient))
                    time.sleep(1)
                    data = bytes("coucou ! ça marche enfin", 'utf8') # on rentre des donnees
                    self.Client.send(data)
            except:
                pass

    def run(self):
        try:
            self.GetAuth()
        except:
            print("impossible d'authentifier le client {}".format(self.Address))

        if self.Authenticated : self.Listen(1)




class Receptionist (threading.Thread):
    ''' Classe de threading chargée de récéptionner les conncetions des clients.
    concue pour être invoquée en 1 exemplaire par la classe ServerNet.
    N'est pas prévue pour être manipulée par l'utilisateur.
    '''
    def __init__(self, threadID, name): #initiallisation des variables de l'objet nouvellement crée
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        i = 0 # i : thread counter
        while 1:# On est a l'ecoute d'une seule et unique connexion à la fois :
            Sock.listen(5)
            # Le script se stoppe ici jusqu'a ce qu'il y ait connexion :
            Client, Address = Sock.accept() # accepte les connexions de l'exterieur
            t = Guest(i, Client, Address)
            MyClient.insert(i, t)
            MyClient[i].start()
            i+=1






MyServ = ServerNet()
MyServ.Listen(True)
print("En attente de clients...")

while 1 :

    try :
        exec(input(">>>")) #sorte d'invite de commande en cas de lancement interactif sur le serveur
    except:
        pass
