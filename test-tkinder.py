import tkinter as tk  # Importation de la bibliothèque tkinter pour créer l'interface graphique.
from tkinter import messagebox  # Importation de messagebox pour afficher des boîtes de dialogue (bien que non utilisée ici).
from tkinter import *  # Importation de tous les éléments de tkinter (ce qui n'est pas recommandé, car cela peut entraîner des conflits de noms).
import requests
import random

def dico():
    url = "http://109.10.114.61/300_mots_pendus.txt"
    response = requests.get(url)        
    liste = response.text.splitlines()
    mot = random.choice(liste)
    return mot

fenetre = Tk()  # Création de la fenêtre principale de l'application.
fenetre.title('Liste de tâches')  # Définition du titre de la fenêtre.
fenetre.geometry("600x600+200+50")  # Définition de la taille de la fenêtre (600x600 pixels) et de sa position (200, 50).
fenetre.resizable(height=True, width=True)  # Autorisation de redimensionner la fenêtre en hauteur et largeur.

listbox = tk.Listbox(fenetre, font=("Arial", 12), selectbackground="#4286f4", selectforeground="white")  # Création d'une Listbox pour afficher les tâches, avec une police spécifique et des couleurs pour la sélection.
listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)  # Placement de la Listbox dans la fenêtre avec des espacements et une extension pour occuper tout l'espace disponible.

entry = tk.Entry(fenetre)  # Création d'un champ de saisie (Entry) pour que l'utilisateur entre des tâches.
entry.pack(pady=5, padx=10)  # Placement du champ de saisie dans la fenêtre avec un espacement autour.

frame_boutons = tk.Frame(fenetre)  # Création d'un cadre (Frame) pour contenir les boutons.
frame_boutons.pack(pady=5)  # Placement du cadre de boutons avec un espacement.

def ajouter_tache():
    tache = dico()  # Récupération du texte saisi dans le champ de saisie.
    for i in range(len(tache)):
        listbox.insert(tk.END,"_")  # Ajouter la tâche à la fin de la Listbox.
    
ajouter_tache()

fenetre.mainloop()
