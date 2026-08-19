import os
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# ESTRUCTURAS DE DATOS INICIALES
# ==========================================
# Tuplas: Catálogo inmutable de productos ((ID, Nombre), ...)
catalogo = (
    ("P01", "Laptop"),
    ("P02", "Mouse"),
    ("P03", "Teclado"),
    ("P04", "Monitor"),
    ("P05", "Audifonos")
)

# Diccionarios: Precios unitarios y stock disponible
precios = {
    "P01": 800.0,
    "P02": 25.0,
    "P03": 45.0,
    "P04": 200.0,
    "P05": 50.0
}

stock = {
    "P01": 15,
    "P02": 60,
    "P03": 40,
    "P04": 20,
    "P05": 50
}

# Listas/Arreglos: Buffer para almacenar las ventas registradas
ventas_buffer = []

# ==========================================
# FUNCIONES MODULARES Y CONTROL DE ERRORES
# ==========================================

def guardar_ventas_csv():
    """Guarda el buffer de ventas en ventas.csv usando Pandas."""
    try:
        df = pd.DataFrame(ventas_buffer)
        df.to_csv("ventas.csv", index=False)
    except Exception as e:
        print(f"Error al guardar los datos en CSV: {e}")

def cargar_ventas_csv():
    """Carga los datos desde ventas.csv si existe (Control de Archivos y Excepciones)."""
    global ventas_buffer
    try:
        if os.path.exists("ventas.csv"):
            df = pd.read_csv("ventas.csv")
            ventas_buffer = df.to_dict(orient="records")
            print(f"Se cargaron {len(ventas_buffer)} registros desde 'ventas.csv'.")
        else:
            print("El archivo 'ventas.csv' no existe todavía. Se creará uno nuevo al registrar ventas.")
    except FileNotFoundError:
        print("Archivo ventas.csv no encontrado.")
    except Exception as e:
        print(f"Error inesperado al leer el archivo CSV: {e}")
    else:
        print("Lectura de archivos completada exitosamente.")
    finally:
        print("Inicialización de almacenamiento finalizada.\n")

def ver_catalogo():
    """Muestra el catálogo actual de productos, precios y stock."""
    print("\n--- CATÁLOGO DE PRODUCTOS ---")
    for prod in catalogo:
        pid, nombre = prod
        p = precios.get(pid, 0.0)
        s = stock.get(pid, 0)
        print(f"ID: {pid} | Producto: {nombre:<10} | Precio: ${p:>6.2f} | Stock: {s}")

def registrar_venta():
    """Registra una venta con validaciones, descuento (Reto C) y registro de errores en log.txt (Reto D)."""
    global ventas_buffer, stock
    print("\n--- REGISTRAR NUEVA VENTA ---")
    id_prod = input("Ingrese el ID del producto (ej. P01): ").strip().upper()
    
    # Validar existencia en el catálogo (Tupla)
    ids_validos = [prod[0] for prod in catalogo]
    if id_prod not in ids_validos:
        mensaje_error = f"[{datetime.datetime.now()}] Error: Intento fallido de vender ID inexistente: {id_prod}\n"
        print("¡Error! El producto no existe en el catálogo.")
        # Reto D: Escribir intento fallido en log.txt
        try:
            with open("log.txt", "a") as f_log:
                f_log.write(mensaje_error)
            print("Se ha registrado el incidente en 'log.txt'.")
        except Exception as e:
            print(f"Error escribiendo en log.txt: {e}")
        return

    # Control de errores para entradas inválidas (try/except)
    try:
        cantidad = int(input("Ingrese la cantidad a vender: "))
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
    except ValueError as ve:
        print(f"Entrada inválida para la cantidad: {ve}")
        return
    
    # Validar stock suficiente
    if stock[id_prod] < cantidad:
        print(f"Stock insuficiente. Stock actual disponible: {stock[id_prod]}")
        return
    
    precio_unitario = precios[id_prod]
    subtotal = precio_unitario * cantidad
    
    # Reto C: Aplicar descuento del 5% si unidades >= 10
    descuento = 0.0
    if cantidad >= 10:
        descuento = subtotal * 0.05
        print("¡Descuento aplicado del 5% por comprar 10 o más unidades!")
    
    total = subtotal - descuento
    
    # Actualizar stock en el diccionario
    stock[id_prod] -= cantidad
    
    # Agregar registro a la lista (buffer)
    venta_registro = {
        "Fecha": datetime.date.today().strftime("%Y-%m-%d"),
        "ID_Producto": id_prod,
        "Cantidad": cantidad,
        "Precio_Unitario": precio_unitario,
        "Total": total
    }
    ventas_buffer.append(venta_registro)
    
    # Guardar cambios en CSV
    guardar_ventas_csv()
    print(f"Venta registrada con éxito. Total a pagar: ${total:.2f}")

def calcular_metricas_numpy():
    """Calcula métricas estadísticas usando NumPy y controla división por cero."""
    print("\n--- MÉTRICAS CON NUMPY ---")
    if not ventas_buffer:
        print("No hay ventas registradas para calcular métricas.")
        return
    
    try:
        totales = np.array([v["Total"] for v in ventas_buffer])
        cantidades = np.array([v["Cantidad"] for v in ventas_buffer])
        
        media_total = np.mean(totales)
        std_total = np.std(totales)
        suma_total = np.sum(totales)
        
        print(f"Suma total de ingresos: ${suma_total:.2f}")
        print(f"Media de ingresos por venta: ${media_total:.2f}")
        print(f"Desviación estándar de ingresos: ${std_total:.2f}")
        
        # Simulación controlada de división por cero
        total_unidades = np.sum(cantidades)
        if total_unidades == 0:
            raise ZeroDivisionError("No se pueden promediar ingresos entre cero unidades vendidas.")
        
        ingreso_promedio_unidad = suma_total / total_unidades
        print(f"Ingreso promedio por unidad: ${ingreso_promedio_unidad:.2f}")
        
    except ZeroDivisionError as zde:
        print(f"Error controlado (División por cero): {zde}")
    except Exception as e:
        print(f"Error al calcular las métricas: {e}")

def graficar_ingresos():
    """Genera una gráfica de barras de ingresos por producto utilizando Matplotlib y Pandas."""
    print("\n--- GRÁFICA DE INGRESOS POR PRODUCTO ---")
    if not ventas_buffer:
        print("No hay ventas registradas para graficar.")
        return
    
    try:
        df = pd.DataFrame(ventas_buffer)
        # Uso de Pandas groupby para agrupar ingresos
        ingresos_por_prod = df.groupby("ID_Producto")["Total"].sum()
        
        productos = ingresos_por_prod.index
        ingresos = ingresos_por_prod.values
        
        plt.figure(figsize=(8, 5))
        plt.bar(productos, ingresos, color='skyblue', edgecolor='black')
        plt.title("Ingresos Totales por Producto")
        plt.xlabel("ID de Producto")
        plt.ylabel("Ingresos ($)")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error al generar la gráfica: {e}")

# ==========================================
# RETOS ADICIONALES IMPLEMENTADOS
# ==========================================

def agregar_producto_catalogo():
    """Reto A: Agrega un producto nuevo al catálogo y actualiza precios/stock."""
    global catalogo, precios, stock
    print("\n--- RETO A: AGREGAR NUEVO PRODUCTO ---")
    nuevo_id = input("Ingrese el ID del nuevo producto (ej. P06): ").strip().upper()
    
    ids_existentes = [p[0] for p in catalogo]
    if nuevo_id in ids_existentes:
        print("El ID del producto ya existe en el catálogo.")
        return
        
    nombre = input("Ingrese el nombre del producto: ").strip()
    try:
        precio = float(input("Ingrese el precio unitario: "))
        cantidad_stock = int(input("Ingrese el stock inicial: "))
        if precio < 0 or cantidad_stock < 0:
            raise ValueError("El precio y el stock deben ser valores positivos.")
    except ValueError as ve:
        print(f"Entrada inválida: {ve}")
        return
        
    # Actualizar la tupla convirtiéndola temporalmente a lista
    catalogo_lista = list(catalogo)
    catalogo_lista.append((nuevo_id, nombre))
    catalogo = tuple(catalogo_lista)
    
    # Actualizar diccionarios
    precios[nuevo_id] = precio
    stock[nuevo_id] = cantidad_stock
    
    print(f"¡Producto '{nombre}' ({nuevo_id}) agregado con éxito!")

def exportar_grafico_png():
    """Reto B: Exporta el gráfico actual a un archivo PNG usando plt.savefig."""
    print("\n--- RETO B: EXPORTAR GRÁFICO A PNG ---")
    if not ventas_buffer:
        print("No hay ventas registradas para exportar.")
        return
    
    try:
        df = pd.DataFrame(ventas_buffer)
        ingresos_por_prod = df.groupby("ID_Producto")["Total"].sum()
        
        productos = ingresos_por_prod.index
        ingresos = ingresos_por_prod.values
        
        plt.figure(figsize=(8, 5))
        plt.bar(productos, ingresos, color='salmon', edgecolor='black')
        plt.title("Ingresos Totales por Producto")
        plt.xlabel("ID de Producto")
        plt.ylabel("Ingresos ($)")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        plt.savefig("ingresos.png")
        plt.close()
        print("¡Gráfico exportado exitosamente como 'ingresos.png'!")
    except Exception as e:
        print(f"Error al exportar la gráfica: {e}")

# ==========================================
# MENÚ PRINCIPAL CON BUCLE WHILE Y CONTROL
# ==========================================
def menu_principal():
    cargar_ventas_csv()
    
    while True:
        print("\n========================================")
        print("      SISTEMA DE GESTIÓN DE VENTAS")
        print("========================================")
        print("1. Registrar Venta")
        print("2. Ver Catálogo y Stock")
        print("3. Calcular Métricas (NumPy)")
        print("4. Graficar Ingresos (Matplotlib)")
        print("5. Reto A: Agregar Nuevo Producto")
        print("6. Reto B: Exportar Gráfico a PNG")
        print("7. Salir")
        
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            ver_catalogo()
        elif opcion == "3":
            calcular_metricas_numpy()
        elif opcion == "4":
            graficar_ingresos()
        elif opcion == "5":
            agregar_producto_catalogo()
        elif opcion == "6":
            exportar_grafico_png()
        elif opcion == "7":
            print("Guardando datos y saliendo del sistema...")
            guardar_ventas_csv()
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 7.")
            continue

if __name__ == "__main__":
    menu_principal()