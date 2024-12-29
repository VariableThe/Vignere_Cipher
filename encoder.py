message = input('Please enter the text to be encoded: ')
key = input('Please enter the key: ')
message = message.upper()
key = key.upper()
messageLength = len(message)
keyLength = len(key)
messageLetters = list(message)
keyLetters = list(key)

encoded_message = []

for i in range(messageLength):
     shift = (ord(messageLetters[i]) - ord('A') + ord(keyLetters[i % keyLength]) - ord('A')) % 26
     encoded_char = chr(shift + ord('A'))
     encoded_message.append(encoded_char)

encoded_message_str = ''.join(encoded_message)
print('Encoded Message:', encoded_message_str)
