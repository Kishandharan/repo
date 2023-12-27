divisor = [2,4,6,8,10]
divident = int(input("Enter the divident: "))
flag = False
for Divisor in divisor:
    if divident % Divisor == 0:
        flag = True
        if flag == True:
            print(f"The number {divident} is divisble by one number in divisor list")
        else:
            print(f"The number {divident} is not divisble by any one number in divisor list")