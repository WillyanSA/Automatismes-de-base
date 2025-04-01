"Organisateur de fichiers."
# Bonjour, c'est ma première automatisation, le but est d'automatiser
# l'organisation des fichiers sur le PC !

import os
import shutil

dossier_downloads = os.path.expanduser("~/Downloads")

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".odt", ".txt", ".pptx", ".xlsx"],
    "Musique": [".mp3", ".wav", ".ogg"],
    "Vidéos": [".mp4", ".avi", ".mov", ".mkv"],
    "Exécutable": [".exe", ".msi", ".sh"],
    "Compressible": [".rar", ".zip", ".tar", ".gz"],
    "Autre": [] # Fichiers qui n'entrent pas dans les catégories précédentes.
}

# Créer les dossiers s'ils n'existent pas
for dossier in categories.keys():
    maniere_dossier = os.path.join(dossier_downloads, dossier)
    os.makedirs(maniere_dossier, exist_ok = True )

# Organiser les fichers.
for fichier in os.listdir(dossier_downloads):
    maniere_dossier = os.path.join(dossier_downloads, fichier)

    # Ignore les dossiers (fichier de traitement uniquement).
    if os.path.isdir(maniere_dossier):
        continue

    # Prenez l'extension du fichier et convertissez-la en minuscules
    _, extension = os.path.splitext(fichier)
    extension = extension.lower()

    # Définir la catégorie par défaut sur « Autre »
    destination = os.path.join(dossier_downloads, "Autre")
    for categorie, extensions in categories.items():
        if extension in extensions:
            destination = os.path.join(dossier_downloads, categorie)
            break

    # Déplacer le fichier dans le dossier correspondant.
    shutil.move(maniere_dossier, destination)
    print(f"Déplacé: {fichier} -> {destination}.")

print("📂 Organisation achevée.")
