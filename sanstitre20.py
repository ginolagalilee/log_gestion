# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 18:55:59 2025

@author: hp EliteBook 850 G6
"""

import json

recettes = []

# 1. Ajouter une recette
def ajouter_recette():
    nom = input("Entrez le nom de la recette : ")
    #petite des
    ingredient= input("Liste des ingredients (separer les ingredients par un tiret): ")
    recette = input("description de la recette de cuisine: ")
    categorie=input("Entrez la categorie de la recette: (entrées, plats, desserts): ")
    recette = {'nom': nom, 'ingredient': ingredient, 'recette': recette,'categorie': categorie}
    recettes.append(recette)
    print("Recette ajouté avec succès.")
    
    return

# 2. Supprimer une recette
def supprimer_recette():
    nom = input("Entrez le nom de la recette :")
    for recette in recettes:
        if recette['nom'] == nom:
            recettes.remove(recette)
            print("Recette supprimée avec succès.")
            return
    print("Erreur : Recette introuvable.")

# 3. Modifier la recette
def modifier_recette():
    nom = input("Entrez le nom de la recette à modifier : ")
    for recette in recettes:
        if recette['nom'] == nom:
                nouvelle_recette = input("Entrez la nouvelle recette : ")
                recette['recettes'] = nouvelle_recette
                print("Recette mise à jour avec succès.")
                return

    print("Erreur : Recette introuvable.")


# 4. Afficher la liste des recettes
def afficher_liste_recette():
    if not recettes:
        print("Aucune recette à afficher.")
        return
    print("\nListe des recettes :")
    for recette in recettes:
        print(f"{recette['nom']} ")
        
        
# 5. Afficher une recette
def afficher_recette():
    if not recettes:
        print("Aucune recette à afficher.")
        return
    nom = input("Entrez le nom de la recette :")
    for recette in recettes:
        if recette['nom'] == nom:
            print(f"\nRecette {recette['nom']} {recette['categorie']} {recette['ingredient']} {recette['recette']}")


# 6. Sauvegarder les données dans un fichier
def sauvegarder_donnees():
    nom_fichier = input("Entrez le nom du fichier pour sauvegarder (ex: Recette.json) : ")
    try:
        # Ouverture du fichier en mode écriture
        with open(nom_fichier, mode='w') as fichier:
            # Conversion de la liste de recettes en format JSON et écriture dans le fichier
            json.dump(recettes, fichier, indent=4, ensure_ascii=False)
        
        print("Données sauvegardées avec succès.")
    
    except Exception as e:
        print("Erreur lors de la sauvegarde :", e)

# 7 Charger les données depuis un fichier

def charger_donnees():
    nom_fichier = input("Entrez le nom du fichier à charger (ex: recettes.json) : ")
    try:
        # Ouverture du fichier en mode lecture
        with open(nom_fichier, mode='r', encoding='utf-8') as fichier:
            # Charger les données JSON du fichier dans la variable globale recettes
            global recettes  # On utilise la variable globale
            recettes = json.load(fichier)
        
        print("Données chargées avec succès.")

    except FileNotFoundError:
        print("Erreur : Fichier introuvable.")
    except json.JSONDecodeError:
        print("Erreur : Le fichier n'est pas un fichier JSON valide.")

        
def menu():
    while True:
        print("\n--- Système de Gestion des Recettes ---")
        print("1. Ajouter une recette")
        print("2. Supprimer une recette")
        print("3. Modifier une recette")
        print("4. Afficher la liste complete des recettes")
        print("5. Afficher la  recette")
        print("6.Sauvegarder les données dans un fichier")
        print("7. Charger les données depuis un fichier")
        print("0. Quitter")
        print("\n--- Tableau des Recettes ---")
        
        for recette in recettes[:5]:
            print(f"   {recette['nom']}   |   {recette['categorie']}")
        
        choix = input("Entrez votre choix : ")
        
        if choix == '1':
            ajouter_recette()
        elif choix == '2':
            supprimer_recette()
        elif choix == '3':
            modifier_recette()
        elif choix == '4':
            afficher_liste_recette()
        elif choix == '5':
            afficher_recette()
        elif choix == '6':
            sauvegarder_donnees()
        elif choix == '7':
            charger_donnees()
        elif choix == '0':
            print("Merci d'avoir utilisé le système de gestion des recettes. Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

# Exécuter le menu
menu()