f1=open("pp.csv", "r")
maharastra_people = []
chennai_people = []
banglore_people = []
mumbai_people = []

f1.readline()
while f1:
    line = f1.readline().replace("\n", "")
    temp1 = line.split(",")
    print(temp1)
    person = temp1[0]
    place = temp1[1]
    if f1.readline()=="":
        break
    match place:
        case "Maharastra":
            maharastra_people.append(person)
        case "Chennai":
            chennai_people.append(person)
        case "Banglore":
            banglore_people.append(person)
        case "Mumbai":
            mumbai_people.append(person)

print("Maharastra people: ")
for i in maharastra_people:
    print(i)
    print()

print("Chennai people: ")
for i in chennai_people:
    print(i)
    print()

print("Banglore people: ")
for i in banglore_people:
    print(i)
    print()

print("Mumbai people: ")
for i in mumbai_people:
    print(i)
    print()

