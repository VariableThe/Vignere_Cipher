def vigenere_decoder():
    encoded_message = input('Please enter the text to be decoded: ')
    key = input('Please enter the key: ')

    # Normalize the key to uppercase for consistent handling
    key = key.upper()
    key_length = len(key)

    decoded_message = []
    key_index = 0

    for char in encoded_message:
        if char.isalpha():  # Process only alphabetic characters
            shift = (ord(char.upper()) - ord('A') - (ord(key[key_index % key_length]) - ord('A'))) % 26
            decoded_char = chr(shift + ord('A'))
            # Preserve the case of the original character
            decoded_char = decoded_char.lower() if char.islower() else decoded_char
            decoded_message.append(decoded_char)
            key_index += 1  # Move to the next letter in the key
        else:
            # Non-alphabetic characters are added unchanged
            decoded_message.append(char)

    decoded_message_str = ''.join(decoded_message)
    print('Decoded Message:', decoded_message_str)

# Call the function
vigenere_decoder()
