f = open("day1-1.txt","r")
lista = []
k = 0
prejsna = 0
for x in f.readlines():
    x = x.rstrip("\n")
    nova = int(x)
    lista.append(nova)

for i in range(3, len(lista)):
    if lista[i] > lista[i-3]:
        k += 1

print(k)