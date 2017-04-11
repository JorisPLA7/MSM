from tkinter import*

def save():
    a=pseudo.get()
    b=prenom.get()
    c=nom2.get()
    e=mdp2.get()
    f=jour.get()
    g=mois.get()
    h=année.get()

inscription = Tk()
inscription.wm_title("MSM (inscription)")
##pseudo
pseudal = Frame(inscription)
pseudal.pack()

psn = Label(pseudal, text="Pseudo:", pady=4)
psn.pack(side = LEFT)
pseudo = Entry(pseudal)
pseudo.pack(side = RIGHT)
##prénom
prénom = Frame(inscription)
prénom.pack()

prn = Label(prénom, text="Prénom:", pady=4)
prn.pack(side = LEFT)
prenom = Entry(prénom)
prenom.pack(side = RIGHT)
##nom
nom = Frame(inscription)
nom.pack()

nom1 = Label(nom, text="NOM:", pady=4)
nom1.pack(side = LEFT)
nom2 = Entry(nom)
nom2.pack(side = RIGHT)
##mdp
mdp = Frame(inscription)
mdp.pack()

mdp1 = Label(mdp, text="Mot de passe:", pady=4)
mdp1.pack(side = LEFT)
mdp2 = Entry(mdp, show='*')
mdp2.pack(side = RIGHT)
##date de naissance
jourf = Frame(inscription)
jourf.pack()
jour = Spinbox(jourf, from_=1, to=31)
jour.pack(side=RIGHT)
journ = Label(jourf, text="Jour:", pady=4)
journ.pack(side = LEFT)

moisf = Frame(inscription)
moisf.pack()
mois = Spinbox(moisf, from_=1, to=12)
mois.pack(side=RIGHT)
moisn = Label(moisf, text="Mois:", pady=4)
moisn.pack(side = LEFT)

annéef = Frame(inscription)
annéef.pack()
année = Spinbox(annéef, from_=1920, to=2000)
année.pack(side=RIGHT)
annéen = Label(annéef, text="Année:", pady=4)
annéen.pack(side = LEFT)



bsave = Button(inscription, text ="SAVE", command = save, anchor=CENTER, pady=4, height=3, width=15)
bsave.pack(side = BOTTOM)

inscription.mainloop()
