# Escreva um programa que obtenha o menor número de uma lista.

def NumMin (lista):  
    min = lista[0]

    for a in lista:  
        if a < min:  
            min = a
    
    return min  

print(NumMin([7,8,101,34,90]))
