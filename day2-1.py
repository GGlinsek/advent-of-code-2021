f=open("day2-1.txt","r")
naprej=0
dol=0

for x in f.readlines():
    x = x.rstrip("\n")
    x = list(x.split(" "))
    print(x)
    if x[0]=="forward":
        naprej += int(x[1])
    elif x[0]== "up":
        dol -= int(x[1])
    elif x[0]== "down":
        dol += int(x[1])

print(dol*naprej)
