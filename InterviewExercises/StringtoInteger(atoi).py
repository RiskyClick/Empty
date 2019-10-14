import re

def myAtoi(str):
    regex = re.compile('[ ]')
    str = regex.sub('', str)
    theNeg = False
    if str == "":
        return 0
    if str[0].isdigit() == False:
        if str[0] != "-":
            return 0
        else:
            theNeg = True
    str = re.sub("\D", "", str)
    if len(str) > 10:
        if theNeg:
            return -2147483648
        else:
            return 2147483648
    if theNeg:
        if str == "":
            return 0
        return -1 * int(str)
    return int(str)

string = "-"
print(myAtoi(string))
