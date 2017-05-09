# -∗- coding: utf-8 -∗-

try :
    import socket
    print("Bibliothèque socket importée avec succès !")
except:
    print("Impossible d'importer la bibliothèque socket !")
try :
    import threading
    print("Bibliothèque threading importée avec succès !")
except:
    print("Impossible d'importer la bibliothèque threading !")
try :
    import time
    print("Bibliothèque time importée avec succès !")
except:
    print("Impossible d'importer la bibliothèque time !")
try :
    from threading import Thread
    print("Bibliothèque threading.Thread importée avec succès !")
except:
    print("Impossible d'importer la bibliothèque threading.Thread !")

Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host = '127.0.0.1' # l'ip locale de l'ordinateur
Port = 8082 # choix d'un port

global MyClient
MyClient = []
global NicknameList
NicknameList = {}
'''
La NicknameList est un historique des utilisateurs connectés depuis le lancement.
Elle permet de savoir à quel thread s'adresser pour envoyer des informations.

Par exemple pour envoyer un message à 'joris' :
MyClient[NicknameList['joris']].Transmit('Message!')

'''
global Timeout
Timeout = 1.0
global verbose
verbose = 0 #en cas de besoin il est possible de demander au serveur plus d'informations.
global Flow
# on bind notre socket :
Sock.bind((Host,Port))

class ServerNet():
    '''Classe Serveur, sert d'interface entre certains threads et mes collègues

    Par Joris Placette
    '''
    def __init__(self): #initiallisation du thread de reception des nouveaux clients
        self.ReceptionistThread = Receptionist(1, "ReceptionistThread")


    def Listen(self,Toogler):
        if Toogler == True:
            self.ReceptionistThread.start()


class Guest(threading.Thread) :
    '''Classe de gestion de Client individuellement.

    Par Joris Placette
    '''
    def __init__(self, GuestID, Client, Address): #initiallisation des variables de l'objet nouvellement crée
        threading.Thread.__init__(self)
        self.__GuestID = GuestID
        self.Client = Client
        self.Client.settimeout(Timeout) #timeout crucial pour que le serv abandonne l'écoute toute les 2 secondes pour transmettre le(s) message(s)
        self.Address = Address
        self.Identificated = False
        self.Nickname = None
        self.NickLen = None
        self.IdentificationThread = 0
        self.DoComm = 0
        self.Message = 0


    def SetNickname(self, NewNick):
        self.Nickname = NewNick
        self.NickLen = len(self.Nickname)

    def GetIdentified(self):
        while not self.Identificated :
            data = self.Client.recv(32) # on recoit x caracteres grand max
            RequeteDuClient = data.decode() #qu'on décode
            RequeteDuClient = str(object=RequeteDuClient)
            if verbose : print("RequeteDuClient : '{}'".format(RequeteDuClient))

            if RequeteDuClient[0:4] == 'IDTF':
                ReceivedNickLen = int(RequeteDuClient[4]) #lecture de la longueur du pseudo (doit être <= à 9 char! )
                if verbose : print("ReceivedNicklen = {}".format(ReceivedNickLen))
                self.Nickname = RequeteDuClient[5:5+ReceivedNickLen]

                self.Identificated = True #Le client est désormais identifié
                me = (self.Client)
                NicknameList[self.Nickname] = self.__GuestID #permet à samuel de savoir à quel thread s'adresser en donnant un pseudo
                print("Historique des clients : {}".format(NicknameList))
                print("Client {} Identifié !".format(self.Nickname))

    def __RequestTreatment(self, Request):
        try:
            exec(Request)# on tente d'executer la chaine de caractères reçus arbitrairement
        except:
            Flow(self.__GuestID, self.Address, self.Nickname, Request) #sinon on la soumet à la fonction Flow pour Samuel

    def Transmit(self, msg):
        '''Cette fonction permet à mes camarades d'envoyer du contenu tel qu'une chaine de caractères (un tuple, une image, etc...) au client.

        Par Joris Placette
        '''
        self.Message = msg

    def __Comm(self,value):
        ''' Classe chargée de l'envoi & récéption de donnée via le socket une fois le client Identifié.
        Elle s'occupe de la partie "veille" de la classe Net.

        N'est pas concue pour être manipulée par Mes camarades.

        Par Joris Placette
        '''
        self.DoComm = value #variable permettant de stopper les échanges
        while self.DoComm == 1:
            if self.Message != 0: #si un message a été ajouté depuis la dernière fois
                self.Client.sendall(self.Message.encode()) #sendall permet de s'assurer que le message arrive EN ENTIER
                self.Message = 0
            try:
                data = self.Client.recv(1024).decode() #le thread reste à l'écoute d'un message pendant la durée renseignée par Timeout
                self.__RequestTreatment(data) #on sous-traite les données pour reserver cette fonction aux seuls communications
            except:
                #en cas de time-out on passe simplement à la suite
                pass

    def WhoIsIt(self):
        '''Fonction retournant le Pseudonyme rensigné par l'utilisateur lors de la phase d'Identification.
        Par Joris Placette
        '''
        return self.Nickname

    def run(self):
        '''Se lance automatiquement en thread.

        N'est pas concue pour être manipulée par Mes camarades.

        Par Joris Placette
        '''
        try:
            self.GetIdentified()
        except:
            print("impossible d'Identififier le client {}".format(self.Address))

        if self.Identificated : self. __Comm(1)

class Receptionist (threading.Thread):
    ''' Classe de threading chargée de récéptionner les conncetions des clients.
    concue pour être invoquée en 1 exemplaire par la classe ServerNet.

    N'est pas concue pour être manipulée par Mes camarades.

    Par Joris Placette
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


def Flow(clientID, clientAddress, clientNick, data):
    '''Cette fonction est appelée à chaque fois que des données sont recues.
    Le traitement de ces données est une simple démonstration.
    Cette fonction permettra à Samuel de recevoir et traiter les données émises par les clients.

    Par Joris Placette
    '''
    broadcast = True
    result = "-- {} -- {} {} :  {}" .format(clientID, clientNick, clientAddress, data)
    print(result)
    if broadcast == True:
        for i in range(0,len(MyClient)+1):
            MyClient[i].Transmit(result)

def SimpleHost():
    '''Fct de démonstration et de test.
    c'est un cadeau pour toi Samuel <3 ^^

    Par Joris Placette
    '''
    MyServ = ServerNet()
    MyServ.Listen(True)
    print("En attente de clients...")

    while 1 :

        try :
            exec(input(">>>")) #sorte d'invite de commande en cas de lancement interactif sur le serveur
        except:
            pass

if __name__ == '__main__':
    SimpleHost() # ce fichier sera peut-être une librairie, il faut donc empêcher l'inclusion du login si appelée par un autre fichier.
