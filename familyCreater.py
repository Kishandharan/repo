import os

son_names = ["Natraj", "Suresh"]
os.mkdir("Mother")
os.chdir("Mother")
os.mkdir("Sons")
os.chdir("Sons")
for i in son_names:
    open((i+".txt"), "x")
