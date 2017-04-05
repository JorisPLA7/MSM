#!/usr/bin/python3.2
# -∗- coding: utf-8 -∗-
#  http://www.progx.org/index.php?section=articles&article=Python/article13

def ConnectMe(Host, Port, Nickname, Pass):
    """Connection au serveur """
    try:
        # on se connecte sur le serveur avec les informations ci-dessus
        # assurez-vous d'avoir mis en marche le serveur !
        Sock.connect((Host,Port))
        Sock.send(msg)
    except:
        print("connection au serveur {}:{} impossible".format(Host, Port))


import socket # on importe le module
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on cree notre socket

##phase de login
Host =input("Entrez l'ip du serveur auquel se conecter; entrer '0' pour '127.0.0.1': ")
if Host == "0":
        Host ="127.0.0.1"
Port = 8082
Nickname = input("Saisissez un Pseudo: ")
Pass = input("Saisissez un mot de passe: ")
ConnectMe(Host, Port, Nickname, Pass)

# On est connecte, on fait une boucle infinie d'inputs pour l'envoi des messages :
while 1:

        msg = bytes(input('{}>> '.format(Host)), 'utf8') # on rentre des donnees
        Sock.send(msg) # on envoie ces donnees
