def reversStringIterative(str):
    revString = ""
    for i in range(len(str) - 1, -1, -1):
        revString += str[i]
    return revString

print(reversStringIterative("izhar is"))

def reversRecursive(str):
    if str == "":
        return ""
    return reversRecursive(str[1:]) + str[0]

print(reversRecursive("izhar"))