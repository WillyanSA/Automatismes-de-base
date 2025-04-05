"Nettoyeur de fichiers temporaires"

# Bonjour, c'est ma deuxième automatisation avec de l'aide, 
# c'est un nettoyeur de fichiers temporaires.

import os # Bibliothèque pour gérer les fichiers et les dossiers
import shutil # Bibliothèque pour supprimer des répertoires entiers

# Répertoires de fichiers temporaires communs sous Windows
temp_dirs = [
    os.path.expandvars(r"%TEMP%"), # Dossier temporaire de l'utilisateur
    os.path.expandvars(r"C:\Users\User\AppData\Local\Temp") # Dossier temporaire du système
]

def nettoyer_temp():
    total_libere = 0 # Variable pour stocker l'espace libéré
    
    for temp_dir in temp_dirs: # Faites défiler chaque répertoire de la liste
        if os.path.exists(temp_dir): # Vérifier que le dossier existe
            print(f"Nettoyage: {temp_dir}")
            
            for root, dirs, fichiers in os.walk(temp_dir, topdown=False): # Faire les fichier et les dossiers
                for fichier in fichiers:
                    fichier_path = os.path.join(root, fichier) # Chemin d'accès complet au fichier
                    try:
                        total_libere += os.path.getsize(fichier_path) # Additionnez la taille du fichier
                        os.remove(fichier_path) # Suprimmez le fichier
                    except Exception as e: # pylint: disable=broad-exception-caught
                        print(f"Il n'a pas été possible d'exclure {fichier_path}: {e}") # Message d'erreur
                for dossier in dirs:
                    dossier_path = os.path.join(root, dossier) # Chemin complet dans le dossier
                    try:
                        shutil.rmtree(dossier_path) # Supprimer le dossier
                    except Exception as e: # pylint: disable=broad-exception-caught
                        print(f"Erreur de suppression {dossier_path}: {e}") # Message d'erreur

    print(f"\n🗑️ Espace potentiellment libre: {total_libere / (1024 * 1024): .2f} MB")

if __name__ == "__main__":
    nettoyer_temp() # Assure la fonction de nettoyage
