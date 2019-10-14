import re

def isPalindrome(s):
    regex = re.compile('[^a-zA-Z0-9]')
    s = regex.sub('', s)
    s = s.upper()
    t = s[::-1]
    if s == t:
        return True
    return False

stirng = "0P"
print(isPalindrome(stirng))
