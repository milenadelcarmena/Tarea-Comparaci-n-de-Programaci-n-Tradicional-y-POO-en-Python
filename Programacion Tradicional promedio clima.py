def ingresar_temperaturas():
  """Ingresa las temperaturas diarias de una semana."""
  temperaturas = []
  for dia in range(1, 8):
    temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
    temperaturas.append(temperatura)
  return temperaturas

def calcular_promedio(temperaturas):
  """Calcula el promedio de una lista de temperaturas."""
  return sum(temperaturas) / len(temperaturas)

# Bloque principal del programa
temperaturas_semanales = ingresar_temperaturas()
promedio = calcular_promedio(temperaturas_semanales)
print("El promedio semanal de temperatura es:", promedio)
