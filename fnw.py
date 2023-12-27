f1 = open("nums.txt", "w")
limit = 1000000
for i in range(1,limit+1,1):
    f1.write(str(i)+"\n")
f1.close()
