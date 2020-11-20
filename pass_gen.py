import random

def pass_gen():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H', 
            'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Z']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    simbolos = ['!', '#', '$', '&', '(', '%', ')', '=', '?', '¿', 'º', '@']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayus + minus + simbolos + numeros

    password = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = ''.join(password)
    return password



def run():
    password = pass_gen()
    print('Tu nueva contraseña es: ' + password)


if __name__ == "__main__":
    run()