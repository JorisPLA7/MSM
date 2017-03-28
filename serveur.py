#!/usr/bin/python3.2
# -∗- coding: utf-8 -∗-
#  http://www.progx.org/index.php?section=articles&article=Python/article13


import socket

#pour récupérer l'adresse ip
#Sock.connect(("gmail.com",80))
#Host=Sock.getsockname()[0]
#Sock.close()
#print(Host)

Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host = '127.0.0.1' # l'ip locale de l'ordinateur
Port = 8082 # choix d'un port

# on bind notre socket :
Sock.bind((Host,Port))

# On est a l'ecoute d'une seule et unique connexion :
Sock.listen(2)

# Le script se stoppe ici jusqu'a ce qu'il y ait connexion :
client, adresse = Sock.accept() # accepte les connexions de l'exterieur
print(("L'adresse {} vient de se connecter au serveur !").format(adresse))
while 1:
            RequeteDuClient = client.recv(255) # on recoit 255 caracteres grand max
               if not RequeteDuClient: # si on ne recoit plus rien
                print(("L'adresse {} vient de se déconnecter!").format(adresse))
                break  # on break la boucle (sinon les bips vont se repeter)
               exec(RequeteDuClient.decode())# affiche les donnees
