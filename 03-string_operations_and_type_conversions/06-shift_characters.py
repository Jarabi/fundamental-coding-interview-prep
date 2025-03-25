def solution(input_string):
    shifted, num = [], ""

    for char in input_string:
        if char.isdigit():
            num += char
        elif num and char.isalpha():
            shifted.append(f"{char}{num}")
            num = ""
        elif num and not char.isalnum():
            continue
        else:
            shifted.append(char)
    return ''.join(shifted)


if __name__ == "__main__":
    strings = [
        "I have 2 apples and 5! oranges and 3 grapefruits.",
        "4 foxes are chasing 1 rabbit."
    ]

    for s in strings:
        print(solution(s))