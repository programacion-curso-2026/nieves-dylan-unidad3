import pandas as pd

# 1. Crear un diccionario con datos
datos = {'Fruta': ['Manzana', 'Pera', 'Banano'], 'Cantidad': [10, 5, 20]}

# 2. Crear la tabla (DataFrame)
df = pd.DataFrame(datos)

# 3. Mostrar la tabla
print(df)

# --- Segundo Ejemplo ---
print("\n--- Segundo Ejemplo ---")
datos2 = {'Producto': ['Camisa', 'Pantalón'], 'Precio': [20, 50]}
df2 = pd.DataFrame(datos2)

# Sumar todos los precios
total = df2['Precio'].sum()
print(f"Total a pagar: {total}")
