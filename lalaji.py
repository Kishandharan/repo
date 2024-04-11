from flask import Flask
app = Flask(__name__)
app.route("/")
def prin():
    tep = 99
    return tep

if __name__ == "__main__":
    app.run()
