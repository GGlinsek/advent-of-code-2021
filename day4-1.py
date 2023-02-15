f=open("day4-1","r").read().split(",")
karte=open("karte","r").read().split("\n\n")

karte_dict=dict.fromkeys(karte, 0)


for x,bullshit in karte_dict.items():
    y=[]
    celotna=x.split("\n")
    cela=set()
    for item in celotna:
        item=item.split()
        for thingie in item:
            cela.add(thingie)
    y.append(cela)
    d=x.split("\n")
    prvi_s=set()
    drugi_s=set()
    tretji_s=set()
    cetrti_s=set()
    peti_s=set()
    for item in d:
        nekidruga=set(item.split())
        item=item.split()
        y.append(nekidruga)
        prvi_s.add(item[0])
        drugi_s.add(item[1])
        tretji_s.add(item[2])
        cetrti_s.add(item[3])
        peti_s.add(item[4])
    y.append(prvi_s)
    y.append(drugi_s)
    y.append(tretji_s)
    y.append(cetrti_s)
    y.append(peti_s)
    karte_dict[x]=y

i=0
kul=0
pomembna=0
neki=karte_dict.copy()
while len(karte_dict)>0:
    i=0
    for x in f:
        if i==0:
            for a,b in karte_dict.items():
                for mnozica in b:
                    if x in mnozica:
                        mnozica.remove(x)
                    if len(mnozica)==0 and len(karte_dict)!=1:
                        i=1
                        del karte_dict[a]
                        print(x)
                        break
                    if len(mnozica)==0 and len(karte_dict)==1:
                        i=1
                        pomembna=int(x)
                        kul=a
                        print(sum(int(x) for x in b[0])*pomembna)
                        del karte_dict[a]
                        print(x)
                        break
                if i==1:
                    break




        else:
            break




print(len(karte_dict))
print(karte_dict)






