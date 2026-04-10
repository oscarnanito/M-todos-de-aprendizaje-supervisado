import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, r2_score

# Cargar dataset
df = pd.read_csv("dataset_transporte.csv")

# Convertir texto a números
le_origen = LabelEncoder()
le_destino = LabelEncoder()

df["origen"] = le_origen.fit_transform(df["origen"])
df["destino"] = le_destino.fit_transform(df["destino"])

# Variables de entrada (X)
X = df[[
    "origen",
    "destino",
    "distancia_m",
    "hora_pico",
    "trafico",
    "lluvia",
    "pasajeros"
]]

# Variable de salida (y)
y = df["tiempo_viaje_min"]

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Crear modelo
modelo = LinearRegression()

# Entrenar modelo
modelo.fit(X_train, y_train)

# Hacer predicciones
y_pred = modelo.predict(X_test)

# Evaluar modelo
error = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("===== RESULTADOS =====")
print("Error (Promedio):", round(error, 2))
print("R2 (Varianza):", round(r2, 2))
