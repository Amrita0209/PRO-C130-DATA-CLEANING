import pandas as pd

df = pd.read_csv("merged.csv")

#Delete the entire column under the particular header
del df["Luminosity"]
del df["Unnamed: 0"]

df.to_csv("final.csv")

