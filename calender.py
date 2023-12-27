def cal1():
    list1 = ["M", "T", "W", "T", "F", "S", "S"]
    for i in range(0,7):
        print(list1[i], end = " ")
    print()
    for j in range(0,31,1):
        for i in range(j, j+7, 1):
            print((i%31)+1, end = " ")
    print()
cal1()
print()