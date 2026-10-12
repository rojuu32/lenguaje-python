#practica 7
# realize un programa para saber si la persona
#puede emitir su voto en las elecciones, usando
#IF "si puede votar", ELSE "no puede votar"

nombre =input("nombre de la persona: ") 
edad =int(input("ingrese la edad :"))

if edad >= 18:
    print(f"si puede votar {nombre}")
else:
    print(f"no puede votar {nombre}")
