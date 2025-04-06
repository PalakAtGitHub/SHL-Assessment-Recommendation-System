import pandas as pd

df = pd.read_csv('shl_catalog.csv')

df = df.dropna(subset=['Title'])

df = df.reset_index(drop=True)

df.to_csv('cleaned_data.csv', index=False)

df.head()
