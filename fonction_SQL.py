import sqlite3
con = sqlite3.connect("MSMv1.db")

def createUserRegTable(): #fonction créant la table user
    cur = con.cursor()
    cur.execute("""CREATE TABLE User
    (p_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    pseudo TEXT NOT NULL)
    """)

def createDiscussionTable(): #fonction créant la table discusion
    cur = con.cursor()
    cur.execute("""CREATE TABLE Discussions
    (m_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    m_pseudo TEXT NOT NULL,
    m_contenu TEXT)
    """)

def writeMessage(contenu,pseudoUtilisateur): #fonction inscrivant un message et le nom de l'utilisateur dans la BDD
    params = (pseudoUtilisateur,contenu)
    cur = con.cursor()
    cur.execute("INSERT INTO Discussions(m_pseudo, m_contenu) VALUES(?, ?)",params)
    con.commit()

def requestMessage(nbMessage): #demande le contenu des n messages précédent
    cur = con.cursor()
    listMessages = cur.execute("SELECT m_contenu FROM Discussions ORDER BY m_ID DESC LIMIT 0, {}".format(nbMessage)).fetchall()
    return message

def requestPseudo(nbMessage): #demande les pseudos des n message précédent
    cur = con.cursor()
    listPseudos = cur.execute("SELECT m_pseudo FROM Discussions ORDER BY m_ID DESC LIMIT 0, {}".format(nbMessage)).fetchall()
    return listPseudos

def requestAll(nbMessage):#récupére le ccontenu et le pseudo des n messages précédents
    cur = con.cursor()
    listAll = cur.execute("SELECT * FROM Discussions ORDER BY m_ID DESC LIMIT 0,{}".format(nbMessage)).fetchall()
    return listAll

def infoUser(pseudoUtilisateur): #récupération des infos d'un utilisateur
    cur = con.cursor()
    info = cur.execute("SELECT * FROM User WHERE pseudo=pseudoUtilisateur").fetchall()
    return info

def verificationPseudo(pseudoUtilisateur):#vérifie si le pseudo est déja pris,renvoie un booléen
    i=0
    cur = con.cursor()
    b = cur.execute("SELECT pseudo FROM User ").fetchall()#on récupère une list de tuples
    for i in b :
        c = list(i)#on transforme le tuple en list
        d = str(c[0])#puis en string
        if pseudoUtilisateur == d :
            return True
    return False

def UserAdd(pseudoUtilisateur):#on ajoute un utilisateur à la BDD
    cur = con.cursor()
    cur.execute("INSERT INTO User (pseudo) VALUES (?)", (pseudoUtilisateur,))
    con.commit()

def delUser(pseudoUtilisateur):#supprimer un utilisateur par son pseudo
    cur = con.cursor()
    cur.execute("DELETE FROM User WHERE pseudo = (?)", (pseudoUtilisateur,))
    con.commit()

def printUser():#renvoie une list de tuples contenant tous les pseudos
    cur = con.cursor()
    listPseudo = cur.execute("SELECT pseudo FROM User").fetchall()
    return listPseudo
