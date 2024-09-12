import pandas as pd

df = pd.read_csv("latvijas_dzimstības_dati.csv",delimiter=";")

gadi_summārā_dzimstība = df[["Laika periods","Summārais dzimstības koeficients"]]

print(gadi_summārā_dzimstība.sort_values("Summārais dzimstības koeficients",ascending=False))




