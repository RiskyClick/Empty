# This program says hello and asks for my name

print("Hello World!")
print("what is your name?") #ask for their name
myName = input()#needs to have number handling. will cause problem in digit is enterd
print("It is good to meet you, " + myName)
print("The length of your name is: ")
print(len(myName))
print("What is your age?") #asks for age
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year.")
