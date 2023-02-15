f=open("day2-1.txt","r")
naprej=0
dol=0
aim=0


for x in f.readlines():
    x = x.rstrip("\n")
    x = list(x.split(" "))
    print(x)
    if x[0] == "forward":
        naprej += int(x[1])
        dol += aim*int(x[1])
    elif x[0] == "up":
        aim -= int(x[1])
    elif x[0] == "down":
        aim += int(x[1])

print(dol*naprej)
