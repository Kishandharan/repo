import os
import shutil
from time import sleep
path_memory = []
file_memory = []
folder_memory = []
command_memory = []
while True:
    try:
        command = input("<< COMMAND >>")
        if command.startswith("cd"):
            command_memory.append("cd")
            d1 = command.split(" ", 1)[1]
            path_memory.append(d1)
            os.chdir(d1)
        elif command.startswith("read"):
            command_memory.append("read")
            d2 = command.split(" ", 1)[1]
            file_memory.append(d2)
            f1 = open(d2, "r")
            print(f1.read())
            f1.close()
        elif command.startswith("write"):
            command_memory.append("write")
            d3 = command.split(" ", 1)[1]
            file_memory.append(d3)
            print("<< WRITE CONTENTS >>")
            f2 = open(d3, "w")
            while True:
                con=input()
                if con=="quit":
                    break
                f2.write(con+"\n")
            f2.close()
            print("Written successfully!")
        elif command.startswith("append"):
            command_memory.append("append")
            d4 = command.split(" ", 1)[1]
            file_memory.append(d4)
            print("<< WRITE CONTENTS >>")
            f3 = open(d4, "a")
            while True:
                con=input()
                f3.write(con)
            print("Written successfully!")
        elif command.startswith("create"):
            command_memory.append("create")
            n1 = command.split(" ", 1)[1]
            file_memory.append(n1)
            f1 = open(n1, "x")
            f1.close()
            print("Created successfully!")
        elif command.startswith("delete"):
            command_memory.append("delete")
            j = command.split(" ",1)[1]
            file_memory.append(j)
            os.remove(j)
            print("Deleted successfully!")
        elif command.startswith("cf"):
            command_memory.append("cf")
            n2 = command.split(" ", 1)[1]
            folder_memory.append(n2)
            os.mkdir(n2)
            print("Folder created successfully!")
        elif command.startswith("df"):
            command_memory.append("df")
            fn = command.split(" ",1)[1]
            folder_memory.append(fn)
            shutil.rmtree(fn)
            print("Folder deleted successfully!")
        elif command == "getcwd":
            command_memory.append("getcwd")
            print(os.getcwd())
        elif command == "listdir":
            command_memory.append("listdir")
            for i in os.listdir():
                print(i)
        elif command == "quit":
            break
        elif command == "get_path_memory":
            command_memory.append("get_path_memory")
            for mem in path_memory:
                print(mem)
        elif command == "get_file_memory":
            command_memory.append("get_file_memory")
            for mem in file_memory:
                print(mem)
        elif command == "get_folder_memory":
            command_memory.append("get_folder_memory")
            for mem in folder_memory:
                print(mem)
        elif command == "get_command_memory":
            command_memory.append("get_command_memory")
            for mem in command_memory:
                print(mem)
        elif command == "getcommands":
            command_memory.append("getcommands")
            print("getcommands")
            print("cd")
            print("read")
            print("write")
            print("append")
            print("delete")
            print("cf")
            print("df")
            print("getcwd")
            print("listdir")
            print("quit")
            print("get_path_memory")
            print("get_file_memory")
            print("get_folder_memory")
            print("quit")
        else:
            print("Invalid command")
    except:
        print("Sorry, an error occurred!")
        quitinput = input("Do you want to quit: ").lower
        if quitinput == "yes":
            break
        elif quitinput == "no":
            pass
