# Fonctions utilitaires, par exemple, pour un nettoyage de texte
def clean_text(text):
    return text.strip().lower()

# Exemple de fonction pour vérifier si un fichier existe
import os
def file_exists(filepath):
    return os.path.isfile(filepath)
