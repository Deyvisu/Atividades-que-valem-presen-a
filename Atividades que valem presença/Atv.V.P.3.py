#Escrever um programa que multiplique todos os itens da lista
#obs: utilizei a importação da função de multiplicação importado de math
from math import prod

i = 0
lista = []

while i <5:
    lista.append(int(input(f"Insira o {i+1}º número inteiro: ")))
    i+=1

print("Eis a lista dos números: ",lista, f"e o produto dos números da lista é: {prod(lista)}")