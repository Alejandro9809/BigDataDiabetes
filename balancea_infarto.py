import pandas as pd


df_original = pd.read_csv('DataSet90restante.csv')

df_muestra = pd.read_csv('muestra10.csv')

condicion1 = (df_original['HeartDiseaseorAttack'] == 1)

df_condicion = df_original[condicion1].sample(frac=.95).reset_index(drop=True)

df_balanceado = pd.concat([df_muestra, df_condicion], ignore_index=True)

df_balanceado.to_csv('muestraBalanceadaInfarto.csv', index=False)