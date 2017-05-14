# -∗- coding: utf-8 -∗-
from tkinter import*    #pour l'affichage des fenêtres
from tkinter import messagebox  #pouvoir mettre des messager d'erreur
import time #pouvoir mettre un minuteur

fenetre = Tk()          #création de la fenêtre login
fenetre.wm_title("MSM (login)") #renomme la fenetre



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

class NetThread (threading.Thread) :
    '''Classe-Thread chargé de l'envoi & récéption de donnée via le socket une fois le client identifié.
    Elle s'occupe de la partie "veille" de la classe Net.

    N'est pas concue pour être manipulée par Mes camarades.

    Voir l' help(Net())

    Par Joris Placette
    '''
    def __init__(self):
        threading.Thread.__init__(self) #séquence init du thread
        self.Message = 0
        self.thereIsSomeNewData = False # désolé pour la longueur du nom de cette variable je n'ai pas trouvé mieux
    def __RequestTreatment(self, Request):
        Flow(Request)

    def run(self):

        while 1:
            if self.Message != 0:
                Sock.sendall(self.Message.encode()) #envoi du message ss forme de bytecode
                self.Message = 0

            try :
                data = Sock.recv(1024).decode() #attente d'une reponse pdt 2sec en cas de timeout retourne une erreur, d'ou le try & except
                self.thereIsSomeNewData = True
            except:
                pass #en cas de time-out on passe simplement à la suite
            if self.thereIsSomeNewData:
                self.__RequestTreatment(data)#J'ai sorti la fonction du try; pour rendre le débuggage possible
            self.thereIsSomeNewData = False

class Net ():
    '''Classe interactive (API) pour mes camarades, se charge de mettre en forme les interactions client-serveurr pour une utilisation simplifiée des fonctionnallités socket.

    Par Joris Placette
    '''
    def __init__(self,Host, Port, Nickname, Pass):

        global Sock #devra être accessible dans toutes les classes
        Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on cree notre socket
        Sock.settimeout(1.0) #timeout crucial pour que le serv abandonne l'écoute toute les 2 secondes pour transmettre le(s) message(s)

        self.Host = socket.gethostbyname(Host) #récupération de l'adresse auprès des DNS par défaut si nom de domaine fourni
        self.Port = Port
        self.Nickname = Nickname #La Gui indique Pseudo au lieu de Nickname, doit mesurer 10 charactères ou moins
        self.NickLen = str(len(self.Nickname))  #calcul de la longueur du Pseudonyme
        self.Pass = Pass #le pas ne sert pas durant la phase d'identification du client, j'ai cependant implanté cette variable si mes camarades en ont besoin
        self.Connected = False
        self.__NetThread = NetThread()
        self.__NetThread.start() #Démarrage du thread chargé d'éccouter et de shipper les messages

    def Identify(self):
        '''Envoie une requette d'identification.
        Necessaire coté serveur c'est la première chose à faire après avoir initialisé Net.

        Par Joris Placette
        '''
        data = bytes("IDTF" + self.NickLen + self.Nickname, 'utf8') #on crée la chaine d'info d'identification comme "IDTF7exemple"

        try:
            Sock.connect((self.Host,self.Port)) # on se connecte sur le serveur avec les informations données
            print("Connection avec le serveur...")
            Sock.sendall(data)
            print("Identification auprès du serveur...")
            time.sleep(1) #afin de donner le temps au serv d'être en écoute

            self.Connected = True #la connexion a été établie, MAJ du status

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
        Sock.close() # rends impossible l'entrée et la sortie de données.
        print("Disconnected")

    def Transmit(self,typed):
        '''Permet de transmettre une chaine de caractères brute au serveur.

        /!\ : Pour le moment les messages sont transmis toute les 2sec et non empillés, donc en cas de spam des messages seront perdus :/

        /!\ : Version DEV :
            Svp pay attention :) !
            Si la Chaine est reconnue comme une ligne de code python alors elle est EXECUTEE.

        Par Joris Placette
        '''
        self.__NetThread.Message = typed #transmett la chaine au thread, on n'execute pas de fonction sinon il faut attentdre la fin de celle-ci , on se contente donc de transmettre la donnée.

    def WhoAmI(self):
        '''Renvoie le Pseudonyme déclaré au serveur lors de l'__init__()

        Par Joris Placette
        '''
        return self.Nickname
global Flow
def Flow(Request):
    global repflow,verifvar,msgre
    repflow = Request   #repflow prend la veleur que la base de données envoie
    verifvar = 0
    if repflow == False:    #si le pseudo est deja utilisé cela modifie la veleur et deconnecte l'utilisateur
        verifvar = 1
    if len(repflow)==2: #recupere le string de la base de donné avec le dernier message
        msgre = 1


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
    '''
    Par Arthur Duca
    '''
def login():
    global Nickname,MyNet,strnick
    Nickname = pseudo.get()          #récupère le pseudo saisie
    strnick = str(Nickname) #preparation du message a envoyer a la base de données
    '''
    Par Joris Placette
    '''
    Host ="127.0.0.1"
    Port = 8082
    Pass = "lol ;')"

    MyNet = Net(Host, Port , Nickname, Pass)
    MyNet.Identify()
    '''
    Par Joris Placette
    '''
    if MyNet.Connected == True :
        print("Vous êtes connecté en tant que {}".format(MyNet.WhoAmI()))
        if Nickname!='':        #Vérif qu'il y a un pseudo
            fenetre.destroy() #fermeture fenetre login
            verifpseudo()   #verifie avec la base de donnée si le pseudo est déja pris
        elif Nickname=='':
            messagebox.showinfo("ERREUR", "Il semble que votre pseudo ou mot de passe soit incorrect.") #message d'errueur si l'utilisateur n'a pas rentré de pseudo
        while True:
            Typed = input(">")
            MyNet.Transmit(Typed)
    '''
    Par Arthur Duca
    '''
def verifpseudo():  #fonction qui vérifie avec la base de données si le psudo est valide
    global verifvar
    MyNet.Transmit(strnick) #envoie du sting definit plus haut a la base de données
    time.sleep(5)   #attente de reponse
    if verifvar==0:
        chate() #ouvre la fenetre suivante
    else:
        messagebox.showinfo("ERREUR","Ce nom d'utilisateur est déjà pris. Relancer l'application.") #message d'erreur si le pseudo est deja pris
        time.sleep(2)
        MyNet.Disconnect()  #deconnexion de l'utilisateur


def envoie():
    global zchat,messaje,messagetap
    messagetap=zchat.get()  #recuperation du message ecrit dans la case
    messaje=[Nickname,messagetap]   #creation d'une liste avec pseudo est message pour la base de données
    MyNet.Transmit(messaje) #envoie de la liste a la base de données
    nuser1 = LabelFrame(fenetre3, text=Nickname)    #création de la fenetre avec le nom d'utilisateur
    nuser1.pack()
    tuser1 = Label(nuser1, text=messagetap) #insertion dans la fenetre du texte ecrit par l'utilisateur
    tuser1.pack()
    zchat.destroy() #efface la case avec le message et la recrees
    zchat = Entry(chat)
    zchat.pack(side=LEFT)

def sel():
    global MyNet
    B=cont2.curselection()  #recupere l'information du nom selectionné
    psdsel=cont[B[0]]    #Nom de la personne selectionné
    MyNet.Transmit(1)   #envoie le nombre de message desireux a la base de données
    time.sleep(5)   #attends une reponse de la base de données
    if msgre==1:    #crée une fenetre avec le dernier message de la personne selectionné
        nuser1 = LabelFrame(fenetre3, text=C)
        nuser1.pack()
        tuser1 = Label(nuser1, text=messagetap)
        tuser1.pack()

##titre+bouton
titre = Label(fenetre, text="MSM", width=30, height=10, anchor=CENTER)
titre.pack(side=TOP)

bsal = Frame(fenetre)
bsal.pack(side=BOTTOM)
bgo = Button(bsal, text ="GO", command = login, anchor=CENTER, pady=4, height=3, width=15)  #anchor=placement
bgo.pack(side = BOTTOM)
##pseudo
pseudal = Frame(fenetre) #Création de fenetre dans une fenetre pour une meilleure presentation
pseudal.pack()
psn = Label(pseudal, text="Pseudo:", pady=4)   #Création et positionnement du mot "pseudo"
psn.pack(side = LEFT)
pseudo = Entry(pseudal)   #Création et positionnement d'une zone pour la sasie du pseudo
pseudo.pack(side = RIGHT)

def chate(): #nouvelle fenetre avec le chat
    global cont2,cont,fenetre3,chat,zchat
    fenetre3 = Tk() #création de la fenêtre chat
    fenetre3.wm_title("MSM (chat)") #renomme la fenetre de chat
    contact = Frame(fenetre3)   #creation de sous fenetres pour un positionnement plus simple
    contact.pack(side=LEFT)
    chat = Frame(fenetre3)  #creation de sous fenetres pour un positionnement plus simple
    chat.pack(side=BOTTOM)
##CONTACT
    scrollbar = Scrollbar(contact)   #Création et positionnement de la scrollbar
    scrollbar.pack( side = RIGHT, fill=Y)
    cont2 = Listbox(contact, yscrollcommand = scrollbar.set, height=30, width=30)
    cont=['Arthur','Samuel','Joris']

    for i in range(len(cont)):  #insertion des utilisateurs de la liste cont dans la listbox
        cont2.insert(END, cont[i])

    cont2.pack(side=TOP, fill=Y)
    scrollbar.config( command = cont2.yview)   #orientation de la scroll bar

    bsel = Button(contact, text ="sélectionner", command = sel, anchor=CENTER, pady=4, height=1, width=16)   #Création et positionnement du bouton pour selectionne un utilisateur
    bsel.pack(side = BOTTOM, fill=X)

    zchat = Entry(chat)   #Création et positionnement de la zone de chat
    zchat.pack(side=LEFT)

    benvoie = Button(chat, text ="Envoyer", command=envoie, anchor=CENTER, pady=4, height=1, width=7)   #Création et positionnement d'un bouton pour envoyer du texte
    benvoie.pack(side = RIGHT)

    fenetre3.mainloop()

fenetre.resizable(width=False, height=False) #non posibilité de modifier la taille de la fenêtre
fenetre.mainloop()
