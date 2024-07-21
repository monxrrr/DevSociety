print("CONDICIONALES 'if', 'elif' y 'else'")
print()

edad = int(input("Ingresa tu edad: "))

if edad <= 19:
  print("¡Estás súper joven!")
elif edad >= 20 and edad <=29: 
  print("¡Aprovecha tus 20s!")
elif edad >= 29 and edad <=39:
  print("¡Ya estás en el 3er piso!")
elif edad >= 40 and edad <=64:
  print("¿Ya ahorraste para tu retiro?")
else:
  print("¡Tiempo de disfrutar!")