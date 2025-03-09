def encrypt_string(text):
    encrypted = []
    for c in text:
        # Check if `c` is a letter different from 'z' and 'Z'. If so, increment by 1.
        if c.isalpha():
            if c not in ('z', 'Z'):
                encrypted.append(chr(ord(c) + 1))
            # If 'c' is 'z', change it to 'a'. If 'c' is 'Z', change it to 'A'.
            else:
                encrypted.append(chr(ord(c) - 25))
        # Otherwise, keep 'c' unchanged and add it to the encrypted list.
        else:
            encrypted.append(c)
    return ''.join(encrypted)


# Encrypt the string "Hello, Python!" by shifting each letter in the alphabet one by one.
encrypted_text = encrypt_string("Hello, PythonZ!")
print("The encrypted text is:", encrypted_text) # Should print out "Ifmmp, QzuipoA!"