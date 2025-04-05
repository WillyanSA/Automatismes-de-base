"Organisateur de taille"
# Il s'agit d'un projet qui lit les fichiers et indique leur taille.
# This is a project that reads the files and says their size.
# Petit (<1mb)   | Small (<1mb))
# Moyen (1-10mb) | Medium (1-10mb)
# Grand (>10mb)  | Big (>10mb)
# Utilisation recommandée avec le projet « organisateur de fichiers »
# Use recommended with the "organisateur de fichiers" project
import os

localisation_des_fichiers = os.path.expanduser("~/Downloads")

for root, dirs, fichiers  in os.walk(localisation_des_fichiers):
    for fichier in fichiers:
        chemin_complet = os.path.join(root, fichier)
        taille = os.path.getsize(chemin_complet)
        
        if taille < 1_000_000:
            taille_affichable = f"{round(taille / 1_000, 2)} Kb"
            categorie = "Petit / Small"
        elif taille <= 10_000_000:
            taille_affichable = f"{round(taille / 1_000_000, 2)} Mb"
            categorie = "Moyen / Medium"
        else:
            taille_affichable = f"{round(taille / 1_000_000, 2)} Mb"
            categorie = "Grand / Big"

        print(f"{fichier} - {categorie} ({taille_affichable})")
