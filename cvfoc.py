import os
import shutil
from time import sleep
import datetime as dt
print("Note: This app is only for windows")
un = input("Enter user name(on this computer): ")
path_memory = []
file_memory = []
folder_memory = []
command_memory = []
time_memory = []
path_shortcuts = dict()
default_sc = f"Desktop : C:/Users/{un}/OneDrive/Desktop"
des = f"C:/Users/{un}/OneDrive/Desktop"
os.chdir(des)
if not os.path.exists("FinnyFoUsers.txt"):
    createFinnyFoUsers = open("FinnyFoUsers.txt", "x")
ap  = open("FinnyFoUsers.txt", "a")
FinnyFo_Users_r = open("FinnyFoUsers.txt", "r")
users = FinnyFo_Users_r.readlines()
users2 = []
for i in users:
    if "\n" in i:
        users2.append(i.replace("\n", ""))
    else:
        users2.append(i)
print("Users available:")
for user in users2:
    print(user)
print()
self_username = input("Enter your user name(On finnyfo): ")
if self_username in users2:
    while True:
        try:
            command = input("<< COMMAND >>")
            if command.startswith("shortcut"):
                command_memory.append("shortcut")
                name = command.split(" ", 1)[1]
                path = input("<< PATH >>")
                path_memory.append(path)
                path_shortcuts.update({name:path})
                
            elif command.startswith("cd"):
                command_memory.append("cd")
                d1 = command.split(" ", 1)[1]
                if d1 == "Desktop":
                    path_memory.append("C:/Users/KRISHNA/OneDrive/Desktop")
                    os.chdir("C:/Users/KRISHNA/OneDrive/Desktop")
                elif d1 in path_shortcuts.keys():
                    path_memory.append(path_shortcuts.get(d1))
                    os.chdir(path_shortcuts.get(d1))
                else:
                    path_memory.append(d1)
                    os.chdir(d1)                
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - cd")
                
            elif command.startswith("rename"):
                filename = command.split(" ", 1)[1]
                if os.path.isfile(filename):
                    file_memory.append(filename)
                elif os.path.isdir(filename):
                    folder_memory.append(filename)
                command_memory.append("rename")
                name = input("<< NAME >>")
                os.rename(filename, name)
                print("Renamed successfully!")
                
            elif command.startswith("read"):
                command_memory.append("read")
                d2 = command.split(" ", 1)[1]
                file_memory.append(d2)
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - read")
                f1 = open(d2, "r")
                print(f1.read())
                f1.close()
                
            elif command.startswith("write"):
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - write")
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
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - append")
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
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - create")
                command_memory.append("create")
                n1 = command.split(" ", 1)[1]
                file_memory.append(n1)
                f1 = open(n1, "x")
                f1.close()
                print("Created successfully!")
                
            elif command.startswith("delete"):
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - delete")
                command_memory.append("delete")
                j = command.split(" ",1)[1]
                file_memory.append(j)
                os.remove(j)
                print("Deleted successfully!")
                
            elif command.startswith("cf"):
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - cf")
                command_memory.append("cf")
                n2 = command.split(" ", 1)[1]
                folder_memory.append(n2)
                os.mkdir(n2)
                print("Folder created successfully!")
                
            elif command.startswith("df"):
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - df")
                command_memory.append("df")
                fn = command.split(" ",1)[1]
                folder_memory.append(fn)
                shutil.rmtree(fn)
                print("Folder deleted successfully!")
                
            elif command == "listdir":
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - listdir")
                command_memory.append("listdir")
                for i in os.listdir():
                    print(i)
                    
            elif command == "quit":
                break
            
            elif command == "get_cwd":
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - get_cwd")
                print(os.getcwd())
                
            elif command == "get_path_memory":
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - get_path_memory")
                command_memory.append("get_path_memory")
                if len(path_memory) > 0:
                    for mem in path_memory:
                        print(mem)
                else:
                    print("No path memory")
                    
            elif command == "get_file_memory":
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - get_file_memory")
                command_memory.append("get_file_memory")
                if len(file_memory) > 0:
                    for mem in file_memory:
                        print(mem)
                else:
                    print("No file memory")
                    
            elif command == "get_folder_memory":
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - get_folder_memory")
                command_memory.append("get_folder_memory")
                if len(folder_memory) > 0:
                    for mem in folder_memory:
                        print(mem)
                else:
                    print("No folder memory")
                    
            elif command == "get_command_memory":
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - get_command_memory")
                command_memory.append("get_command_memory")
                for mem in command_memory:
                    print(mem)

            elif command.startswith("set_username_oc"):
                username = command.split(" ",1)[1]
                default_sc = f"Desktop : C:/Users/{username}/OneDrive/Desktop"
                
            elif command == "getcommands":
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - get_commands")
                command_memory.append("getcommands")
                print("getcommands")
                print("rename")
                print("cd")
                print("read")
                print("write")
                print("append")
                print("delete")
                print("cf")
                print("df")
                print("getcwd")
                print("listdir")
                print("shortcut")
                print("get_path_memory")
                print("get_file_memory")
                print("get_folder_memory")
                print("get_command_memory")
                print("get_ctime_memory")
                print("get_path_shortcuts")
                print("get_default_shortcut")
                print("set_username_oc")
                print("quit")
            elif command == "get_ctime_memory":
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - get_ctime_memory")
                command_memory.append("get_ctime_memory")
                for mem in time_memory:
                    print(mem)
                    
            elif command == "get_path_shortcuts":
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - get_path_shortcuts")
                command_memory.append("get_path_shortcuts")
                for i in path_shortcuts:
                    print(i, ":", path_shortcuts.get(i))
                    
            elif command == "get_default_shortcut":
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - get_default_shortcut")
                command_memory.append("get_default_shortcuts")
                print(default_sc)
                
            elif command.startswith("delsc"):
                command_memory.append("delsc")
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - delsc")
                short_name = command.split(" ", 1)[1]
                path_shortcuts.pop(short_name)
                
            elif command.startswith("rashc"):
                command_memory.append("rashc")
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - rashc")
                sh = command.split(" ",1)[1]
                path = input("<< PATH >>")
                path_memory.append(path)
                path_shortcuts[sh] = path

            elif command == "get_current_username":
                command_memory.append("get_current_username")
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - get_current_username")
                print(self_username)

            elif command == "get_users":
                command_memory.append("get_users")
                time_memory.append(f"{dt.datetime.now().strftime('%X')} - get_users")
                print("Users available:")
                for user in users2:
                    print(user)
            elif command.startswith("copy"):
                fn = command.split(" ",1)[1]
                f1 = open(fn,"r")
                cons=f1.read()
                print(cons)
                dest = input("<<DEST FILE>>")
                f2=open(dest, "w")
                f2.write(cons)
                f2.close()
            else:
                print("Invalid command")
                
        except:
            print("Sorry, an error occurred!")
            quitinput = input("Do you want to quit: ").lower()
            if quitinput == "yes":
                break
            elif quitinput == "no":
                pass
else:
    print("Sorry, You are a unknown user.\nTo add a user, add it on FinnyFoUsers.txt on the desktop in a new line.")
    sleep(9)
