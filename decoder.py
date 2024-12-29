encoded_message = input('Please enter the text to be decoded: ')
key = input('Please enter the key: ')
key = key.upper()
messageLength = len(encoded_message)
keyLength = len(key)
encoded_messageLetters = list(encoded_message)
keyLetters = list(key)
decoded_message = []

for i in range(messageLength):
    shift = (ord(encoded_messageLetters[i]) - ord('A') - (ord(keyLetters[i % keyLength]) - ord('A'))) % 26
    decoded_char = chr(shift + ord('A'))
    decoded_message.append(decoded_char)

decoded_message_str = ''.join(decoded_message)
print('Decoded Message:', decoded_message_str)
