#practica 5
#realize un programa para saber si es 
#mayor de edad o menor de edad

nombre =input("nombre de la persona: ") 
edad =int(input("ingrese la edad :"))

if edad >= 18:
    print(f"eres mayor de edad {nombre}")
else:
    print(f"es menor de edad {nombre}")
