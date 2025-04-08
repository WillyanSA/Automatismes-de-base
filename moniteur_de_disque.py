"Moniteur de disque"
# Surveille l'espace utilisé sur le disque (par exemple, C:\N-, D:\N-, etc.).
# Monitors the space used on the disc (e.g. C:\, D:\, etc).
# Affiche l'espace occupé et l'espace libre.
# Displays how much is occupied and how much is free.
# S'il dépasse une limite (par exemple 90 %), il envoie une alerte.
# If it exceeds a limit (e.g. 90%), it sends an alert

import psutil # Est utilisé pour surveiller les ressources du système : CPU, mémoire, disque, processus, etc.
import ctypes # Pour affichier les messages d'alert dans Windows

def info_disque():
    partition = psutil.disk_usage('C:\\')
    total = partition.total / (1024 ** 3) # GB
    used = partition.used / (1024 ** 3) # GB
    free = partition.free / (1024 ** 3) # GB
    percent = partition.percent

    print(f"💽 Total: {total:.2f} GB")
    print(f"📂 Utilisé: {used:.2f} GB")
    print(f"📭 Libre: {free:.2f} GB")
    print(f"📊 Porcentage utilisé: {percent}%")

    # Si elle dépasse 90% un avertissement s'affiche à l'écran / If the rate exceeds 90%, an alert is issued.
    if percent >= 90:
        ctypes.windll.user32.MessageBoxW(
          0,
          f"Alert. Le disque C:\\ est utilisé à {percent:.0f}% !",
          "Alerte Disque",
          0x30 # Icône d'Avis / Notification icon
        )

if __name__ == '__main__':
    info_disque()