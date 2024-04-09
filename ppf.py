f1=open("pp.csv", "r")
maharastra_people = []
chennai_people = []
banglore_people = []
mumbai_people = []
person = []
place=[]

f1.readline()
while f1:
    line = f1.readline().replace("\n", "")
    temp1 = line.split(",")
    print(temp1)
    person.append(temp1[0])
    place.append(temp1[1])
    if f1.readline()=="":
        break
for i in range(0,len(person),1):
    temp2 = place[i]
    match temp2:
        case temp2:
            print(temp2, "people")
            print(person[i])
            print()
            
            
