# Indtrudizca dos numeros que tengan mas de 3 digitos y determine si son o no AMIGO. (validar)
# un numero es amigo del otro cuando la suma de sus digitos es igual a la suma de los digitos del otro numero
#Ejemplo: Si A = 5321 y B =271010 --> Se despliea "son amigos"
print("----Números Amigos----")
def introducir_numero1():
    while True:
        numero1 = input("Ingrese el primer número con más de 3 dígitos: ")
        if len(numero1) > 3 and numero1.isdigit():
            return numero1
        else:
            print("Número incorrecto. Por favor, ingrese un número con más de 3 dígitos.")
def introducir_numero2():
        while True:
            numero2 = input("Ingrese el segundo número con más de 3 dígitos: ")
            if len(numero2) > 3 and numero2.isdigit():
                return numero2
            else:
                print("Número incorrecto. Por favor, ingrese un número con más de 3 dígitos.")
def separar_digitos(numero1, numero2):
    digitos1 = []
    digitos2 = []
    while numero1 > 0:
        digitos1.append(numero1 % 10)
        numero1 //= 10
    while numero2 > 0:
        digitos2.append(numero2 % 10)
        numero2 //= 10
    return digitos1, digitos2
def suma_digitos(digitos1,digitos2):
    suma1 = sum(digitos1)
    suma2 = sum(digitos2)
    return suma1, suma2
def son_amigos(suma1,suma2):
    if suma1 == suma2:
        print("Son amigos")
    else:
        print("No son amigos")
def main():
    numero1 = int(introducir_numero1())
    numero2 = int(introducir_numero2())
    digitos1, digitos2 = separar_digitos(numero1, numero2)
    suma1, suma2 = suma_digitos(digitos1,digitos2)
    son_amigos(suma1,suma2)

main()