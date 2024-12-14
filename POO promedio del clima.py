class Dia:
  def __init__(self, temperatura):
    self.temperatura = temperatura

  def obtener_temperatura(self):
    return self.temperatura

class Semana:
  def __init__(self):
    self.dias = []

  def agregar_dia(self, dia):
    self.dias.append(dia)

  def calcular_promedio(self):
    temperaturas = [dia.obtener_temperatura() for dia in self.dias]
    return sum(temperaturas) / len(temperaturas)

# Bloque principal del programa
semana = Semana()
for _ in range(7):
  temperatura = float(input("Ingrese la temperatura del día: "))
  dia = Dia(temperatura)
  semana.agregar_dia(dia)

promedio = semana.calcular_promedio()
print("El promedio semanal de temperatura es:", promedio)