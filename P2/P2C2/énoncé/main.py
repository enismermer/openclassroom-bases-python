# Ecrivez votre code ici !
nombres = input('Entrez une liste de nombres : ')

liste = nombres.split(',')
print("Liste des nombres", liste)

liste_entiers = []
for nombre in liste:
    nombre_entier = int(nombre)
    liste_entiers.append(nombre_entier)


somme = sum(liste_entiers)
print(f"La somme est : {somme}")

moyenne = somme / len(liste_entiers)
print(f"La moyenne est : {moyenne}")

nombre_au_dessus_moyenne = 0
for nombre in liste_entiers:
    if nombre > moyenne:
        nombre_au_dessus_moyenne += 1
print(f"Nombre de nombres supérieurs à la moyenne est : {nombre_au_dessus_moyenne}")
