class ErrorManage:
    def alert(string = "your code has some errors"):
        print(string)

try:
    print(eval(input("Enter expression: ")))
except:
    ErrorManage.alert()
