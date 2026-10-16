import string

def decrypt(encrypted_text, shift_value):
    # Define English lowercase alphabet letters
    alphabet = string.ascii_lowercase
    decrypted_text = ""

    # Loop through each character in the encrypted text
    for char in encrypted_text:
        if char.lower() in alphabet:
            # Identify current index of character
            current_index = alphabet.index(char.lower())

            # Calculate new index by shifting backward
            new_index = (current_index - shift_value) % 26
            decrypted_char = alphabet[new_index]

            # Preserve character casing (uppercase vs lowercase)
            if char.isupper():
                decrypted_char = decrypted_char.upper()

            decrypted_text += decrypted_char
        else:
            # Retain spaces and special symbols without modification
            decrypted_text += char

    # Output decrypted text result
    print(f"\n🔓 Decrypted Message : {decrypted_text}")


# --- User Interface ---
print("=" * 35)
print(" 🔓   CAESAR CIPHER DECRYPTER   🛡️ ")
print("=" * 35)

# Prompt inputs from user
user_message = input("\n📝 Enter encrypted message : ")
shift_number = int(input("🔢 Enter shift number       : "))

# Invoke decryption function
decrypt(user_message, shift_number)

print("=" * 35)