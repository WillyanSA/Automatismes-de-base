"Inventaire TXT"
# Ce projet :
# Lire le dossier ~/Downloads
# Lister tous les fichiers trouvés (pas da dossier)
# Créer ou écraser un fichier appéle Inventaire.txt dans la dossier Downloads.
# Écrire dans ce fichier .txt le nom de chaque fichier trouvé, un par ligne.
# --------------------------------------------------------------------------------
# This project:
# Read the ~/Downloads folder
# List all files found (no folders)
# Create or overwrite a file called inventory.txt inside the Downloads folder
# Write in this .txt the name of each file found, one per line

import os 

localisation = os.path.expanduser("~/Downloads")

chemin_du_fichier = os.path.join(localisation, "Inventaire.txt")

fichiers_trouves = []

for root, dirs, fichiers in os.walk(localisation):   
    for fichier in fichiers:
        if fichier != "Inventaire.txt":
            fichiers_trouves.append(fichier)

with open (chemin_du_fichier, "w", encoding="utf-8") as f:
    for nom in fichiers_trouves:
        f.write(nom + "\n")

print("📄 Inventaire.txt créé avec succès.")



