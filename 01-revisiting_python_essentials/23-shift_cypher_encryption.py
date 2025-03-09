# Define a function to encrypt the text using a shift cipher
# The function should take two parameters: the text to encrypt and the shift amount
def encrypt_text(text, shift_amount):
    encrypted = ""

    # Inside the function, create a loop that goes through each character of the text
    for c in text:
        # Check if the current character is an alphabetic character
        if c.isalpha():
            # Perform the character shift operation and append the result to the encrypted text
            # Hint: Use 'ord', 'chr', and modulo (%) operations to cyclically shift the letter by `shift`
            a = 'A' if c.isupper() else 'a'
            encrypted += chr((ord(c) - ord(a) + shift_amount) % 26 + ord(a))

        # If the character is not alphabetic, add it as is to the encrypted text
        else:
            encrypted += c
    print(encrypted)


# Outside the function, call your `encrypt_text` function with some sample text and a shift value to test it
encrypt_text('Encrypt me', 5)  # Jshwduy rj