# 1. Creer une instance de la classe 
# montre(un objet)
# 2. Afficher l'instance
# 3.afficher la marque de l'instance
# 4. Creer une seconde instance.
# REMARQUE : les instances ont les memes valeurs d' attibuts(attr ce classe)

class Montre:
    marque = "Rolex"
    style = "Equille"
    bracelet = "Cuir"


# 1)
montre_01 = Montre()
# 2)
print(montre_01)
# 3)
print(montre_01.marque)
# 4)
montre_02 = Montre()
print(montre_02)
print(montre_02.marque)
