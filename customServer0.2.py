# -∗- coding: utf-8 -∗-

import socket
import threading

verbose = 0
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host = '127.0.0.1' # l'ip locale de l'ordinateur
Port = 8082 # choix d'un port

MyClient = []
global Client

# on bind notre socket :
Sock.bind((Host,Port))

class ServerNet():
    def __init__(self):
        self.ReceptionistThread = Receptionist(1, "ReceptionistThread")
        self.ClientList = {}

    def Listen(self,Toogler):
        if Toogler == True:
            self.ReceptionistThread.start()

        #if Toogler == False:
            #self.ReceptionistThread.Stop() #non fonctionnel


    def ListClients(self):
        return self.ReceptionistThread.ListClients()

class Guest(threading.Thread) :
    '''Classe de gestion de Client pas le serveur client par client.
    '''
    def __init__(self, SessionID, Client, Address):
        self.SessionID = SessionID
        self.Client = Client
        self.Address = Address
        self.Authenticated = False
        self.Nickname = None
        self.NickLen = None
        self.HandlerThread = 0
        self.IsAuth = 0

    def Handle(self):
        self.HandlerThread = Handler(self.SessionID, self.Client, self.Client)
        self.HandlerThread.start()
        self.IsAuth = 1


    def Listen(self,value):
        while value == 1:
            try:
                RequeteDuClient = self.Client.recv(1024).decode() # on recoit 255 caracteres grand max
                if not RequeteDuClient: # si on ne recoit plus rien
                    if verbose : print(("L'adresse {} vient de se déconnecter!").format(self.Address))
                    break  # on break la boucle (sinon les bips vont se repeter)
                try:
                    exec(RequeteDuClient)# affiche les donnees
                except:
                    print("LOG: Commande rendeignée par {} impossible ('{}')" .format(self.Address, RequeteDuClient))
            except:
                print("Le Client {} s'est déconnecté".format(self.Address))
                break

class Receptionist (threading.Thread):
    ''' Classe de threading chargée de récéptionner les conncetions des clients.
    concue pour être invoquée en 1 exemplaire par la classe ServerNet.
    N'est pas prévue pour être manipulée par l'utilisateur.
    '''
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.ClientList = {}
        self.HandlerThread = {}

    def run(self):
        i = 0 # i : thread counter
        while 1:# On est a l'ecoute d'une seule et unique connexion à la fois :
            Sock.listen(2)
            # Le script se stoppe ici jusqu'a ce qu'il y ait connexion :
            Client, Address = Sock.accept() # accepte les connexions de l'exterieur
            MyClient.insert(i,Guest(i, Client, Address))
            MyClient[i].Handle()
            MyClient[i].Listen(1)
            i+=1

        #return self.ClientList


class Handler (threading.Thread): # conserve un lien avec le Client
    '''Classede threading d'appréhension du Client en attendant authentification.
    '''
    def __init__(self, threadID, Client, Address):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.Client = Client
        self.Address = Address
        self.Authenticated = False
        self.Nickname = None
        self.NickLen = None

    def run(self):
        while not self.Authenticated :
            data = self.Client.recv(32) # on recoit x caracteres grand max
            RequeteDuClient = data.decode()
            RequeteDuClient = str(object=RequeteDuClient)
            if verbose : print("RequeteDuClient : '{}'".format(RequeteDuClient))
            print(RequeteDuClient[0:3])
            if RequeteDuClient[0:3] == 'AUT':
                NickLen = int(RequeteDuClient[3])
                if verbose : print("Nicklen = {}".format(NickLen))
                self.Nickname = RequeteDuClient[4:4+NickLen]
                self.Authenticated = True
                print("Client {} authentifié !".format(self.Nickname))

        while 1:
            try:
                RequeteDuClient = self.Client.recv(1024) # on recoit 255 caracteres grand max
                if not RequeteDuClient: # si on ne recoit plus rien
                    if verbose : print(("L'adresse {} vient de se déconnecter!").format(self.Address))
                    break  # on break la boucle (sinon les bips vont se repeter)
                try:
                    exec(RequeteDuClient.decode())# affiche les donnees
                except:
                    print("LOG: Commande rendeignée par {} impossible ('{}')" .format(self.Address, RequeteDuClient))
            except:
                print("Le Client {} s'est déconnecté".format(self.Address))
                break

MyServ = ServerNet()
MyServ.Listen(True)
print("En attente de clients...")


while 1 :
    try :
        exec(input(">>>"))
    except:
        pass


'''    if not RequeteDuClient: # si on ne recoit plus rien
        print(("L'Address {} vient de se déconnecter!").format(self.Address))
        break  # on break la boucle (sinon les bips vont se repeter)
        print(("L'Address {} vient de se connecter au serveur !").format(self.Address))


'''
