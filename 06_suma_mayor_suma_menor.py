#practica 6
#Realize un programa para sumar dos numeros
#si el resultado supera los 50 mandar un sms
#"Suma mayor", sino "suma menor".

#definir variables y entrada
numero1 =int(input("ingrese el primer numero: "))
numero2 =int(input("ingrese el segundo numero: "))
# proceso
resultado=numero1+numero2

#salida
print(f"la suma de dos numeros es: {resultado}")


#condicional doble

if resultado >= 50:
    print(f"suma mayor {resultado}")
else:
    print(f"suma menor {resultado}")
