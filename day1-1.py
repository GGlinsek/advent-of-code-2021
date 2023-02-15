f = open("day1-1.txt","r")
prejsna = 0
i=0
for x in f.readlines():
    x = x.rstrip("\n")
    nova = int(x)
    if nova > prejsna != 0:
        i += 1
    prejsna = int(x)


print(i)
