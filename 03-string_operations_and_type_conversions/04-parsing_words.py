def solution(s: str) -> str:
    lower_a = ord('a')

    return "-".join(
        chr((int(c) - 1) + lower_a)
        if c.isdigit()
        else str((ord(c) - lower_a) + 1)
        for c in s.split('-')
    )


if __name__ == "__main__":
    str_list = [
        "1-a-3-c-5",
        "a-26-b-25-c-24"
    ]

    for sequence in str_list:
        print(solution(sequence))