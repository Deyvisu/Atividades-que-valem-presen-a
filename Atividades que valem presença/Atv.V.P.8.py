# link 1 = Q 13 - Adicionar o ing e ly nas strings

def addString(str1):
    length = len(str1)

    if length > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else: 
            str1 += 'ing'

    return str1

print(addString('ab'))
print(addString('abc'))
print(addString('string'))