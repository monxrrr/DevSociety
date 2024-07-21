print("Programa para convertir una palabra o frase a lenguaje leet.")
print()

frase = input("Ingresa una palabra o frase sin acentos ni signos de puntación: ")
print()
char_cambio = {'a':"4",'b':"ß",'c':"(",'d':"[)",'e':"ε",'f':"ƒ",'g':"(_+",'h':"/-/",'i':"!",'j':"_|",'k':"|<",'l':"£",'m':"м",'n':"(\)",'o':"()",'p':"ρ",'q':"(,)",'r':"Я",'s':"$",'t':"7",'u':"µ",'v':"\/",'w':"[/\]",'x':"}{",'y':"¥",'z':"2"}


for char in char_cambio.keys():
    frase = frase.lower().replace(char,char_cambio[char])

print(frase)
