#! python3
#practiceing doing things from the terminal. 
#this file was created and done useing vim
#my goals for this project are to rename, write a program, 
#and be able to run the whole shebang from the terminal

book = {"mark" : "123",
        "mandy" : "456",
        "tony" : "789"}

print("UserName: ")
userName = input()
userName = userName.lower()
while(True):
    if userName in book:
        
        break
    else:
        print("--UserName not found--")
        print("--Create Account?--")
        createA = input()
        createA = createA.lower()
        print(createA)
        if createA == "yes":
            print("Enter your password: ")
            password = input()
            book[userName] = password
        
    print("never made it")
    break
