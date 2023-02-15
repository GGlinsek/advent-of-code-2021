f=open("day5-1","r").read().split("\n")

mreza={}

for x in range(1000):
    for y in range(1000):
        mreza[(x,y)]= 0

for x in f:
    prva_terka, druga_terka= x.split("->")
    x0,y0=prva_terka.split(",")
    x1,y1=druga_terka.split(",")
    x0=int(x0)
    x1=int(x1)
    y0=int(y0)
    y1=int(y1)
    if x0!=x1 and y0!=y1:

        if x0<x1 and y0<y1:
            for linija in range(abs(x1 - x0)+1):
                mreza[x0+linija,y0+linija]+=1
        elif  x1<x0 and y0<y1:
            for linija in range(abs(x1 - x0)+1):
                mreza[x0 - linija, y0 + linija] += 1
        elif  x0<x1 and y1<y0:
            for linija in range(abs(x1 - x0)+1):
                mreza[x0 + linija, y0 - linija] += 1
        elif  x1<x0 and y1<y0:
            for linija in range(abs(x1 - x0)+1):
                mreza[x0 - linija, y0 - linija] += 1
    else:
        if x0!=x1:
            if x0<x1:
                for linija in range(x0,x1+1):
                    mreza[linija,y0]+=1
            else:
                for linija in range(x1, x0 + 1):
                    mreza[linija, y0] += 1
        elif y0!=y1:
            if y0<y1:
                for linija in range(y0,y1+1):
                    mreza[x0,linija]+=1
            else:
                for linija in range(y1, y0 + 1):
                    mreza[x0, linija] += 1

print(sum(1 for _,x in mreza.items() if x>1))