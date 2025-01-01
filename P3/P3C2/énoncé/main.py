# Écrivez votre code ici !
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
with open("P3/P3C2/énoncé/index.html", 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

    # Récupérer le titre de la page
    title = soup.title.string
    print("Titre de la page :", title)

    # Récupérer le texte de la balise <h1> avec l'ID "titre"
    h1_titre = soup.find('h1', id='titre').string
    print("Texte de la balise <h1> :", h1_titre)

    # Récupérer les informations sur les produits
    produits = []
    product_list = soup.find_all('li', class_='product')
    
    for product in product_list:
        nom = product.find('h2').string
        prix = product.find('p', class_='price').string
        description = product.find_all('p')[1].string
        produits.append({
            "nom": nom,
            "prix": prix,
            "description": description
        })

    # Nettoyer les prix pour ne garder que le montant
    for produit in produits:
        prix_brut = produit['prix']  # Exemple: "Prix: 20€"
        prix_net = prix_brut.replace("Prix:", "").replace("€", "").strip()
        produit['prix'] = float(prix_net)  # Convertir en nombre

    # Convertir les prix en dollars
    for produit in produits:
        produit['prix_dollars'] = round(produit['prix'] * 1.2, 2)

    # Afficher les informations avec les prix en dollars
    print("\nProduits avec prix en dollars :")
    for produit in produits:
        print(f"Nom : {produit['nom']}")
        print(f"Prix en euros : {produit['prix']}€")
        print(f"Prix en dollars : {produit['prix_dollars']}$")
        print(f"Description : {produit['description']}\n")

    
