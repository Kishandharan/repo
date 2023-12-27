def TopperEng():
    f1 = open("marks.txt", "r")
    marksEng = []
    for i in range(0, 26, 1):
        s1 = f1.readline()
        list1 = s1.split(",")
        m1 = list1[3].split(":")
        m2 = int(m1[1])
        marksEng.append(m2)

    MaxMar = max(marksEng)
    return f"{MaxMar} is the highest mark in English"

def TopperMat():
    f1 = open("marks.txt", "r")
    marksEng = []
    for i in range(0, 26, 1):
        s1 = f1.readline()
        list1 = s1.split(",")
        m1 = list1[4].split(":")
        m2 = int(m1[1])
        marksEng.append(m2)

    MaxMar = max(marksEng)
    return f"{MaxMar} is the highest mark in Maths"

def TopperPhy():
    f1 = open("marks.txt", "r")
    marksEng = []
    for i in range(0, 26, 1):
        s1 = f1.readline()
        list1 = s1.split(",")
        m1 = list1[5].split(":")
        m2 = int(m1[1])
        marksEng.append(m2)

    MaxMar = max(marksEng)
    return f"{MaxMar} is the highest mark in Physics"

def TopperChem():
    f1 = open("marks.txt", "r")
    marksEng = []
    for i in range(0, 26, 1):
        s1 = f1.readline()
        list1 = s1.split(",")
        m1 = list1[6].split(":")
        m2 = int(m1[1])
        marksEng.append(m2)

    MaxMar = max(marksEng)
    return f"{MaxMar} is the highest mark in Chemistry"

def TopperBio():
    f1 = open("marks.txt", "r")
    marksEng = []
    for i in range(0, 26, 1):
        s1 = f1.readline()
        list1 = s1.split(",")
        m1 = list1[7].split(":")
        m2 = int(m1[1])
        marksEng.append(m2)

    MaxMar = max(marksEng)
    return f"{MaxMar} is the highest mark in Biology"
EnglishTopper = TopperEng()
MathsTopper = TopperMat()
PhysicsTopper = TopperPhy()
ChemistryTopper = TopperChem()
BiologyTopper = TopperBio()
print(EnglishTopper)
print(MathsTopper)
print(PhysicsTopper)
print(ChemistryTopper)
print(BiologyTopper)