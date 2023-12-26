list1 = []
list2= []
for i in range(0,20,1):
    list1.append(i+1)
f1 = open("words.txt")
for i in range(0,20,1):
    list2.append(f1.readline().replace("\n", ""))
for i in range(0,20,1):
    print(list1[i],"-",list2[i])
    
part1=20
for i in range(1,10,1):
    part2=i
    num1=part1+part2
    print(num1,"-",list2[part1-1],list2[part2-1])
list1.append(30)
list2.append(f1.readline().replace("\n", ""))
len1 = len(list1)
print(list1[20], "-",list2[20])

part1=30
for i in range(1,10,1):
    
    part2=i
    num1=part1+part2
    print(num1, "-", list2[20], list2[part2-1])
