#practica5
#Realize 


#definir variables y entrada
monto = float(input("monto a enviar: "))
destinatario =  input("nombre del beneficiario: ")
ente_emisor = input("entidad bancaria: ")

#variables fijos
fecha = "12/10/2026"
hora = "16:15 p.m."
cuenta = "57023768"
nro_transaccion = "100100100"
nombre = "brandon"
apellido = "tito"

#salida, diseño del comprobante
print("")
print("       YAPE COMPROBANTE      ")
print("┌────────────────────────────────")
print(" !yapeaste¡                  ")
print(f"  Bs:{monto}")
print("                             ")
print(f"  nombre:{destinatario}")
print(f"  fecha:{fecha} hora:{hora}")
print("                             ")
print("  DATOS DE LA TRANSACCION      ")
print("                             ")
print(f"  cuenta:{cuenta}")
print(f"  destino:{ente_emisor}")
print(f"  Nro de transaccion:{nro_transaccion}")
print(f"  Realizado por:{nombre}")
print("└───────────────────────────────┘")
print("   con el respaldo de >BCP>   ")

