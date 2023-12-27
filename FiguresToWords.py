import mfo
try:
    content1 = mfo.rfile("words6_en.txt")
    list1 = content1.split(",")
    res = list1[int(input("Enter a number: "))-1]
    print(res)
except IndexError:
    print("Number too large")
