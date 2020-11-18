# pesos = float(input("Pesos: "))
# valor_dolar = 3875
# dolares = pesos / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print("Tienes $" + dolares + "dólares")

def conversor(pesos, tipo_cambio):
    pesos = float(input("Pesos " + pesos + ":"))
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


menu = """
Bienvenido al conversor de monedas 

Opción 1. - Pesos Colombianos
Opción 2. - Pesos Argentinos
Opción 3. - Pesos Uruguayos

Elije una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
    
elif opcion ==2:  
    conversor("argentinos", 195)

elif opcion == 3:
    conversor("uruguayos", 24)

else:
    print("Ingrese una opción correcta!")