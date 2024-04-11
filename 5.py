from flask import Flask
app = Flask(__name__)

@app.route("/")
def prison():
    count = 10
    prison = ["C"]*count
    lucky = []

    for i in range(0,count,1):
        prison[i] = "O"


    for i in range(1,count,2):
        prison[i] = "C"

    for j in range(2,count,1):  
        for i in range(j, count, j+1):
            if prison[i] == "C":
               prison[i] = "O"
            else:
               prison[i] = "C" 
        
    for i in range(0,count, 1):
        if prison[i] == "O":
            lucky.append(i+1)
    return "Hello"
if __name__ == "__main__":
    app.run()
