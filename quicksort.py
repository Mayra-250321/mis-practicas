def quick_stor(lista):
    if len(lista)<=1:
        return lista

    pivote = lista[-1]
    menores=[x for x in lista[:-1]if x <=pivote]
    mayores=[x for x in lista[:-1] if x >pivote]
     
    return quick_stor(menores)+[pivote]+ quick_stor(mayores)

numeros =[12, 23, 4, 8, 9]
print(quick_stor(numeros))    