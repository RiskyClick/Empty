#practive with expertion handeling
def div42by(div):
    try:
        return 42 / div
    except ZeroDivisionError:
        print("Error: Cant Do 0")

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

print("how many cats i got")
numCats = input()
try:
    if(int(numCats) >= 4):
        print("thats a lot of cats")
    elif int(numCats) < 0:
        print("dosent work that way")
    else:
        print("Get more cats")
except ValueError:
    print("Thats not a number")
