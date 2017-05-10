from tkinter import*
import tkinter.messagebox

pseudotest='arthur'
mdptest='123'

def go():
   a=pseudo.get()
   if a!='':
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
##pseudo
pseudal = Frame(fenetre)
pseudal.pack()
psn = Label(pseudal, text="Pseudo:", pady=4)
psn.pack(side = LEFT)
pseudo = Entry(pseudal)
pseudo.pack(side = RIGHT)
##verif pseudo/mdp


fenetre.resizable(width=False, height=False)
fenetre.mainloop()
