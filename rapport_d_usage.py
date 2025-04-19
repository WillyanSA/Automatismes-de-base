"Rapport d'usage"
# Vérifie l'utilisation du disque ou l'unité centrale
# Enregistre ces information dans un fichier .txt ou .csv
# Tout a long de la semaine, il génère un jornal quotidien automatique
# A la fin de la semaine, vous recevez un rapport d'activité.

# Checks disk or CPU usage
# Records this information in a .txt or .csv file
# Throughout the week, it generates an automatic daily log
# At the end of the week, you have an activity report

import psutil
import os
from datetime import datetime

dossier_downloads = os.path.expanduser("~/Downloads/Documents")

# Créer le dossier s'il n'existe pas
maniere = os.path.join(dossier_downloads, "Rapport d'usage")
os.makedirs(maniere, exist_ok = True)

aujourdhui = datetime.now()

nom_fichier = aujourdhui.strftime("%Y-%m-%d") + ".txt"
chemin_du_fichier = os.path.join(maniere, nom_fichier)

with open(chemin_du_fichier, 'w', encoding = "utf-8") as fichier:
    fichier.write(f"📅 Date: {aujourdhui.strftime('%Y-%m-%d')}\n")
    fichier.write(f"🕒 Heure: {aujourdhui.strftime('%H-%M-%S')}\n\n")

    disque = psutil.disk_usage('C:\\')
    fichier.write(f"💽 Espace total: {disque.total / (1024 ** 3):.2f} GB \n")
    fichier.write(f"📂 Espace utilisé: {disque.used / (1024 **3):.2f} GB \n")
    fichier.write(f"📭 Espace libre: {disque.free / (1024 ** 3):.2f} GB\n")
    fichier.write(f"📊 Pourcentage utilisé: {disque.percent}%\n\n")

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    fichier.write(f"🧠 CPU utilisé: {cpu}%\n")
    fichier.write(f"📈 RAM utilisé: {ram.percent}%\n")
    fichier.write(f"📉 RAM libre: {ram.available / (1024 ** 3):.2f} GB\n")
