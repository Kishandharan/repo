import random as rd
randlist = []
for i in range(0,8,1):
    randlist.append(rd.randint(0,7))
list1 = ["A","B","C","D",""]
list2 = ["a","b","c","d"]
list3 = [1,2,3,4]
list4 = list1 + list2 + list3
pwd = ""
pwd = pwd + list1[randlist[0]] + list2[randlist[1]] + str(list3[randlist[2]]) + list4[randlist[3]] + list4[randlist[4]] + list4[randlist[5]] + list4[randlist[6]]+ list4[randlist[7]] 
print(pwd)
