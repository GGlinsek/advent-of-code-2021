f=open("day9-1","r").read().split("\n")

mreza={}


for x in range (100):
    for y in range(100):
        mreza[x,y]=0

stevec_dol=0
for x in f:
    stevec_desno=0
    x=list(x)
    for item in x:
        mreza[stevec_desno, stevec_dol]= item
        stevec_desno+=1
    stevec_dol+=1

def minimum_x(x,y):
    najmanjsi= set()
    if x[0]<x[1]:
        najmanjsi.add((0,y))
    for i in range(1, len(x)):
        if 99!=i:
            if x[i-1]>x[i] and x[i+1]>x[i]:
                najmanjsi.add((i, y))
        if i==99:
            if x[i-1]>x[i]:
                najmanjsi.add((i, y))
    return najmanjsi

def minimum_y(mreza,x):
    najmanjsi = set()
    if mreza[(x,0)] < mreza[(x,1)]:
        najmanjsi.add((x, 0))
    for i in range(1, 100):
        if 99 != i:
            if mreza[(x,i-1)]>mreza[(x,i)] and mreza[(x,i+1)]>mreza[(x,i)]:
                najmanjsi.add((x, i))
        if i==99:
            if mreza[(x, i - 1)] > mreza[(x, i)]:
                najmanjsi.add((x, i))
    return  najmanjsi

najmanjsi_v_vrsto=set()
najmanjsi_v_stolp=set()
stevec_y=0
for x in f:
    x=list(x)
    najmanjsi_v_vrsto.update(minimum_x(x,stevec_y))
    najmanjsi_v_stolp.update(minimum_y(mreza,stevec_y))
    stevec_y+=1


najmanjsi=set()

for x in najmanjsi_v_vrsto:
    if x in najmanjsi_v_stolp:
        najmanjsi.add(x)

vsota=0
for x in najmanjsi:
    vsota+= 1+int(mreza[x])
print(vsota)
print(najmanjsi)
