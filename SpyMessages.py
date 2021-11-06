alphabet = "".join([chr(65 + r) for r in range(26)] * 2)

stringToEncrypt = input("please enter a message to encrypt")
stringToEncrypt = stringToEncrypt.upper()
shiftAmount = int(input("please enter a whole number from -25-25 to be your key"))
encryptedString = ""
for currentCharacter in stringToEncrypt:
    position = alphabet.find(currentCharacter)
    newPosition = position + shiftAmount
    if currentCharacter in alphabet:
        encryptedString = encryptedString + alphabet[newPosition]
    else:
        encryptedString = encryptedString + currentCharacter
print("your encrypted message is", encryptedString)