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
        mreza[stevec_desno, stevec_dol]= int(item)
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

neki = dict.fromkeys(najmanjsi, 0)

krtk = set()
for prva,druga in mreza.items():
    if druga==9:
        krtk.add(prva)

for rktk in krtk:
    del mreza[rktk]
print(mreza)

def najdi_sosede(x):
    x_koord,y_koord= x
    sosedi= set()
    if (x_koord + 1,y_koord) in mreza:
        sosedi.add((x_koord + 1,y_koord))
    if (x_koord - 1, y_koord) in mreza:
        sosedi.add((x_koord - 1, y_koord))
    if (x_koord, y_koord + 1) in mreza:
        sosedi.add((x_koord, y_koord + 1))
    if (x_koord, y_koord - 1) in mreza:
        sosedi.add((x_koord, y_koord - 1))
    return sosedi

stevec = 0
for x in neki:
    stevec+=1
    print(stevec)
    neki[x] = najdi_sosede(x)
    uporabljene = set()
    uporabljene.add(x)
    nove=set()
    dolz_star=0
    dolz_nove=len(neki[x])
    while dolz_nove!=dolz_star:
        dolz_star = len(neki[x])
        for tocka in neki[x]:
            nove.update(najdi_sosede(tocka))
            uporabljene.add(tocka)
        neki[x].update(nove)
        dolz_nove = len(neki[x])
print(neki)

asd=[]
for x,y in neki.items():
    asd.append(len(y))
print(sorted(asd))