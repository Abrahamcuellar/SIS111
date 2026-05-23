# Obtenga la suma de numeros primos comprendidos entre 2...n
# Un numero primo es aquel numero natural mayor que 1 que solo tiene dos divisores el 1 y el mismo. Si
# intentas dividirlo por cualquier otro numero, el resultado no es un entero.
print("----Suma de Números Primos----")
def ingresar_numero():
    while True:
        numero = input("\nIngrese un número: ")
        if numero.isdigit() and int(numero) > 1:
            return int(numero)
        else:
            print("Número no válido. Por favor, ingrese un número primo.")
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2,int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True
def suma_primos(numero):
    suma = 0
    for i in range(2, numero+1):
        if es_primo(i):
            suma += i
    return suma
def main():
    numero = ingresar_numero()
    suma = suma_primos(numero)
    print(f"La suma de los números primos entre 2 y {numero} es {suma}")
main()