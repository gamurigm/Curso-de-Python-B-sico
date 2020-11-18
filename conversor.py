pesos = float(input("Pesos: "))
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)

print("Tienes $" + dolares + "dólares")