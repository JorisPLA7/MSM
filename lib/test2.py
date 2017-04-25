Salut Sam, je vais avoir besoin de ces fonctions là :


Class ClientsStatus():
    def __init__(self):
        self.ClientsList = {}

    def ListAll(self):
        return TrucMuche
    def Refresh(self, PseudoUtilisateur, RawData):
        return TrucMuche
    def UserDel(self, PseudoUtilisateur):
        return TrucMuche
    def UserAdd(self, PseudoUtilisateur, RawData):
        #TrucMuche
    def ExisteTIlUnUntilisateurAppele(self, PseudoUtilisateur):
        return #bool
    def DisMoiToutAProposDe(self, PseudoUtilisateur):
        return RawData

dans la table il me faudrait comme données accessibles :
    PseudoUtilisateur, chaine <= 50 char
    Droits, un entier <=777
    EtatClient, un booleen
    Client, une chaine qui ressemble à ça :
        <socket.socket fd=540, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 55664)>
        donc assez longue

quand je te soumettrais RawData, ce sera ces données sous forme d'une liste (ou dico comme tuv) dans cet ordre , et il fautdrait que tu me les restitues sans modifications
exemple :

RawData = (Joris, 753, 1, <socket.socket fd=540, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 55664)>)
et par exemple dans Refresh si je te donne la liste
    (Joris, ?, ?, <socket.socket fd=540, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 55664)>)
alors ça veut dire que je ne veut pas modifier ces données.
