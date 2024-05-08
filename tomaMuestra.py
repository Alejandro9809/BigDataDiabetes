import pandas as pd

# Lee el archivo CSV original
df_original = pd.read_csv('DataSet90restanteBinary.csv')

# Selecciona registros aleatorios sin repetición
df_muestra = df_original.sample(frac=.5).reset_index(drop=True)

df_original = df_original.drop(df_muestra.index)

# Guarda la muestra en un nuevo archivo CSV
df_muestra.to_csv('muestra10binaryPrueba.csv', index=False)

df_original.to_csv('DataSet90restanteBinaryPrueba.csv', index=False)
