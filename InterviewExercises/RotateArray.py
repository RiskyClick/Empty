#Given an array, rotate the array to the right by k steps,
#where k is non-negative.

def rotate(array, k):
    print("Beging: " + str(array))
    while k > 0:
        array.insert(0,array.pop(len(array) - 1))
        k -= 1
        print("K: " + str(k))
        print("Rotation: " + str(array))

    print("End: " + str(array))

myList = [1,2,3,4,5,6,7]
rotate(myList, 3)
