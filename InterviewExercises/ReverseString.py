#this revers a list of chars as well as a givin int
def reverseString(charList, x):
    i = 0
    finalInt = ""
    while i < len(charList) - 1:
        charList.insert(i,charList.pop(len(charList) - 1))
        i += 1
    if x < 0:
        x = x * -1
        flop = True
    else:
        flop = False
    newInt = str(x)
    j = 0
    finalInt = ""
    if x < 0:
        finalInt += "-"
    while j < len(newInt):
        finalInt = finalInt + newInt[len(newInt)-1-j:len(newInt)-j]
        j += 1
    if int(finalInt) > 2147483647:
        return 0
    if flop:
        return int(finalInt) * -1
    else:
        return int(finalInt)
charList = ["h","e","l","l","o"]
ints = -123456789
print(reverseString(charList, ints))
