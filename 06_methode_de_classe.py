# 1) On suppose que l'entreprise vend toutes 
# les marques de montre mais 90% des montres vendues
# sont des "Hublot" à aiguille en cuir et des TAG
# Heuer electronique en metal.

# Solution: Les methodes de class (avec le decorateur @classmethod)

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


    def afficher_heure(self):
        from datetime import datetime
        date = datetime.now()
        print(date.strftime("%H:%M:%S"))


m1 = Montre.Hublot()
m2 = Montre.TAGHeuer()


print(m1.marque)
