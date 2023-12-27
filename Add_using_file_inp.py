from mfo import *
f1 = rfile("text.txt")
split = f1.split(",")
print(int(split[0])+int(split[1])+int(split[2])+int(split[3]))
