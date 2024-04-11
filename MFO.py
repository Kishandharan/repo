def cfile(name):
    with open(name, "x") as h:
     name = str(name)
     
def rfile(name):
    name = str(name)
    f1 = open(name, "r")
    content2 = f1.read()
    return content2

def wfile(name, content):
    name = str(name)
    content = str(content)
    Write = open(name, "w")
    Write.write(content)

def afile(name, content):
    name = str(name)
    content = str(content)
    Append = open(name, "a")
    Append.write(content)
