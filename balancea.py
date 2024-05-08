import pandas as pd


df_original = pd.read_csv('DataSet90restante.csv')

df_muestra = pd.read_csv('muestra2BalanceadaD012.csv')

condicion1 = (df_original['Diabetes_012'] == 1)
#condicion2 = (df_original['Diabetes_012'] == 2)

#condiciones = condicion1 | condicion2

df_condicion1 = df_original[condicion1].sample(frac=0.7).reset_index(drop=True)

#df_condicion2 = df_original[condicion2].sample(frac=.55).reset_index(drop=True)

#df_condicion = pd.concat([df_condicion1, df_condicion2], ignore_index=True)

df_balanceado = pd.concat([df_muestra, df_condicion1], ignore_index=True)

df_balanceado.to_csv('muestraBalanceadaFINALD012.csv', index=False)