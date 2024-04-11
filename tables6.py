f1 = open("in.txt", "r")
f2=open("out.txt", "w")
line=f1.readline()
temp1=line.split(",")
start=int(temp1[0])
end=int(temp1[1])

for j in range(start,end+1,1):
    for i in range(1,11,1):
        f2.write(str(j)+"x"+str(i)+"="+str(j*i))
        f2.write("\n")
    f2.write("\n")
f2.close()
