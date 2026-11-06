
import random
import time
from datetime import datetime

# ==========================================
# PROGRAMA: ORDENAMIENTO DE 10,000 NUMEROS
# METODO: BURBUJA
# ==========================================

# 1. Generar 10,000 numeros aleatorios
cantidad = 10000

numeros = []

for i in range(cantidad):
    ai = int(random.random() * 10000)
    numeros.append(ai)

# Guardar una copia de los numeros originales
numeros_originales = numeros.copy()

print("====================================")
print("     ORDENAMIENTO POR BURBUJA")
print("====================================")

print("\nNUMEROS ALEATORIOS GENERADOS:")
print(numeros_originales)

# 2. Inicializar contadores
comparaciones = 0
intercambios = 0

# 3. Registrar tiempo de inicio
hora_inicio = datetime.now()
tiempo_inicio = time.perf_counter()

# 4. METODO DE LA BURBUJA
for i in range(cantidad - 1):

    for j in range(cantidad - 1 - i):

        comparaciones += 1

        if numeros[j] > numeros[j + 1]:

            # Intercambiar numeros
            auxiliar = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = auxiliar

            intercambios += 1

# 5. Registrar tiempo de finalizacion
tiempo_fin = time.perf_counter()
hora_fin = datetime.now()

tiempo_total = tiempo_fin - tiempo_inicio

# 6. Calcular media
media = sum(numeros) / cantidad

# 7. Calcular mediana
if cantidad % 2 == 0:
    mediana = (
        numeros[cantidad // 2 - 1] +
        numeros[cantidad // 2]
    ) / 2
else:
    mediana = numeros[cantidad // 2]

# 8. Mostrar resultados
print("\n====================================")
print("       NUMEROS ORDENADOS")
print("====================================")

print(numeros)

print("\n====================================")
print("          ESTADISTICAS")
print("====================================")

print("Cantidad de datos:", cantidad)
print("Comparaciones realizadas:", comparaciones)
print("Intercambios realizados:", intercambios)

print("Media aritmetica:", media)
print("Mediana:", mediana)

print("\n====================================")
print("       MEDICION DEL TIEMPO")
print("====================================")

print("Hora de inicio:", hora_inicio)
print("Hora de finalizacion:", hora_fin)

print("Tiempo total de ordenamiento:",
      tiempo_total, "segundos")

print("\n====================================")
print("       PROCESO TERMINADO")
print("====================================")

# 9. Guardar los resultados en archivos TXT

with open("numeros_originales.txt", "w") as archivo:
    archivo.write(str(numeros_originales))

with open("numeros_ordenados.txt", "w") as archivo:
    archivo.write(str(numeros))

print("\nSe guardaron los archivos:")
print("numeros_originales.txt")
print("numeros_ordenados.txt")
