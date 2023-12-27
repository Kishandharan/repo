from mfo import *
print("Note: when you type the file name, please type it with the extension.")
mode1 = input("enter the mode: ")
mode2 = mode1.lower()
if mode2 == "create":
    name1 = input("enter the name of the file that should created: ")
    cfile(name=name1)
    print("Process finished")

elif mode2 == "write":
    name2 = input("In which file the content should be written: ")
    content1 = input("What content should be written: ")
    wfile(name=name2, content=content1)
    print("Process finished")

elif mode2 == "append":
    name3 = input("In which file the content should be appended: ")
    content2 = input("What content should be appended: ")
    afile(name=name3, content=content2)
    print("Process finished")

elif mode2 == "chece existence":
    name4 = input("enter the file name that should be checeed: ")
    if Dir.exist(name4):
        print("Yes! this file exists in this directory")
    else:
        print("No! the file your aseing does not exist in this directory")

elif mode2 == "execute a file":
    try:
        name5 = input("enter the file name that should be executed: ")
        print("execution of that file:")
        efile(name=name5)
    except:
        print("Sorry. an error occurred\nplease try again.")
        print("Process finished")

elif mode2 == "remove":
    name6 = input("enter the file name that should be removed: ")
    removef(name6)
    print("Process finished")

elif mode2 == "show list of files":
    print("The files available are:")
    for i in slf():
        print(i)

elif mode2 == "read":
    name7 = input("What file should be read: ")
    contents = rfile(name=name7)
    print(f"The contents of the file {name7} are: ")
    print(contents)
