import MFO
import os
mode = input("Enter the mode: ")
match(mode):
    case "Overwrite":
        f1 = input("What file to write: ")
        print("Write '\ n' without space if you want to write the content in new line.")
        print("Note: if you enter a file that does not exist,\nthe file that you entered will be created \n and the content is written.")
        print("Type '.txt' after you write the name of file to specify the the file is a text file, otherwise you cannot open the file.")
        f2 = input("What to write: ")
        MFO.wfile(f1, f2)
        print("Process finished")
    case "Create":
        c1 = input("What is the name of file that should be created: ")
        MFO.cfile(c1)
    case "remove":
        print("Please enter the valid file name, otherwise you will get an error.")
        r = input("Which file to remove: ")
        os.remove(r)
