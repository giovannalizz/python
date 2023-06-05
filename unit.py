def gera_primos(numero):
    primos = []
    for num in range(2, numero + 1):
        if eh_primo(num):
            primos.append(num)
    return primos

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Escreva um número: "))
primos = gera_primos(numero)
print(f"Números primos menores ou iguais a {numero}: {primos}")