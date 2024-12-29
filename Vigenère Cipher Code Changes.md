This document presents my older code and the newer one while highlighting the differences/upgrades.

---
## Old Code:

### Encoder:
```python
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
```


### Decoder:
```python
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
```

---

## New Code:

### Encoder:
```python
def vigenere_cipher():

    message = input('Please enter the text to be encoded: ')

    key = input('Please enter the key: ')

    key = key.upper()

    key_length = len(key)

  

    encoded_message = []

    key_index = 0

  

    for char in message:

        if char.isalpha():  # Process only alphabetic characters

            shift = (ord(char.upper()) - ord('A') + ord(key[key_index % key_length]) - ord('A')) % 26

            encoded_char = chr(shift + ord('A'))

            # Preserve the case of the original character

            encoded_char = encoded_char.lower() if char.islower() else encoded_char

            encoded_message.append(encoded_char)

            key_index += 1

        else:

            # Non-alphabetic characters are added unchanged

            encoded_message.append(char)

  

    encoded_message_str = ''.join(encoded_message)

    print('Encoded Message:', encoded_message_str)

  

vigenere_cipher()
```

### Decoder: 
```python
def vigenere_decoder():

    encoded_message = input('Please enter the text to be decoded: ')

    key = input('Please enter the key: ')

    key = key.upper()

    key_length = len(key)

  

    decoded_message = []

    key_index = 0

  

    for char in encoded_message:

        if char.isalpha():  # Process only alphabetic characters

            shift = (ord(char.upper()) - ord('A') - (ord(key[key_index % key_length]) - ord('A'))) % 26

            decoded_char = chr(shift + ord('A'))

            # Preserve the case of the original character

            decoded_char = decoded_char.lower() if char.islower() else decoded_char

            decoded_message.append(decoded_char)

            key_index += 1

        else:

            # Non-alphabetic characters are added unchanged

            decoded_message.append(char)

  

    decoded_message_str = ''.join(decoded_message)

    print('Decoded Message:', decoded_message_str)

  

vigenere_decoder()
```

This code is now able to handle spaces and is case sensitive, providing a more accurate message
