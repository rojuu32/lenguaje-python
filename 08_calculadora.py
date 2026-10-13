#practica 8

#realize


import os
os.system("cls")

#menu de opciones

print("-----CALCULADORA-----")
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")

#entrada

opcion_calculadora = int(input("elija una opcion"))
numero1 = int(input("primer numero :"))
numero2 = int(input("segundo numero :"))

#proceso
match opcion_calculadora:
    case 1:
        print("operacion suma")
        resultado=numero1+numero2
        print(f"la suma es: {resultado}")
    case 2:
        print("operacion resta")
        resultado=numero1-numero2
        print(f"la resta es: {resultado}")
    case 3:
        print("operacion multiplicar")
        resultado=numero1*numero2
        print(f"la multiplicacion es: {resultado}")
    case 4:
        print("operacion division")
        if numero2 != 0:
            resultado =numero1/numero2
            print(f"la division es: {resultado}")
        else:
            print("error: no se puede dividir entre cero")
    case _:
        print ("error, seleccione nuevamente")
print ("gracias por usar mi calculadora")
