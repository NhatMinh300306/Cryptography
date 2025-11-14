# Ceasar cipher technique: each letter of plain text is replaced
#                          by a letter with some fixed number of positions down with alphabet

def encrypt(plaintext):
    res = ''
    for char in plaintext:
        if 'a' <= char and char <= 'z':
            ascii_char = ord(char)
            new_char = (ascii_char - ord('a') + n) % 26 + ord('a')
            res += chr(new_char)

        elif 'A' <= char and char <= 'Z':
            ascii_char = ord(char)
            new_char = (ascii_char - ord('A') + n) % 26 + ord('A')
            res += chr(new_char)

        else:
            res += char
    return res

def decrypt(ciphertext):
    res = ''
    for char in ciphertext:
        if 'a' <= char and char <= 'z':
            ascii_char = ord(char)
            new_char = (ascii_char - n - ord('a')) % 26 + ord('a')
            res += chr(new_char)
        
        elif 'A' <= char and char <= 'Z':
            ascii_char = ord(char)
            new_char = (ascii_char - n - ord('A')) % 26 + ord('A')
            res += chr(new_char)

        else:
            res += char

    return res
# Hello
plaintext = input()
n = 4
res = ''

print("Plaintext: ", plaintext)
print("Ciphertext: ", encrypt(plaintext))
print("Plaintext: ", decrypt(encrypt(plaintext)) )