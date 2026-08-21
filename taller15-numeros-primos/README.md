import random

def es_primo(n):
    """Función para verificar si un número es primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# --- EJERCICIO A ---
print("--- EJERCICIO A: Número primo aleatorio ---")
while True:
    numero_aleatorio = random.randint(1, 100)
    if es_primo(numero_aleatorio):
        print(f"El número primo aleatorio generado es: {numero_aleatorio}")
        break

# --- EJERCICIO B ---
print("\n--- EJERCICIO B: Números primos hasta N ---")
try:
    entrada = input("Ingrese un valor entero N: ")
    N = int(entrada)
    
    if N < 2:
        print("No hay números primos menores a 2.")
    else:
        lista_primos = [i for i in range(2, N + 1) if es_primo(i)]
        print(f"Números primos hasta {N}: {lista_primos}")
except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")