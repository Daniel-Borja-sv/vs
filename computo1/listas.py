#indices   0          1            2
lista = ["lapiz", "Borrador", "Sacapuntas"]
#           -3         -2         -1

lista2 = [12,1,5,89,0]
lista3 = ["Maria", 12, True]

print (lista.index("lapiz"))
#lista.index("lapicero")

lista2.append(7)
print(lista2)
lista2.insert(2,10)
print(lista2)


indice = 0 

for i in lista:
    print(lista[indice])
    indice+=1

lista[1]="corrector"
print (lista)
