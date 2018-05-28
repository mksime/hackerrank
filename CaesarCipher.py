def caesarCipher(s, k):
    # Complete this function
    encrypt = ""
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for char in s:
        chadd = ord(char) + k
        if char not in abc and char not in abc.upper():
            encrypt += char
        elif char in abc.upper() and chadd > ord('Z'):
            encrypt += chr(ord('A') - 1 + chadd - ord('Z'))
        elif char in abc.upper() and chadd < ord('A'):
            encrypt += chr(ord('Z') + 1 - (ord('A') - chadd))
        elif char in abc and chadd > ord('z'):
            encrypt += chr(ord('a') - 1 + chadd - ord('z'))
        elif char in abc and chadd < ord('a'):
            encrypt += chr(ord('z') + 1 - (ord('a') - chadd))
        else:
            encrypt += chr(chadd)
    return encrypt
    
print(caesarCipher('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*() -+:;[]{}?/|\"\">.\n<,çá§¬¢£³²¹~°ºª´µn”“©»«ºæßðđŋħłø→↓←ŧ®€?/ãà', -3))
#print(caesarCipher('A', 2))
