def solution(input_str: str) -> str:
    transformed_list = []
    capitalize_next = True

    for char in input_str:
        if char.isalpha():
            # Handle first character, or after space
            transformed_list.append(char.upper() if capitalize_next else char.lower())
            capitalize_next = False
        else:
            transformed_list.append(char.lower())
            capitalize_next = char == " "

    return ''.join(transformed_list)


if __name__ == "__main__":
    str_list = [
        "SoME rAndoM _TeXT",
        "CAPS lock IS on"
    ]

    for s in str_list:
        print(solution(s))