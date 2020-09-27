ListOfNames = ['Someing III','Louis IX', 'Louis VIII', 'Louis IX', 'Peper I']


def compare(jrc, jrn):
    first = 0
    sec = 0
    roman = {'I': 1, 'V': 5, 'X': 10,
             'L': 50, 'C': 100, 'D': 500,
             'M': 1000, 'IV': 4, 'IX': 9,
             'XL': 40, 'XC': 90, 'CD': 400,
             'CM': 900
             }
    if roman.get(jrc) is None:
        for c in jrc:
            first += roman.get(c)
    else:
        first = roman.get(jrc)
    if roman.get(jrn) is None:
        for c in jrn:
            sec += roman.get(c)
    else:
        sec = roman.get(jrn)

    return True if sec < first else False


def roman(theList) -> list:
    stillSwapping = False
    theList = iter(theList)
    newList = []
    current = next(theList, 'end')

    while 1:
        nextName = next(theList, 'end')
        if nextName == 'end':
            newList.append(current)
            if stillSwapping:
                roman(newList)
                return newList
            else:
                return newList
        else:
            jnc = current[:current.index(" ")]
            jnn = nextName[:nextName.index(" ")]

            jrc = current[current.index(" ") + 1:]
            jrn = nextName[nextName.index(" ") + 1:]
            if jnc == jnn:
                if compare(jrc, jrn):
                    newList.append(nextName)
                    stillSwapping = True
                else:
                    newList.append(current)
                    current = nextName
            else:
                newList.append(current)
                current = nextName

    print(newList)


ListOfNames.sort()
print(roman(ListOfNames))


