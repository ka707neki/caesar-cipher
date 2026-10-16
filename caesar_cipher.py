# Import string library to access English alphabet characters
import string

# Function to encrypt text using the Caesar cipher algorithm
def encrypt(message, shift):
    # Create string containing lowercase English alphabet from a to z
    alphabet = string.ascii_lowercase
    encrypted_message = ""

    # Iterate through every character in the input string
    for letter in message:
        # Check if character is part of the English alphabet
        if letter.lower() in alphabet:
            # Find current position of character in alphabet
            original_position = alphabet.index(letter.lower())

            # Calculate new position after shift (using modulo 26 to wrap around z)
            new_position = (original_position + shift) % 26
            encrypted_letter = alphabet[new_position]

            # Preserve letter casing if original character was uppercase
            if letter.isupper():
                encrypted_letter = encrypted_letter.upper()

            # Append encrypted character to final output string
            encrypted_message += encrypted_letter
        else:
            # Retain spaces, special characters, and numbers as-is without encryption
            encrypted_message += letter

    # Output the resulting encrypted string
    print(f"\n🔐 Encrypted Message : {encrypted_message}")


# --- Main Application ---

# Print banner frame and title
print("=" * 35)
print(" 🛡️   CAESAR CIPHER ENCRYPTER   🛡️ ")
print("=" * 35)

# Get message input and shift value from user
user_message = input("\n📝 Enter a message      : ")
shift_number = int(input("🔢 Enter a shift number : "))

# Execute cipher function with user inputs
encrypt(user_message, shift_number)

# Print ending divider line
print("=" * 35)