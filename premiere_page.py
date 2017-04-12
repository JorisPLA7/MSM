from tkinter import*
import tkinter.messagebox
import sqlite3
con = sqlite3.connect("MSMv0.2.db")

def createUserRegTable(): #fonction créant la table user
    cur = con.cursor()
    cur.execute("""CREATE TABLE User
    (p_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    pseudo TEXT NOT NULL UNIQUE,
    motDePasse TEXT NOT NULL,
    admin BOOLEAN NOT NULL,
    IP TEXT NOT NULL)
    """)

def go():
   if pseudo.get()=='':
       messagebox.showinfo("ERREUR", "Il semble que votre pseudo ou mot de passe soit incorrect ou invalide.")
   elif mdp2.get()=='':
       messagebox.showinfo("ERREUR", "Il semble que votre pseudo ou mot de passe soit incorrect ou invalide.")
   elif ip.get()!='127.0.0.1':
      messagebox.showinfo("ERREUR", "Il semble que l'adresse ip soit invalide.")
   else:
       cur = con.cursor()
       Nickname=pseudo.get()
       Host=ip.get()
       Pass=mdp2.get()
       Port = 8082
       params=(Nickname,Pass,False,Host)
       cur.execute("INSERT INTO User(pseudo, motDePasse, admin, IP) VALUES(?, ?, ?, ?)",params)
       con.commit()
       fenetre.destroy()

#createUserRegTable()

fenetre = Tk()
fenetre.wm_title("MSM (login)")
##titre+bouton
titre = Label(fenetre, text="MSM", width=30, height=10, anchor=CENTER)
titre.pack(side=TOP)

bsal = Frame(fenetre)
bsal.pack(side=BOTTOM)
bgo = Button(bsal, text ="GO", command = go, anchor=CENTER, pady=4, height=3, width=15)
bgo.pack(side = BOTTOM)
##ip
ipsal = Frame(fenetre)
ipsal.pack()
ipn = Label(ipsal, text="Ip:", pady=4, padx=16)
ipn.pack(side = LEFT)
ip = Entry(ipsal)
ip.pack(side=RIGHT)
##pseudo
pseudal = Frame(fenetre)
pseudal.pack()
psn = Label(pseudal, text="Pseudo:", pady=4)
psn.pack(side = LEFT)
pseudo = Entry(pseudal)
pseudo.pack(side = RIGHT)
##mdp
mdp = Frame(fenetre)
mdp.pack()
mdp1 = Label(mdp, text="Mot de passe:", pady=4)
mdp1.pack(side = LEFT)
mdp2 = Entry(mdp, show='*')
mdp2.pack(side = RIGHT)
##verif pseudo/mdp


fenetre.resizable(width=False, height=False)
fenetre.mainloop()
