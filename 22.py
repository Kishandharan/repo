f1 = open("bitcoin_2017_to_2023.csv", "r")
f2=open("bitcoin2.txt","w")
f1.readline()
for i in range(0, 400000, 1):
    s1 = f1.readline()
    list1 = s1.split(",")
    for i in range(8,1,-1):
        if f"2023-0{i}-01 00:00:00" in list1[0]:
            f2.write(list1[0]+","+list1[1])
            f2.write("\n")
            print(list1[0], "-", list1[1])
f2.close()
