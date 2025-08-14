import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde el archivo Excel proporcionado
file_path = "Tarea 1 Punto 1 Regression.xlsx"
df = pd.read_excel(file_path)

# Asegurar que no haya espacios en los nombres de las columnas
df.columns = df.columns.str.strip()

# Asignar las columnas correctas
X = df['Inputs']
Y = df['Outputs']

# Normalizar los datos
X_norm = (X - X.mean()) / X.std()
Y_norm = (Y - Y.mean()) / Y.std()

# Definir función para calcular el MSE
def MSE(y_target, y_pred):
    mse = np.mean((y_target - y_pred) ** 2)
    return mse

# Regresión Lineal en datos normalizados
X_mean = np.mean(X_norm)
Y_mean = np.mean(Y_norm)

num_beta_1 = np.sum((X_norm - X_mean) * (Y_norm - Y_mean))
den_beta_1 = np.sum((X_norm - X_mean) ** 2)
beta_1 = num_beta_1 / den_beta_1

beta_0 = Y_mean - (beta_1 * X_mean)

Y_pred_linear = beta_1 * X_norm + beta_0
error_linear = MSE(Y_norm, Y_pred_linear)

# Regresión Polinomial de grado 2 en datos normalizados
n = 2
X_poly = np.ones((len(X_norm), n+1))

for i in range(1, n+1):
    X_poly[:, i] = X_norm ** i

Beta_poly = np.linalg.inv(X_poly.T @ X_poly) @ X_poly.T @ Y_norm
Y_pred_poly = X_poly @ Beta_poly
error_poly = MSE(Y_norm, Y_pred_poly)

# Mostrar los errores de ambas regresiones
print(f"Error de Regresión Lineal: {error_linear:.4f}")
print(f"Error de Regresión Polinomial (Grado 2): {error_poly:.4f}")

# Comparar y mostrar cuál método tiene menor error
if error_linear < error_poly:
    print("La Regresión Lineal tiene un error menor.")
else:
    print("La Regresión Polinomial tiene un error menor.")

# Graficar resultados
plt.figure(figsize=(14, 6))

# Gráfico de regresión lineal
plt.subplot(1, 2, 1)
plt.plot(X_norm, Y_norm, 'ro', label='Datos Originales')
plt.plot(X_norm, Y_pred_linear, 'b-', label='Regresión Lineal')
plt.title(f'Regresión Lineal Normalizada (MSE: {error_linear:.4f})')
plt.xlabel('Inputs Normalizados')
plt.ylabel('Outputs Normalizados')
plt.legend()
plt.grid()

# Gráfico de regresión polinomial
plt.subplot(1, 2, 2)
plt.plot(X_norm, Y_norm, 'ro', label='Datos Originales')
plt.plot(X_norm, Y_pred_poly, '*g', label='Regresión Polinomial (Grado 2)')
plt.title(f'Regresión Polinomial Normalizada (MSE: {error_poly:.4f})')
plt.xlabel('Inputs Normalizados')
plt.ylabel('Outputs Normalizados')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
