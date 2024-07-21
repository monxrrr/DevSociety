print("Bucles 'while'")
print()

print('''
Ejemplo para generar una cadena de texto a partir del nombre del usuario. 
Se generará un carácter por línea.''')
print()

nombre = str(input("Ingresa tu nombre de pila: "))
i = 0
while i < len(nombre):
    print(nombre[:i+1])
    i += 1