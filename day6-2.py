f=open("day6-1","r").read().split(",")

stevilo_dni={}

for i in range(0,9):
    stevilo_dni[i]=0

for x in f:
    stevilo_dni[int(x)]+=1

stevec=0
buffer=stevilo_dni.copy()
while stevec<10000000:
    for dan in stevilo_dni:
        if dan != 8:
            stevilo_dni[dan]=stevilo_dni[dan+1]
        elif dan == 8:
            stevilo_dni[8] = buffer[0]

    stevilo_dni[6] += buffer[0]
    buffer=stevilo_dni.copy()
    stevec+=1

sum=0
for x,y in stevilo_dni.items():
    sum+=y
print(sum)






