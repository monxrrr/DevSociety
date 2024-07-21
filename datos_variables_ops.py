# Seleccioné el lenguaje de programación Python: https://www.python.org

# COMENTARIOS

# Esto es un comentario. Todo lo que está después del símbolo de número o hash se ve como una sola línea.
# Para separar un comentario largo, 
# se agrega un hash en cada línea.
# También se puede agregar un backslash para \
# indicar que un comentario largo \
# continúa en la siguiente línea.

''' Para comentarios sobre varias líneas de código o para bloques de texto
se pueden utilizar tres comillas dobles o simples '''

""" 
Sin embargo, estos comentarios multi-línea sirven para
describir o documentar una función o clase.
Se conocen como docstring y pueden ser referenciados
utilizando __doc__ 
"""

var_int = 16
var_float = 5.3
var_comp = 3j
var_bool = True
var_str = "Tipo cadena: Esto es texto ヽ(・∀・)ﾉ"
var_list = ['fresa', 'mango', 'sandía']
var_tupla = (10, 20, 30)
var_set = {1,2,3,4,5,6}
var_dicc = {'nombres':["Monse", "Juan", "Carlos", "Mariana"], 'edades':[38,25,18,22]}
var_null = None

print("VARIABLES:")
print("Tipo numérico: ", var_int, var_float, var_comp)
print("Tipo booleano: ", var_bool)
print(var_str)
print("Tipo lista: ", var_list)
print("Tipo tupla: ", var_tupla)
print("Tipo conjunto: ", var_set)
print("Tipo diccionario: ", var_dicc)
print("Tipo None: ", var_null) #representa la ausencia de un valor
print("--------------------------------------------")
print("¡Hola, Python!")
print("--------------------------------------------")

x = 5; y = 3
print("OPERADORES ARITMÉTICOS")
print("Donde x=5 y y=3")
print("Suma: x+y = ", x+y)
print("Resta: x-y = ", x-y)
print("Multiplicación: x*y = ", x*y)
print("División(float): x/y = ", x/y)
print("División(floor): x//y = ", x//y) #El resultado redondeado al número entero más pequeño 
print("Módulo: x%y = ", x%y)
print("Potencia: x**y = ", x**y)
print("Orden de las operaciones (PEMDAS): ((x*x)/y)+(x**y-y) = ", ((x*x)/y)+(x**y-y))
print()
print("--------------------------------------------")

a = 10; b = 2
print("OPERADORES DE COMPARACIÓN")
print("Donde a=10 y b=2")
print("Mayor que: a>b = ", a>b)
print("Menor que: a<b = ", a<b)
print("Igual a: a==b = ", a==b)
print("No es igual a: a!=b = ", a!=b)
print("Mayor o igual que: a>=b = ", a>=b)
print("Menor o igual  que: a<=b = ", a<=b)
print()
print("--------------------------------------------")

c = True; d = False
print("OPERADORES LÓGICOS")
print("Donde c=True y d=False")
print("c AND d = ", c and d) #Verdadero si ambas variables  son verdaderas
print("c OR d = ", c or d) #Verdadero si cualquiera de las variables  es verdadera
print("NOT d = ", not d) #Verdadero si la variable es falsa
print()
print("--------------------------------------------")

a = 14; b = 5
print("OPERADORES BITWISE") #Para operaciones lógicas a nivel de bits (comparar binarios)
print("Donde a=14 y b=5") #en binario 14 = 1110; 15 = 111
print("AND: a & b = ", a & b) #si los bits comparados en la misma posición tienen como valor 1, el valor resultante es 1; de lo contrario es 0
print("OR: a | b = ", a | b) #si los bits comparados en la misma posición tienen como valor 0, el valor resultante es 0; de lo contrario es 1
print("NOT: ~a = ", ~a) #-a -1
print("XOR: a ^ b = ", a ^ b) #si los bits comparados en la misma posición tienen el mismo valor el resultante es 0; de lo contrario es 1
print("RIGHT SHIFT: a >> 2 = ", a >> 2)
print("LEFT SHIFT: a << 2 = ", a << 2)
print()
print("--------------------------------------------")

numero = 10
print("OPERADORES DE ASIGNACIÓN")
print("Donde numero=10")
numero += 4
print("Sumar AND: numero += 4 = ", numero)
numero -= 2
print("Restar AND: numero -= 2 = ", numero)
numero *= 3
print("Multiplicar AND: numero *= 3 = ", numero)
numero /= 2
print("Dividir AND: numero /= 2 = ", numero)
numero **= 4
print("Potencia AND: numero **= 4 = ", numero)
numero %= 10
print("Módulo AND: numero %= 10 = ", numero) # Módulo muestra el residuo de una divisón 
print()
print("--------------------------------------------")

lista_1 = [1,1,2]; lista_2 = [1,1,2]
print("OPERADORES DE IDENTIDAD")
print("Donde lista_1 = [1,1,2]; lista_2 = [1,1,2]")
print("Aunque los valores de las listas son iguales, cada lista se guarda con un identificador distinto.")
print("El identificador de la lista_1 es " ,id(lista_1))
print("El identificador de la lista_1 es ", id(lista_2))
print("lista_1 IS lista_2 = ", lista_1 is lista_2)
print("lista_1 IS NOT lista_2 = ", lista_1 is not lista_2)
print()
print("--------------------------------------------")

lista_3 = ["sandía", "mango", "tamarindo"]
print("OPERADORES DE MEMBRESÍA")
print("Donde lista_3 = ['sandía', 'mango', 'tamarindo']")
print("'man' IN lista_3 =", "ma" in lista_3)
print("'mango' IN lista_3 =", "mango" in lista_3)
print("'sandía' NOT IN lista_3 =", "sandía" not in lista_3)
