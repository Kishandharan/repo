import random as rd
def function1(length):
    pwd = ""
    list1 = ["A", "B", "C", "D"]
    list2 = ["a","b","c","d"]
    list3 = [0,1,2,3,4,5,6,7,8,9]
    list4 = list1+list2+list3
    r1 = rd.randint(0,3)
    r2 = rd.randint(0,3)
    r3 = rd.randint(0,9)
    pwd = pwd + str(list1[r1])
    pwd = pwd + str(list2[r2])
    pwd = pwd + str(list3[r3])

    for i in range(0, length, 1):
        r4 = rd.randint(0,17)
        pwd = pwd + str(list4[r4])
    return(pwd)
def function2(length):
    list1 = []
    for i in range(0,length,1):
        result1 = function1(5)
        list1.append(result1)
    return list1

result = function2(10)
f1 = open("password_gen_container.txt", "w")
list1 = []
for i in range(0, len(result), 1):
    list1.append(result[i])
for i in list1:
    f1.write(i+"\n")
f1.close()
