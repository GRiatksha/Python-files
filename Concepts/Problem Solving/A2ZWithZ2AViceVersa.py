def getConvertedString(inputString):
    outputString = ""
    for currentCharacter in inputString:
        zASCIIValue = ord('z')
        aASCIIValue = ord('a')
        characterASCIIValue = ord(currentCharacter)
        diffValue = zASCIIValue - characterASCIIValue
        convertedValue = chr(diffValue + aASCIIValue)
        # print(zASCIIValue, characterASCIIValue, diffValue, convertedValue)
        outputString += convertedValue

    return outputString


print("converted string", getConvertedString("abcdxyz"))
print("converted string", getConvertedString("apple"))