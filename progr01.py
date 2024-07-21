print(
'''Programa para imprimir por consola todos los números comprendidos entre 
10 y 100 (incluidos), pares, y que no son ni el 66 ni múltiplos de 3.''')
print()

inicio = 10 ; final = 100
for i in range(inicio,final+1):
    if i % 2 == 0 and i != 66 and i % 3 != 0:
        print(i, end=", ")