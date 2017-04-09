#!/usr/bin/python3.2
# -∗- coding: utf-8 -∗-

import socket
import threading

Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host = '127.0.0.1' # l'ip locale de l'ordinateur
Port = 8082 # choix d'un port

# on bind notre socket :
Sock.bind((Host,Port))
class ServerNet():
    def __init__(self):
        self.ReceptionistThread = Receptionist(1, "ReceptionistThread")

    def Listen(self,Toogler):
        if Toogler == True:
            self.ReceptionistThread.start()
        #if Toogler == False:
            #self.ReceptionistThread.Stop() #non fonctionnel


class Receptionist (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.ClientList = {}
    def run(self):
        i = 0 # i : thread counter
        while 1:# On est a l'ecoute d'une seule et unique connexion à la fois :
            Sock.listen(2)
            # Le script se stoppe ici jusqu'a ce qu'il y ait connexion :
            Client, Address = Sock.accept() # accepte les connexions de l'exterieur
            HandlerThread = Handler(i, Client, Address)
            HandlerThread.start()
            self.ClientList[i] = [i, Client, Address]
            i+=1
    #def Stop(self):
            #Sock.shutdown(SHUT_RDWR)
            #Sock.close(RDWR)

class Handler (threading.Thread): # conserve un lien avec le Client
    def __init__(self, threadID, Client, Address):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.Client = Client
        self.Address = Address
        self.Authenticated = False
        self.Nickname = None
        self.NickLen = None
    def run(self):
        while not self.Authenticated:
            data = self.Client.recv(512) # on recoit x caracteres grand max
            RequeteDuClient = data.decode()
            RequeteDuClient = str(object=RequeteDuClient)
            print(RequeteDuClient)
            print(type(RequeteDuClient))
            print(RequeteDuClient[0:3])
            if RequeteDuClient[0:3] == 'AUT':
                NickLen = int(RequeteDuClient[3])
                print(NickLen)
                self.Nickname = RequeteDuClient[4:4+NickLen]
                self.Authenticated = True
                print("Client {} authentifié \naddresse : {}".format(self.Nickname, self.Address))
                #print(self.ClientList, sep=' ', end='n', file=sys.stdout, flush=False)


        while 1:
            try:
                RequeteDuClient = self.Client.recv(1024) # on recoit 255 caracteres grand max
                if not RequeteDuClient: # si on ne recoit plus rien
                    print(("L'adresse {} vient de se déconnecter!").format(self.Address))
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


'''    if not RequeteDuClient: # si on ne recoit plus rien
        print(("L'Address {} vient de se déconnecter!").format(self.Address))
        break  # on break la boucle (sinon les bips vont se repeter)
        print(("L'Address {} vient de se connecter au serveur !").format(self.Address))


'''
