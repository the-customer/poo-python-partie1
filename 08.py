class Montre:
    nbre_montre = 0
    def __init__(self,marque, style,bracelet):
        print("Creation d'une montre")
        self.marque = marque
        self.style = style
        self.bracelet = bracelet
        Montre.nbre_montre += 1
    
    @classmethod
    def Hublot(clss):
        return clss("Hublot","Aiguille","Cuir")
    @classmethod
    def TAGHeuer(clss):
        return clss("TAG Heuer","Electonique","Metal")
    @staticmethod
    def printCount():
        return "Le nombre de montre cree est : {}".format(Montre.nbre_montre)
    
    def afficher_heure(self):
        from datetime import datetime
        date = datetime.now()
        print(date.strftime("%H:%M:%S"))
    def __str__(self) -> str:
        return "Montre : {} - {} - {}".format(self.marque,self.style,self.bracelet)

m1 = Montre("Casio","Aiguille","Metal")

print(m1)