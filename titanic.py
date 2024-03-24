survived = []
age = []
gender = []
f1 = open("titanic.csv", "r")
f1.readline()
info1 = f1.readlines()
len1 = len(info1)
for i in range(0,len1,1):
    info2 = info1[i].split(",")
    survived.append(info2[1])
    gender.append(info2[5])
    age.append(info2[6])
    if age[i] == "":
        age.pop(i)
        age.append("11")

child_survived = []
males_survived = []
females_survived = []
tsc = 0
tnsc = 0
tsm = 0
tnsm = 0
tsf = 0
tnsf = 0
for i in range(0,len(survived),1):
    if float(age[i])<=10 and survived[i] == '1':
        tsc += 1
    elif float(age[i])<=10 and survived[i] == '0':
        tnsc += 1 
    if float(age[i])>10 and gender[i] == "male" and survived[i] == "1":
        tsm += 1
    elif float(age[i])>10 and gender[i] == "male" and survived[i] == '0':
        tnsm += 1 
    if float(age[i])>10 and gender[i] == "female" and survived[i] == "1":
        tsf += 1
    elif float(age[i])>10 and gender[i] == "female" and survived[i] == '0':
        tnsf += 1 

print("Total childern survived:",tsc)
print("Total men survived:",tsm)
print("Total women survived:",tsf)
print("Total non-survived children:",tnsc)
print("Total non-survived men:",tnsm)
print("Total non-survived females:",tnsf)
