##network-traveler Joris Placette GPL-2017
import socket
import threading
import time


class MyThread (threading.Thread):

   def run ( self ):

      print('VOICI LE PERMIER MESSAGE yeah.')
      time.sleep(3) #will sleep for 5 seconds

      print('SUIVI DU 2EME')
##MyThread().start()
def Server():
    Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    Host = '127.0.0.1' # l'ip locale de l'ordinateur
    Port = 8082 # choix d'un port

    # on bind notre socket :
    Sock.bind((Host,Port))

    # On est a l'ecoute d'une seule et unique connexion :
    Sock.listen(2)
    client, adresse = Sock.accept() # accepte les connexions de l'exterieur

    serverd_thread = threading.Thread(name = 'Handler', target = Listener) ###############"""

    def Listener():
        server_socket.listen(5)
        client, address = self.server_socket.accept() #################################################################


def Application():
    mode=input("Selectionner un mode de fonctionnement (s/c)")
    if mode == 'c':
        Client()

    if mode == 'c':
        Server()

if __name__ == '__main__':
    Application()
