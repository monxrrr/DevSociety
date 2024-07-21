print(
'''Programa que te diga si la frase ingresada por el usuario
es o no un palíndromo.''')
print()

def es_palindromo(frase):
    frase = frase.lower().replace("","")
    primero, ultimo = 0, len(frase) -1
    
    while primero < ultimo:
        if(frase[primero] == frase[ultimo]):
            primero += 1
            ultimo -= 1
        else:
            return False
    
    return True

input_frase = input("Ingresa una frase: ")
if es_palindromo(input_frase):
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")