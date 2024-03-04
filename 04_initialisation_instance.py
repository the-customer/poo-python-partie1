# 1) Creation de la methode __init__:
    # Cette methode est appelee a chaque fois qu'on cree une instance


class Montre:
    nbre_montre = 0
    def __init__(self,marque, style,bracelet):
        print("Creation d'une montre")
        self.marque = marque
        self.style = style
        self.bracelet = bracelet
        Montre.nbre_montre += 1
    


m1 = Montre("Hublot","Electro","Cuir")
# print(Montre.marque) ❌
print(m1.marque) #✅

m2 = Montre("Tag Heuer","Electro","or")