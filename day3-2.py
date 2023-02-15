f=open("day3-1","r").read().split("\n")
day3=open("day3 help.txt","w")
d=[]

for x in f:
   if x[6]=="1":
       d.append(x)
for x in d:
    day3.write(x+"\n")
day3.close()

#010110110011




