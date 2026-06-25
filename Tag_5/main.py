import random

buchstaben = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nummern = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbole = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_buchstabe = int(input("How many letters would you like in your password?\n"))
nr_symbole = int(input(f"How many symbols would you like?\n"))
nr_nummer = int(input(f"How many numbers would you like?\n"))

# LEICHTES LEVEL:
# passwort = ""
#
# for zeichen in range(0, nr_buchstabe):
#     passwort += random.choice(buchstaben)
#
# for zeichen in range (0, nr_symbole):
#     passwort += random.choice(symbole)
#
# for zeichen in range (0, nr_nummer):
#     passwort += random.choice(nummern)
#
# print(passwort)


#HARTES LEVEL
password_liste = []
for zeichen in range(0, nr_buchstabe):
    password_liste.append(random.choice(buchstaben))

for zeichen in range(0, nr_symbole):
    password_liste.append(random.choice(symbole))

for zeichen in range(0, nr_nummer):
    password_liste.append(random.choice(nummern))

random.shuffle(password_liste)

passwort = ""

for zeichen in password_liste:
    passwort += zeichen

print(f"Your password is: {passwort}")