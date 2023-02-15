f=open("day6-1","r").read().split(",")
x=1
buffer={}

for i in f:
    buffer[x]= int(i)
    x+=1
x-=1
stevec=0
ribe= buffer.copy()
while stevec<256:
    for riba in buffer:
        if ribe[riba] == 0:
            ribe[riba] = 7
            x+=1
            ribe[x]= 8
        ribe[riba] -= 1

    buffer=ribe.copy()
    print(stevec)
    stevec+=1

print(len(ribe))