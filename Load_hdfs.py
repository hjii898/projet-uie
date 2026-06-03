def load_hdfs(df):
  df.to_csv("hdfs_insurance.csv", index=false)
  print("chargement hdfs terminé")
