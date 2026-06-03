import pandas as pd
def collecte():
  df=pd.read_csv("insurance.csv")
  print (df.head())
  return df
