f=open("day4-2","r").read().split("\n")

help=open("help","r").read().split("\n")
stev=open("day4-1","r").read().split(",")

stevilke=set()

for x in help:
    x=x.split()
    for y in x:
        stevilke.add(y)

for stevilo in stev:
    if stevilo in stevilke:
        stevilke.remove(stevilo)


print(stevilke)
print(sum((int(x) for x in list(stevilke))))