name = input("Enter your name: ")
mode = input("Enter mode(diff or inter): ")
input1 = input("Enter a num: ")
input2 = input("Enter a num: ")
input3 = input("Enter a num: ")
input4 = input("Enter a num: ")
print()
input5 = input("Enter a num: ")
input6 = input("Enter a num: ")
input7 = input("Enter a num: ")
input8 = input("Enter a num: ")
halfset1 = {input1, input2, input3, input4}
halfset2 = {input5, input6, input7, input8}
intersection = halfset1 & halfset2
difference = halfset1.difference(halfset2)
if mode == "diff":
    for i in difference:
        print(difference)
    
if mode == "inter":
    for i in intersection:
        print(i)
else:
    print()
    print(f"Sorry {name}. Your input has some errors:")
    print("Please enter the valid mode.\nOtherwise you will not get the output.")
    print("You can enter either 'diff' or 'inter'")
