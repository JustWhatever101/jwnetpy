name = "JwCustomSytax"
print(name + " Has been Imported")


def init(oname):
    if oname != "":
        name = oname
        print("JwCustomSytax Is Initilized as " + name)


def readFileAndprintLines(filename):
    print("Reading " + filename)
    f = open(filename, "r")
    print("Printing " + filename)
    print(f.read())
    print("Complete")


def ask(question):
    return input(question)
