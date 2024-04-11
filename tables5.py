f1 = open("in.txt", "r")
line=f1.readline()
temp1=line.split(",")
start=int(temp1[0])
end=int(temp1[1])

for j in range(start,end+1,1):
    for i in range(1,11,1):
        print(j,"x",i,"=",j*i)
    print()

