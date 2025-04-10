"Dossier vide"
# Bienvenue au projet numéro 5 !
# Ce projet supprimera tout dossier vide dans la zone 'Downloads'.
# Je recommande d'utiliser le planificateur de tâches (Windows)
# pour une meilleure expérience 👍.

# Welcome to project number 5!
# This project will delete any empty folder in the 'Downloads' area.
# I recommend using the task scheduler (Windows)
# for a better experience 👍.

import os

voie_de_downloads = os.path.expanduser("~/Downloads")

for root, dirs, files in os.walk(voie_de_downloads, topdown=False):
    if os.path.isdir(root) and not os.listdir(root):
        os.rmdir(root)
        print(f"Dossier supprimé: {root}")
