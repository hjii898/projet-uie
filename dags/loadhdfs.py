
import subprocess
import os

def main():
    source = "/tmp/donnees_collectees.txt"
    destination = "/user/hadoop/donnees/"
    
    # Crée le dossier HDFS s'il n'existe pas (option -p)
    subprocess.run(f"hdfs dfs -mkdir -p {destination}", shell=True)
    
    # Copie le fichier
    cmd = f"hdfs dfs -put -f {source} {destination}"
    result = subprocess.run(cmd, shell=True)
    
    if result.returncode == 0:
        print(f"Fichier chargé dans HDFS : {destination}")
    else:
        print("Erreur lors du chargement HDFS")

if __name__ == "__main__":
    main()