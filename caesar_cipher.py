import string
import sys

letters_lowercase = string.ascii_lowercase
letters_uppercase = string.ascii_uppercase

def encrypt(plaintext, shift):
    result = ''
    for letter in plaintext:
        if letter.islower():
            index = letters_lowercase.find(letter)
            # wrap around the range of alphabets
            new_index = (index + shift) % 26
            # accumulate encrypted message
            result += letters_lowercase[new_index]
        elif letter.isupper():
            index = letters_uppercase.find(letter)
            new_index = (index + shift) % 26
            result += letters_uppercase[new_index]
        else:
            result += letter
    return result

def decrypt(cipherText, shift):
    result = ''
    for letter in cipherText:
        if letter.islower():
            index = letters_lowercase.find(letter)
            # wrap around the range of alphabets
            new_index = (index - shift) % 26
            # accumulate decrypted message
            result += letters_lowercase[new_index]
        elif letter.isupper():
            index = letters_uppercase.find(letter)
            new_index = (index - shift) % 26
            result += letters_uppercase[new_index]
        else:
            result += letter
    return result

def main():
    print("Caesar Cipher\n")
    input_message = input("Enter input message: ")
    shift_value = input("Enter a shift value (1 to 26): ")
   
    # Input validation
    try:
        shift_value = int(shift_value)
    except ValueError:
        print("Shift key should be an integer!")
        sys.exit()

    if shift_value < 1 or shift_value > 26:
        print("Shift key should be between 1 and 26!")
        sys.exit()

    print("\nWhat operation do you want to perform?")
    operation = input("Encryption -> 1, Decryption -> 2: ")
    
    # Input validation
    try:
        operation = int(operation)
    except ValueError:
        print("Option entered is not a number!")
        sys.exit()

    if operation != 1 and operation != 2:
        print("Invalid operation option entered!")
        sys.exit()
        
    if operation == 1:
        result = encrypt(input_message, shift_value)
        operation_name = "encrypted"
    else:
        result = decrypt(input_message, shift_value)
        operation_name = "decrypted"
    
    print(f"The {operation_name} message is: {result}")
        
if __name__ == "__main__":
    main()