class Montre:
    nbre_montre = 0
    def __init__(self,marque, style,bracelet):
        print("Creation d'une montre")
        self.marque = marque
        self.style = style
        self.bracelet = bracelet
        Montre.nbre_montre += 1
    def afficher_heure(self):
        from datetime import datetime
        date = datetime.now()
        print(date.strftime("%H:%M:%S"))
    

m = Montre("Hublot","Electro","Cuir")

Montre.afficher_heure(m)
print(m.afficher_heure())