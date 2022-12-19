#Atv. 2. Escrever um programa que faça o somatório dos itens de uma lista

i = 0
lista = []

while i <5:
    valores = int(input(f"Digite o {i+1}º valor: "))
    i += 1
    lista.append(valores)
    

soma_dos_valores = sum(lista)

print("Eis a lista dos números digitados: ",lista,"e a soma dos valores digitados é: ",soma_dos_valores)