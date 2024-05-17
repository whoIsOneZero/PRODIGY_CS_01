import string
import sys

letters_lowercase = list(string.ascii_lowercase)
#letters_uppercase = list(string.ascii_uppercase)

def encrypt(plaintext, shift):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters_lowercase.find(letter)

def main():
    print("Caesar Cipher\n")
    input_message = input("Enter input message: ")
    shift_value = input("Enter a shift value (1 to 26): ")
   
    # Input validation
    try:
        shift_value = int(shift_value)
    except ValueError:
        print("Shift key should be a number!")
        sys.exit()

    if shift_value < 1 or shift_value > 26:
        print("Shift key out of range!")
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
        
if __name__ == "__main__":
    main()