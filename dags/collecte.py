
import datetime

def main():
    # Crée un fichier avec la date et heure actuelles
    fichier = "/tmp/donnees_collectees.txt"
    with open(fichier, "w") as f:
        f.write(f"Données collectées le {datetime.datetime.now()}\n")
    print(f"Collecte terminée : {fichier} créé")

if __name__ == "__main__":
    main()