#!/usr/bin/python3.2
# -∗- coding: utf-8 -∗-
import socket # on importe le module
import threading
import time
from tkinter import*
import tkinter.messagebox

fenetre = Tk()
fenetre.wm_title("MSM (login)")

global Sock
global MyNet
class Net ():
    def __init__(self,Host, Port, Nickname, Pass):
        self.Host = socket.gethostbyname(Host)
        self.Port = Port
        self.Nickname = Nickname
        self.NickLen = str(len(self.Nickname))
        self.Pass = Pass
        self.Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on cree notre socket

    def Authenticate(self):
        data = bytes("AUT" + self.NickLen + self.Nickname, 'utf8')
        self.Sock.connect((self.Host,self.Port)) # on se connecte sur le serveur avec les informations données
        self.Sock.send(data)

    def Disconnect(self):
        print("Disconnected", sep=' ')

    def SendMsg(self, msg):
        data = bytes(msg, 'utf8') # on rentre des donnees
        self.Sock.send(data) # on envoie ces donnees

    def WhoAmI(self):
        return self.Nickname

##phase de login
def go():   #def bouton
   if pseudo.get()=='':
      messagebox.showinfo("ERREUR", "Il semble que votre pseudo ou mot de passe soit incorrect ou invalide.")
   elif mdp2.get()=='':
      messagebox.showinfo("ERREUR", "Il semble que votre pseudo ou mot de passe soit incorrect ou invalide.")
   elif ip.get()!='127.0.0.1':
      messagebox.showinfo("ERREUR", "Il semble que l'adresse ip soit invalide.")
   else:
      Nickname=pseudo.get()
      Host=ip.get()
      Pass=mdp2.get()
      Port = 8082
      fenetre.destroy()
      MyNet = Net(Host, Port , Nickname, Pass)
      MyNet.Authenticate()
      time.sleep(1) #will sleep for 5 seconds
      MyNet.SendMsg("ça croustille")
      print(MyNet.WhoAmI())

fenetre = Tk()
fenetre.wm_title("MSM (login)")

titre = Label(fenetre, text="MSM", width=30, height=10, anchor=CENTER)  #titre+bouton

titre.pack(side=TOP)

bsal = Frame(fenetre)
bsal.pack(side=BOTTOM)
bgo = Button(bsal, text ="GO", command = go, anchor=CENTER, pady=4, height=3, width=15)
bgo.pack(side = BOTTOM)

ipsal = Frame(fenetre)  #ip
ipsal.pack()
ipn = Label(ipsal, text="Ip:", pady=4, padx=16)
ipn.pack(side = LEFT)
ip = Entry(ipsal)
ip.pack(side=RIGHT)

pseudal = Frame(fenetre)    #pseudo
pseudal.pack()
psn = Label(pseudal, text="Pseudo:", pady=4)
psn.pack(side = LEFT)
pseudo = Entry(pseudal)
pseudo.pack(side = RIGHT)

mdp = Frame(fenetre)    #mdp
mdp.pack()
mdp1 = Label(mdp, text="Mot de passe:", pady=4)
mdp1.pack(side = LEFT)
mdp2 = Entry(mdp, show='*')
mdp2.pack(side = RIGHT)

fenetre.resizable(width=False, height=False)    #empecher redimention fenetre
fenetre.mainloop()

# On est connecte, on fait une boucle infinie d'inputs pour l'envoi des messages :