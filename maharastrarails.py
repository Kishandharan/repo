f1 = open("railwaystations2.txt","r")
cons = f1.read()
list1 = cons.split(",")
mrail_count = 0
#index wanted: 4,9
if "Maharashtra" in list1[4]:
    mrail_count += 1

if "Maharashtra" in list1[9]:
    mrail_count += 1

print("Total number of stations in maharastra is:",mrail_count)
