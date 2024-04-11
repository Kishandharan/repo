start=int(input("Enter start number: "))
end=int(input("Enter end number: "))

for j in range(start,end+1,1):
    for i in range(1,11,1):
        print(j,"x",i,"=",j*i)
    print()

