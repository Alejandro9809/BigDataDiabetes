import pandas as pd


df_original = pd.read_csv('DataSet90restante.csv')

df_muestra = pd.read_csv('muestra10.csv')

condicion0= (df_muestra['Diabetes_012'] == 0)
condicion1 = (df_muestra['Diabetes_012'] == 1)
condicion2 = (df_muestra['Diabetes_012'] == 2)

#condiciones = condicion1 | condicion2

df_condicion0 = df_muestra[condicion0].sample(frac=.37).reset_index(drop=True)
df_condicion1= df_muestra[condicion1].sample(frac=1).reset_index(drop=True)
df_condicion2 = df_muestra[condicion2].sample(frac=1).reset_index(drop=True)

df_condicion = pd.concat([df_condicion0, df_condicion2], ignore_index=True)

#df_balanceado = pd.concat([df_muestra, df_condicion], ignore_index=True)

df_balanceado=pd.concat([df_condicion,df_condicion1])

df_balanceado.to_csv('muestra2BalanceadaD012.csv', index=False)