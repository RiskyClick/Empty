#first atemps at using a function where in we pass an arugment by referance
def hello(name):
    print("Hey")
    print("Hey,Hey")
    print("Hey,Hey, Hey")
    print("hello " + name)

hello("keith")
hello("bob")
hello("linda")

def plusOne(number):
    return number + 1

newNumber = plusOne(1)
newNumber = plusOne(newNumber)
newNumber = plusOne(newNumber)
newNumber = plusOne(newNumber)
print(newNumber)
print("cat","dog","Mouse",sep = "!")
