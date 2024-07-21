print(
'''Programa para que el usuario ingrese la fecha y obtenga cuantos días 
faltan para Día de Muertos y Navidad.''')
print()

from datetime import date

dmuertos = date(2024,11,1)
navidad = date(2024,12,25)

año = int(input("Ingresa el año: "))
mes = int(input("Ingresa el mes: "))
dia = int(input("Ingresa el día: "))

fecha = date(año, mes, dia)
dias_dmuertos = abs(dmuertos - fecha)
dias_navidad = abs(navidad - fecha)

print(f"Días para el Día de Muertos: {dias_dmuertos}")
print(f"Días para Navidad: {dias_navidad}")