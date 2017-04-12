import sqlite3
con = sqlite3.connect("MSMv0.2.db")

def createUserRegTable(): #fonction créant la table user
    cur = con.cursor()
    cur.execute("""CREATE TABLE User
    (p_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    pseudo TEXT NOT NULL UNIQUE,
    motDePasse TEXT NOT NULL,
    admin BOOLEAN NOT NULL)
    """)

def createDiscussionTable(): #fonction créant la table discusion
    cur = con.cursor()
    cur.execute("""CREATE TABLE Discussions
    (m_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    m_pseudo TEXT NOT NULL,
    m_contenu TEXT)
    """)

def writeMessage(contenu,pseudo):
    params = (pseudo,contenu)
    cur = con.cursor()
    cur.execute("INSERT INTO Discussions(m_pseudo, m_contenu) VALUES(?, ?)",params)
    con.commit()

def requestMessage(nbMessage): #demande le contenu des n messages précédent
    cur = con.cursor()
    listMessages = cur.execute("SELECT m_contenu FROM Discussions ORDER BY m_ID DESC LIMIT 0, {}".format(nbMessage))
    return message

def requestPseudo(nbMessage): #demande les pseudos des n message précédent
    cur = con.cursor()
    listPseudos = cur.execute("SELECT m_pseudo FROM Discussions ORDER BY m_ID DESC LIMIT 0, {}".format(nbMessage))
    return listPseudos
