print("Bucles 'for'")
print()

print('''
Ejemplo para generar una numeración por incrementos. En donde el usuario 
indique en qué número inicia, en qué número termina y cómo lo va a hacer.
Por ejemplo, deberá indicar que inicia en 5, termina en 500 y que va de 5 en 5''')
print()

inicio = int(input("Ingresa el número en que inicia tu numeración: "))
final = int(input("Hasta qué número llegará: "))
como = int(input("¿Cómo será el incremento?: "))

for i in range(inicio, final+1, como):
  print(i, end=", ")