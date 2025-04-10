"Renommer des fichiers"
# Bonjour à nouveau, voici le projet numéro 6 !
# Ce projet renommera tous les fichiers de la zone de téléchargement.
# Je recommande d'utiliser celui-ci avec « Organisateur de fichiers »

# Hello again, this is project number 6!
# This project will rename all files in the Downloads area.
# I recommend using this one with "Organisateur de fichiers"

import os

downloads_repertoire = os.path.expanduser("~/Downloads")

compteur = {
    "Images": 1,
    "Documents": 1,
    "Musique": 1,
    "Vidéos": 1,
    "Exécutable": 1,
    "Compressible": 1,
    "Autre": 1
}

for root, dirs, fichiers in os.walk(downloads_repertoire, topdown=False):
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".odt", ".txt", ".pptx", ".xlsx"],
        "Musique": [".mp3", ".wav", ".ogg"],
        "Vidéos": [".mp4", ".avi", ".mov", ".mkv"],
        "Exécutable": [".exe", ".msi", ".sh"],
        "Compressible": [".rar", ".zip", ".tar", ".gz"],
        "Autre": []
    }
    for fichier in fichiers:
        _, extension = os.path.splitext(fichier)

        if extension in categories["Images"]:
            nouveau_nom = f"image_{compteur['Images']}{extension}"
            compteur["Images"] += 1

        elif extension in categories["Documents"]:
            nouveau_nom = f"document_{compteur['Documents']}{extension}"
            compteur["Documents"] += 1

        elif extension in categories["Musique"]:
            nouveau_nom = f"musique_{compteur['Musique']}{extension}"
            compteur["Musique"] += 1

        elif extension in categories["Vidéos"]:
            nouveau_nom = f"vidéo_{compteur['Vidéos']}{extension}"
            compteur["Vidéos"] += 1

        elif extension in categories["Exécutable"]:
            nouveau_nom = f"exécutable_{compteur['Exécutable']}{extension}"
            compteur["Exécutable"] += 1

        elif extension in categories["Compressible"]:
            nouveau_nom = f"compressible_{compteur['Compressible']}{extension}"
            compteur["Compressible"] += 1

        else:
            nouveau_nom = f"autre_{compteur['Autre']}{extension}"
            compteur["Autre"] += 1

        ancien_chemin = os.path.join(root, fichier)
        nouveau_chemin =  os.path.join(root, nouveau_nom)
        os.rename(ancien_chemin, nouveau_chemin)
        print(f"{fichier} ➜ {nouveau_nom}")

        

            




    
    

