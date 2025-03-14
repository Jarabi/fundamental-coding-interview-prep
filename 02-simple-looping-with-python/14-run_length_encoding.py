def encode_rle(s):
    encoded = ''
    current_char = None
    char_count = 0

    # Check if string is empty
    if s == '':
        return encoded

    for char in s:
        if char.isalnum():
            if char == current_char:
                char_count += 1
            else:
                if current_char is not None:
                    encoded += f"{current_char}{char_count}"
                current_char = char
                char_count = 1
    encoded += f"{current_char}{char_count}"
    return encoded

if __name__ == "__main__":
    text = "aaa@@bb!!c#d**e"
    print(encode_rle(text))  # a3b2c1d1e1