# main.py

import sys
import os

src_dir = os.path.join(os.path.dirname(__file__), 'src')

sys.path.insert(0, src_dir) 


try:
    from interface import main_interface
except ImportError as e:
    print(f"ERREUR FATALE : Impossible d'importer l'interface. Vérifiez la structure du dossier 'src'.")
    print(f"Détails : {e}")
    sys.exit(1)


def main():
    """
    Fonction principale pour démarrer l'application.
    """
    print("Démarrage de l'application de calcul du second degré...")
    main_interface()
    print("Application terminée.")


if __name__ == "__main__":
    main()