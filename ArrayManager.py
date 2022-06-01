def filetoArray(fsr):
    contents = []
    for line in fsr:
        contents.append(line)
    return contents


def arraytoString(array):
    string = ""
    for item in array:
        string = (string + str(item) + "\n")
    return string
