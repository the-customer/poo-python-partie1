# 1. Declarer deux instances de la classe montre
# 2. Modifier la marque de la classe Montre
# 3. Modifier la marque pour chaque instance
# REMQARQUE: le changement d'etat d'un attribut d'une 
# classe affecte toutes ses instances 
class Montre:
    marque = "Rolex"
    style = "Equille"
    bracelet = "Cuir"

# 1)
montre_01 = Montre()
montre_02 = Montre()
print(montre_01.marque)
print(montre_02.marque)
print("--------------------------------")
# 2)
Montre.marque = "Hublot"
print(montre_01.marque)
print(montre_02.marque)
print("--------------------------------")
# 3)
montre_01.marque = "Omega"
montre_02.marque = "Tag Heuer"
print(montre_01.marque)
print(montre_02.marque)
print("--------------------------------")

