#!/usr/bin/python3.2
# -∗- coding: utf-8 -∗-

import socket
import threading


Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host = '127.0.0.1' # l'ip locale de l'ordinateur
Port = 8082 # choix d'un port

# on bind notre socket :
Sock.bind((Host,Port))

class Listener (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        i = 0 # i : thread counter
        while 1:# On est a l'ecoute d'une seule et unique connexion :
            Sock.listen(2)
            # Le script se stoppe ici jusqu'a ce qu'il y ait connexion :
            client, address = Sock.accept() # accepte les connexions de l'exterieur
            HandlerThread = Handler(i, client, address)
            HandlerThread.start()
            i+=1
class Handler (threading.Thread): # conserve un lien avec le client
    def __init__(self, threadID, client, address):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.client = client
        self.address = address
    def run(self):
        print(("L'address {} vient de se connecter au serveur !").format(self.address))
        while 1:
            try:
                RequeteDuClient = self.client.recv(1024) # on recoit 255 caracteres grand max
                if not RequeteDuClient: # si on ne recoit plus rien
                    print(("L'address {} vient de se déconnecter!").format(self.address))
                    break  # on break la boucle (sinon les bips vont se repeter)
                exec(RequeteDuClient.decode())# affiche les donnees
            except:
                print("Le client {} s'est déconnecté".format(self.address))
                break


ListenerThread = Listener(1, "ListenerThread")
ListenerThread.start()
