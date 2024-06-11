import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
let = int(input("How many letters would you like in your password?\n")) 
sym = int(input(f"How many symbols would you like?\n"))
num = int(input(f"How many numbers would you like?\n"))

ek = ""
do =""
then = ""

for i in range(let):
    one=random.choice(letters)
    ek+=one
for i in range(sym):
    two=random.choice(symbols)
    do+=two
for i in range(num):
    three=random.choice(numbers)
    then+=three


full=[]
for i in ek:
    full.append(i)

for i in do:
    full.append(i)

for i in then:
    full.append(i)


random.shuffle(full)
fullin="".join(full)
print(fullin,end='')