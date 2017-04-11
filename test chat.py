from tkinter import*

fenetre3 = Tk()
fenetre3.wm_title("test chat")
chat = Frame(fenetre3)
chat.pack(side=BOTTOM,fill=Y)

##conversation

test=2
A="Samuel"
B="Arthur"
bb="C'est toi le noob !"

if test==1:
    nuser1 = LabelFrame(fenetre3, text=A) 
    nuser1.pack()
    tuser1 = Label(nuser1, text=aa)
    tuser1.pack()
if test==2:
    nuser2 = LabelFrame(fenetre3, text=B) 
    nuser2.pack()
    tuser2 = Label(nuser2, text=bb)
    tuser2.pack()

##chat

def envoie(event):
    global zchat
    aa=zchat.get()
    nuser1 = LabelFrame(fenetre3, text=A) 
    nuser1.pack()
    tuser1 = Label(nuser1, text=aa)
    tuser1.pack()
    zchat.destroy()
    zchat = Entry(chat)
    zchat.pack(side=LEFT, fill=Y)
    
fenetre3.bind("<Return>", envoie)


zchat = Entry(chat)
zchat.pack(side=LEFT, fill=Y)

benvoie = Button(chat, text ="Envoyer", command=envoie, anchor=CENTER, pady=4, height=1, width=7)
benvoie.pack(side = RIGHT)

chat.pack(side=BOTTOM,fill=Y)
fenetre3.mainloop()