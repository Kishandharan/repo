f1 = open("railwaystations1.txt", "r")
list1 = []
list2 = []
list3 = []
for i in range(0,10,1):  
    s1 = f1.readline()
    temp1 = s1.split(",")
    list1.append(temp1[0])
    list2.append(temp1[1])
    list3.append(temp1[4])
    
print(list1,"\n")
print(list2,"\n")
print(list3,"\n")
