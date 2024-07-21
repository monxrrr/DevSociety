print("Programa para saber si un año es bisiesto.")
print()

año = int(input("Ingresa un año: "))
if (año % 400 == 0) and (año % 100 == 0):
    print("{0} es un año bisiesto".format(año))
elif (año % 4 == 0) and (año % 100 != 0):
    print("{0} es un año bisiesto".format(año))
else:
    print("{0} no es un año bisiesto".format(año))