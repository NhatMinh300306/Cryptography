# encrypt a string by reversing it

message = input()
translated = ''
i = len(message) - 1

while i >= 0:
    translated = translated + message[i]
    i = i - 1

print("The ciphertext is:", translated)