import json

# Liste des recettes (initialement vide)
recettes = []

def ajouter_recette(nom, ingredients, recette, categorie):
    nouvelle_recette = {'nom': nom, 'ingredient': ingredients, 'recette': recette, 'categorie': categorie}
    recettes.append(nouvelle_recette)

def supprimer_recette(nom):
    for recette in recettes:
        if recette['nom'] == nom:
            recettes.remove(recette)
            return True
    return False

def modifier_recette(nom, nouvelle_recette, nouveaux_ingredients, nouvelle_categorie):
    for recette in recettes:
        if recette['nom'] == nom:
            recette['recette'] = nouvelle_recette
            recette['ingredient'] = nouveaux_ingredients
            recette['categorie'] = nouvelle_categorie
            return True
    return False

def afficher_recette(nom):
    for recette in recettes:
        if recette['nom'] == nom:
            return recette
    return None

def sauvegarder_donnees(nom_fichier):
    try:
        with open(nom_fichier, mode='w', encoding='utf-8') as fichier:
            json.dump(recettes, fichier, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        return False, str(e)

def charger_donnees(nom_fichier):
    try:
        with open(nom_fichier, mode='r', encoding='utf-8') as fichier:
            global recettes
            recettes = json.load(fichier)
        return True
    except Exception as e:
        return False, str(e)

def obtenir_liste_recettes():
    return recettes