#! python3
#Was an interview question i was givint.givien a string filled with any given letter of any size,
#how many times dose the 'build' string need to be replicated to produce the given large text
import random
import string
import pprint

largeString = ""#Enter the large amount of text here that you wish to replicate
build = ""
count = 1
sticker = {}
bigText = {}

#This generates a random sticker
for i in range(0, random.randint(0,100)):
    build = build + random.choice(string.printable)

#dictonary for the random generated sticker. separates the uniqu chars and counts how many there are in  the generated sicker
for k in build:
    sticker.setdefault(k, 0)
    sticker[k] = sticker[k] + 1

#dictionary for the large text, same priciple as above
for j in largeString:
    bigText.setdefault(j, 0)
    bigText[j] = bigText[j] + 1

#rolls though the dictonary in the large text
for key, val in bigText.items():
    if(sticker.get(key, "NULL") == "NULL"):#if there is key in said large text it cannont be acomplished therefore quits
        print("Not able to recreate the large string")
        exit()
    while(True):#increments count till it matches the value in the large text dictionary
        if(sticker.get(key) * count < val):
            count = count + 1
        elif(sticker.get(key) * count >= val):
            break

if(count == 1):
    print("You need only" + str(count) + " copy of the sticker to replicate the large text")
else:
    print("You need " + str(count) + " copys of the sticker to replicate the large text")
