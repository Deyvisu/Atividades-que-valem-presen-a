def maior(n1,n2,n3):
    max = n1

    if n2 > max:
        max = n2
    if n3 > max:
        max = n3

    return max

def numeros():
    num1 = int(input('Primeiro numero: '))
    num2 = int(input('Segundo numero : '))
    num3 = int(input('Terceiro numero: '))

    print("Maior: ", maior(num1, num2, num3))
    print()


while True:
    numeros()
    break