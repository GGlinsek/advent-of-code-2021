f=open("day8-1","r").read().split("\n")
output=[]

for x in f:
    items=x.split("|")
    output.append(items[1])

dolzine = [2,3,4,7]
stevec=0

for x in output:
    stevilke=x.split()
    for stevilka in stevilke:
        if len(stevilka) in dolzine:
            stevec+=1


print(stevec)