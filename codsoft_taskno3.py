import random
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopwrstuvwxyz"
chars = "!@#$%^&*()_-+={[]}\|';:.>,/?<*"
numbs = "0123456789"
unique = upper+lower+chars+numbs
password = ""
length = int(input("Enter the length of the password: "))
for i in range (length):
    password += random.choice(unique)
print(password)
