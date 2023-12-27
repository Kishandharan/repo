from mfo import *
start=int(input("Enter the start number: ") )
end=int(input("Enter the end number: "))
step=int(input("Enter the step number: "))
for i in range(start, end+1, step):
    wfile("f1.txt", i)