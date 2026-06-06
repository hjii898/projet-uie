
import subprocess

def main():
    # Requête Hive : crée une table externe pointant vers les données archivées
    query = """
    CREATE EXTERNAL TABLE IF NOT EXISTS ma_table (
        ligne STRING
    )
    ROW FORMAT DELIMITED FIELDS TERMINATED BY '\\n'
    LOCATION '/user/hadoop/archive/';
    """
    
    # Exécute via beeline ou hive (selon votre environnement)
    # On utilise hive -e pour simplifier
    cmd = f'hive -e "{query}"'
    result = subprocess.run(cmd, shell=True)
    
    if result.returncode == 0:
        print("Table Hive créée avec succès")
    else:
        print("Erreur Hive, vérifiez que hive command est disponible")

if __name__ == "__main__":
    main()