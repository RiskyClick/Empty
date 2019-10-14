#returns the index of the first unique char in a string
def firstUniqChar(s):
    for i, c in enumerate(s):
        counter = s.count(c)
        if counter < 2:
            return i
    return -1

string = "vvpbxaqjinettqfwggigrmvoufibbahvkrmkmpncmwdbqwahjle"
print(firstUniqChar(string))
