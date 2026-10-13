#practica 12
#usamos la estructura FOR para mostrar
#una tabla de multiplicar 

print("MOSTRANDO TABLA DE MULTIPLICACION")

#variables y entrada

numero = int(input("elija un numero"))

#estructura FOR
for i in range(1, 11):
    resultado = numero * i
    print(f" {numero} x {i} = {resultado}")
