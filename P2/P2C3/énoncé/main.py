# Ecrivez votre code ici
def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12

def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees

saisie_salaire_annuel = float(input("Entrez votre salaire annuel : "))
saisie_heures_travaillees = float(input("Entrez le nombre d'heures travaillées par semaine : "))

mensuel = salaire_mensuel(saisie_salaire_annuel)
hebdomadaire = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdomadaire, saisie_heures_travaillees)

print(f"Votre salaire horaire est de {horaire} euros")