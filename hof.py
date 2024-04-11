def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def number(operation, x, y):
    return operation(x,y)

num1 = 10
num2 = 20
addop = number(add, num1, num2)
subtractop = number(subtract, num1, num2)
multiplyop = number(multiply, num1, num2)
divideop = number(divide, num1, num2)
print(addop)
print(subtractop)
print(multiplyop)
print(divideop)

        
