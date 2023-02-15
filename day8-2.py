f=open("day8-1","r").read().split("\n")
dictionary=open("day8-2","r").read().split("\n")
output=[]

for x in f:
    items=x.split("|")
    output.append(items[1])

pozicije={}
for i in range(1,8):
    pozicije[i]=0

for x in output:
    stevilo= []
    pozicije[1] = set()
    pozicije[2] = set()
    pozicije[3] = set()
    pozicije[4] = set()
    pozicije[5] = set()
    pozicije[6] = set()
    pozicije[7] = set()
    znaki=x.split()
    for znak in znaki:
        if len(znak)==2:
            pozicije[3].update(list(znak))
            pozicije[6].update(list(znak))
        elif len(znak) == 3:
            pozicije[1].update(list(znak))
            pozicije[3].update(list(znak))
            pozicije[6].update(list(znak))
        elif len(znak) == 4:
            pozicije[2].update(list(znak))
            pozicije[3].update(list(znak))
            pozicije[4].update(list(znak))
            pozicije[6].update(list(znak))
    for znak in znaki:
        if len(znak)==2:
            stevilo.append(1)
        elif len(znak)==3:
            stevilo.append(7)
        elif len(znak)==4:
            stevilo.append(4)
        elif len(znak)==7:
            stevilo.append(8)
        elif len(znak)== 5:
            if set(znak).issubset(set.union(pozicije[1],pozicije[3],pozicije[4],pozicije[5],pozicije[7])): #2
                stevilo.append(2)
            elif set(znak).issubset(set.union(pozicije[1], pozicije[3], pozicije[4], pozicije[6], pozicije[7])): #3
                stevilo.append(3)
            elif set(znak).issubset(set.union(pozicije[1],pozicije[2],pozicije[4],pozicije[6],pozicije[7])): #5
                stevilo.append(5)



print(sum)