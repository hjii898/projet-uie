def hive():
  import pandas as pd
  df = pd.read_csv("hdfs_insurance.csv)
  df = df.drop_duplicates()
  df.to_csv("resultat.csv", index=False)
  print ("Transformation Hive terminée)
