
import subprocess

def main():
    source_hdfs = "/user/hadoop/donnees/donnees_collectees.txt"
    archive_dir = "/user/hadoop/archive/"
    
    # Crée le dossier archive si nécessaire
    subprocess.run(f"hdfs dfs -mkdir -p {archive_dir}", shell=True)
    
    # Déplace le fichier (mv)
    cmd = f"hdfs dfs -mv {source_hdfs} {archive_dir}"
    result = subprocess.run(cmd, shell=True)
    
    if result.returncode == 0:
        print(f"Fichier archivé dans {archive_dir}")
    else:
        print("Erreur lors de l'archivage")

if __name__ == "__main__":
    main()