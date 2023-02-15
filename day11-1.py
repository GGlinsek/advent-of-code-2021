f=open("day11","r").read().split("\n")


mreza={}
for x in range(10):
    for y in range(10):
        mreza[x,y]=0



for x in f:
    x=x.split()
    for item in x:
        stevec_dol = 0
        for x in f:
            stevec_desno = 0
            for item in x:
                mreza[stevec_desno, stevec_dol] = int(item)
                stevec_desno += 1
            stevec_dol += 1


for hobotnica in mreza:
    mreza[hobotnica] +=1

for hobotnica in mreza:
    x_koord,y_koord = hobotnica
    devetke=set
    if mreza[hobotnica] == 9:
        devetke.add(mreza[hobotnica])


        mreza[x_koord+1,y_koord] +=1
        mreza[x_koord-1,y_koord] +=1
        mreza[x_koord,y_koord+1] +=1
        mreza[x_koord,y_koord-1] +=1
        mreza[x_koord+1,y_koord+1] +=1
        mreza[x_koord-1,y_koord-1] +=1
        mreza[x_koord+1,y_koord-1] +=1
        mreza[x_koord-1,y_koord+1] +=1
        mreza[hobotnica] = 0


