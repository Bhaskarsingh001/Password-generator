import random

numbers = "123456789"
letters = "abcDEFghiJKLmnoPQRstuVWXyz"
mixed = letters + numbers + "@#$%&/"

print("1. Numbers only")
print("2. Letters only")
print("3. Mixed")

choice = input("Choose option: ")
length = int(input("Enter password length: "))

if choice == "1":
    characters = numbers

elif choice == "2":
    characters = letters

else:
    characters = mixed

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)