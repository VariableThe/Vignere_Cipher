def vigenere_cipher():
    message = input('Please enter the text to be encoded: ')
    key = input('Please enter the key: ')

    # Normalize the key to uppercase for consistent handling
    key = key.upper()
    key_length = len(key)

    encoded_message = []
    key_index = 0

    for char in message:
        if char.isalpha():  # Process only alphabetic characters
            shift = (ord(char.upper()) - ord('A') + ord(key[key_index % key_length]) - ord('A')) % 26
            encoded_char = chr(shift + ord('A'))
            # Preserve the case of the original character
            encoded_char = encoded_char.lower() if char.islower() else encoded_char
            encoded_message.append(encoded_char)
            key_index += 1  # Move to the next letter in the key
        else:
            # Non-alphabetic characters are added unchanged
            encoded_message.append(char)

    encoded_message_str = ''.join(encoded_message)
    print('Encoded Message:', encoded_message_str)

# Call the function
vigenere_cipher()
