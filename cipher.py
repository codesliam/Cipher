import random
import string

#shift a letter by an amount
def shiftLetter(character,shiftAmount):

    #get ascii for each character
    ascii = ord(character)

    #if ascii is uppercase (order between 65 - 90)
    #get it to be between 0-25 to shift it mod 26, 
    #then add 65 to get back to uppercase
    if (ascii >= 65) and (ascii <= 90):
        shiftedCharacter = (ascii - 65 + shiftAmount) % 26 + 65

    #similar process for lowercase letters (order between 97 to 122)
    elif (ascii >= 97) and (ascii <= 122):
        shiftedCharacter = (ascii - 97 + shiftAmount) %26 + 97
    
    #last case: if character isn't a letter, leave it
    else:
        shiftedCharacter = ascii

    #return the now shifted character
    return chr(shiftedCharacter)


def generatePad(length):
    #create a random list of uppercase letters of inputted length
    pad = []
    for i in range(length):
        pad.append(random.choice(string.ascii_uppercase))
    return ''.join(pad)

    
def generatepadFile(length, fileName):
    #generate and return a file containing this pad
    padFile = generatePad(length)
    file = open(fileName, "w")
    file.write(padFile)
    file.close()

#encipher a message character by character based on a pad
def encipherMessage(message, pad):
        encipheredMessage = []
        padCharacter = 0
        #iterate over each character in message
        for i in range(0,len(message)):
            messageCharOrder = ord(message[i])
            #if the message character is a letter, shift it and add to encrypted message
            if ((messageCharOrder >= 65) and (messageCharOrder<= 90) or (messageCharOrder >= 97) and (messageCharOrder <= 122)):
                encipheredMessage.append(shiftLetter(message[i], ord(pad[padCharacter])-65))
                padCharacter += 1
            #if the message character is not a letter, add to encrypted message without change
            else:
                encipheredMessage.append(message[i])
        return "".join(encipheredMessage)
#decipher a message character by character based on a pad
def decipherMessage(message, pad):
    decipheredMessage = []
    padCharacter = 0
    #iterate over each character in message
    for i in range(0,len(message)):
        messageCharOrder = ord(message[i])
        #if the message character is a letter, shift it and add to decrypted message
        if ((messageCharOrder >= 65) and (messageCharOrder<= 90) or (messageCharOrder >= 97) and (messageCharOrder<= 122)):
            decipheredMessage.append(shiftLetter(message[i], - ord(pad[padCharacter])-65))
            padCharacter += 1
        #if the message character is not a letter, add to decrypted message without change
        else:
            decipheredMessage.append(message[i])
    return "".join(decipheredMessage)

#decipher a message with the pad file
def decipher(message, padFile):
    file = open(padFile)
    pad = file.read()
    return decipherMessage(message, pad)

#encipher a message with the pad file
def encipher(message, padFile):
    file = open(padFile)
    pad = file.read()
    return encipherMessage(message, pad)

#test the cipher with the example pad.txt and message.txt
with open("encrypted-message.txt") as file:
   text = file.read()
with open("decrypted-message.txt", "w") as file:
    file.write(decipher(text, "pad.txt"))

#test enciphering with generating own pad and "Good morning" message file
generatepadFile(1200, "pad1.txt")
with open("goodmorningmessage.txt") as file:
   text = file.read()
with open("encryptedgoodmorning.txt", "w") as file:
    file.write(encipher(text, "pad1.txt"))

#test deciphering the "Good morning" message that was enciphered above
with open("encryptedgoodmorning.txt") as file:
   text = file.read()
with open("decryptedgoodmorning.txt", "w") as file:
    file.write(decipher(text, "pad1.txt"))