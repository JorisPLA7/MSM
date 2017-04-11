from tkinter import*
import tkinter.messagebox

pseudotest='arthur'
mdptest='123'

def go():
   a=pseudo.get()
   b=ip.get()
   c=mdp2.get()
   if a==pseudotest and c==mdptest:
      fenetre.destroy()
   else:
      messagebox.showinfo("ERREUR", "Il semble que votre pseudo ou mot de passe soit incorrect.")

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