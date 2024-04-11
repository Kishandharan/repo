while True:
    inp1 = int(input("Enter first number: "))#This function takes first input from the user.
    inp2 = int(input("Enter second number: ")) #This function takes second input from the user.
    inp3 = int(input("Enter third number: ")) #This function takes third input from the user.
    inp4 = int(input("Enter fourth number: ")) #This function takes fourth input from the user.
    list1 = [inp1, inp2, inp3, inp4] #This list stores all the input from the user.
    even_numbers = list(filter(lambda x:(x%2 == 0) , list1))#this function filters all the even numbers from the user input. 
    print("even numbers are: ")
    for i in even_numbers:
        print(i)
    print()
