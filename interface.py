import tkinter as tk
from tkinter import messagebox
from gestion_recette import *

def ajouter_recette_interface():
    nom = entry_nom.get()
    ingredients = entry_ingredients.get()
    recette = entry_recette.get()
    categorie = entry_categorie.get()

    if not nom or not ingredients or not recette or not categorie:
        messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
        return

    ajouter_recette(nom, ingredients, recette, categorie)
    messagebox.showinfo("Succès", "Recette ajoutée avec succès.")
    afficher_liste_recettes_interface()

def supprimer_recette_interface():
    nom = entry_nom.get()
    if supprimer_recette(nom):
        messagebox.showinfo("Succès", "Recette supprimée avec succès.")
    else:
        messagebox.showerror("Erreur", "Recette non trouvée.")
    afficher_liste_recettes_interface()

def modifier_recette_interface():
    nom = entry_nom.get()
    recette = entry_recette.get()
    ingredients = entry_ingredients.get()
    categorie = entry_categorie.get()

    if modifier_recette(nom, recette, ingredients, categorie):
        messagebox.showinfo("Succès", "Recette mise à jour avec succès.")
    else:
        messagebox.showerror("Erreur", "Recette non trouvée.")
    afficher_liste_recettes_interface()

def afficher_recette_interface():
    nom = entry_nom.get()
    recette = afficher_recette(nom)
    if recette:
        messagebox.showinfo("Recette", f"Nom: {recette['nom']}\nIngrédients: {recette['ingredient']}\nRecette: {recette['recette']}\nCatégorie: {recette['categorie']}")
    else:
        messagebox.showerror("Erreur", "Recette non trouvée.")

def sauvegarder_donnees_interface():
    nom_fichier = entry_fichier.get()
    if not nom_fichier:
        messagebox.showerror("Erreur", "Le nom du fichier est requis.")
        return
    success = sauvegarder_donnees(nom_fichier)
    if success:
        messagebox.showinfo("Succès", "Données sauvegardées avec succès.")
    else:
        messagebox.showerror("Erreur", "Erreur lors de la sauvegarde.")

def charger_donnees_interface():
    nom_fichier = entry_fichier.get()
    if not nom_fichier:
        messagebox.showerror("Erreur", "Le nom du fichier est requis.")
        return
    success = charger_donnees(nom_fichier)
    if success:
        messagebox.showinfo("Succès", "Données chargées avec succès.")
        afficher_liste_recettes_interface()
    else:
        messagebox.showerror("Erreur", "Erreur lors du chargement.")

def afficher_liste_recettes_interface():
    listbox_recettes.delete(0, tk.END)
    recettes = obtenir_liste_recettes()
    for recette in recettes:
        listbox_recettes.insert(tk.END, f"{recette['nom']} ({recette['categorie']})")

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Gestion des Recettes")

# Créer les widgets
label_nom = tk.Label(fenetre, text="Nom de la recette")
entry_nom = tk.Entry(fenetre)
label_ingredients = tk.Label(fenetre, text="Ingrédients (séparés par un tiret)")
entry_ingredients = tk.Entry(fenetre)
label_recette = tk.Label(fenetre, text="Description de la recette")
entry_recette = tk.Entry(fenetre)
label_categorie = tk.Label(fenetre, text="Catégorie (entrées, plats, desserts)")
entry_categorie = tk.Entry(fenetre)
label_fichier = tk.Label(fenetre, text="Nom du fichier (pour sauvegarde et chargement)")
entry_fichier = tk.Entry(fenetre)

# Créer les boutons
btn_ajouter = tk.Button(fenetre, text="Ajouter une recette", command=ajouter_recette_interface)
btn_supprimer = tk.Button(fenetre, text="Supprimer une recette", command=supprimer_recette_interface)
btn_modifier = tk.Button(fenetre, text="Modifier une recette", command=modifier_recette_interface)
btn_afficher = tk.Button(fenetre, text="Afficher la recette", command=afficher_recette_interface)
btn_sauvegarder = tk.Button(fenetre, text="Sauvegarder", command=sauvegarder_donnees_interface)
btn_charger = tk.Button(fenetre, text="Charger", command=charger_donnees_interface)

# Liste des recettes (affichage)
listbox_recettes = tk.Listbox(fenetre, height=10, width=50)

# Placer les widgets dans la fenêtre
label_nom.grid(row=0, column=0, padx=10, pady=5)
entry_nom.grid(row=0, column=1, padx=10, pady=5)
label_ingredients.grid(row=1, column=0, padx=10, pady=5)
entry_ingredients.grid(row=1, column=1, padx=10, pady=5)
label_recette.grid(row=2, column=0, padx=10, pady=5)
entry_recette.grid(row=2, column=1, padx=10, pady=5)
label_categorie.grid(row=3, column=0, padx=10, pady=5)
entry_categorie.grid(row=3, column=1, padx=10, pady=5)
label_fichier.grid(row=4, column=0, padx=10, pady=5)
entry_fichier.grid(row=4, column=1, padx=10, pady=5)

btn_ajouter.grid(row=5, column=0, padx=10, pady=5)
btn_supprimer.grid(row=5, column=1, padx=10, pady=5)
btn_modifier.grid(row=6, column=0, padx=10, pady=5)
btn_afficher.grid(row=6, column=1, padx=10, pady=5)
btn_sauvegarder.grid(row=7, column=0, padx=10, pady=5)
btn_charger.grid(row=7, column=1, padx=10, pady=5)

listbox_recettes.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Lancer l'application
fenetre.mainloop()
