asciiMin = 32   
asciiMax = 126  

key = 314159    
key = str(key)  

message = input('Type messages for decryption')

messDecr = ""

for index in range(0, len(message)):
    char = ord(message[index])

    if char < asciiMin or char > asciiMax:
        messDecr += message[index]

    else:
        ascNum = char - int(key[index % len(key)])
        if ascNum < asciiMin:
            ascNum += (asciiMax - asciiMin)
        messDecr += chr(ascNum)

print(messDecr)