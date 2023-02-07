plaintext = input("Enter the coded text: ")

key = int(input("Enter the distance: "))

print()

cipherText = ""

for x in plaintext:
    cipherText += chr(ord(x) - key)

print(cipherText)

