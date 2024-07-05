letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt_decrypt(text, mode, key):
    result = ' '
    if mode == 'd':
        key= -key
    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]
    return result

print()
print('...CAESAR CIPHER PROGRAM...')
print()

print('Do you want to Encrypt or Decrypt?')
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
    print('Encryption mode selected')
    print()
    key = int(input('Enter Key(1 to 26):'))
    text = input('Enter Text to Encrypt: ')
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f'Ciphertext: {ciphertext}')

elif user_input == 'd':
    print('Encryption mode selected')
    print()
    key = int(input('Enter Key(1 to 26):'))
    text = input('Enter Text to Encrypt: ')
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f'Plaintext: {plaintext}')