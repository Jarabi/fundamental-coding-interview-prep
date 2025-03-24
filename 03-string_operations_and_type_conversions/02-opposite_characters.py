def solution(input_str):
    UPPER_A = ord('A')
    UPPER_Z = ord('Z')
    LOWER_A = ord('a')
    LOWER_Z = ord('z')

    replaced_chars = []
    for c in input_str:
        c_code = ord(c)

        if UPPER_A <= c_code <= UPPER_Z:
            # Check if c is uppercase
            replaced_chars.append(chr(UPPER_Z - (c_code - UPPER_A)))
        elif LOWER_A <= c_code <= LOWER_Z:
            # Check if c is lowercase
            replaced_chars.append(chr(LOWER_Z - (c_code - LOWER_A)))
        else:
            replaced_chars.append(c)

    replaced = ''.join(replaced_chars)
    split_str = replaced.split(" ")

    if len(split_str) > 1:
        return f"{split_str[-1]} {' '.join(split_str[:-1])}"

    return replaced


if __name__ == "__main__":
    strings = [
        "CapitaL letters",
        "A quick brown FOX jumps over the lazy DOG",
        "m n",
        "abc"
    ]

    for s in strings:
        print(solution(s))