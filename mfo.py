import os


def cfile(name):
    with open(name, "x"):
        name = str(name)


def rfile(name):
    name = str(name)
    f1 = open(name, "r")
    content2 = f1.read()
    return content2


def wfile(name, content):
    name = str(name)
    content = str(content)
    write = open(name, "w")
    write.write(content)


def afile(name, content):
    name = str(name)
    content = str(content)
    append = open(name, "a")
    append.write(content)


def slf():
    listoffiles = os.listdir()
    return listoffiles


def efile(name):
    exefile = open(name, "r").read()
    exec(exefile)


def getExtension(filename):
    file_det = os.path.splitext(f"/path/{filename}")
    return file_det[1]


class Dir:
    def exist(filename):
        listoffiles = os.listdir()
        if filename in listoffiles:
            return True
        else:
            return False


def removef(fname):
    if Dir.exist(fname):
        os.remove(fname)
    else:
        return "file does not exist"
