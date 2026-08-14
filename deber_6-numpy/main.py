import numpy as np

# Creamos una lista de precios básicos
precios = np.array([10, 20, 30])

# Le sumamos 2 dólares de envío a cada producto automáticamente
precios_finales = precios + 2

print("Precios originales:", precios)
print("Precios con envío:", precios_finales)