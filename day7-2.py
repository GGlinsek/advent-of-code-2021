f=open("day7-1","r").read().split(",")

prostori={}

for x in f:
    if int(x) not in prostori:
        prostori[int(x)]=0
    prostori[int(x)]+=1
print(prostori)

minimum=0
stevilka=0
for i in range(1919):
    buffer=0
    for x,y in prostori.items():
        buffer += (abs(x-i)*(abs(x-i)+1))/2*y
    if buffer<minimum or minimum==0:
        minimum=buffer
        stevilka=i

print(minimum)
print(stevilka)