def isAnagram(s,t):
#########BETTER METHOD#####
    nS = ''.join(sorted(s))
    nT = ''.join(sorted(t))
    if nS != nT:
        return False
    return True

##    for c in s:
##        if t.find(c) == -1:
##            return False
##    return True

first = "anagam"
sec = "nagaram"
print(isAnagram(first, sec))
