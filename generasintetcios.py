import pandas as pd
from imblearn.over_sampling import SMOTE

# Cargar tu conjunto de datos existente
data = pd.read_csv('muestraBalanceadaD012.csv')

# Separar características (X) y etiquetas (y)
X = data.drop('Diabetes_012', axis=1)
y = data['Diabetes_012']

smote = SMOTE(sampling_strategy={1:5563}, random_state=42)

X_synthetic, y_synthetic = smote.fit_resample(X, y)
# Crear un nuevo DataFrame con datos sintéticos
X_synthetic = X_synthetic.round()

df_synthetic = pd.DataFrame(X_synthetic, columns=X.columns)
df_synthetic['Diabetes_012'] = y_synthetic

df_synthetic.to_csv('datos_sinteticosB012.csv', index=False)
