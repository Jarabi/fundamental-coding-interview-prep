def solution(s: str) -> int:
    num = ""
    numbers = []

    for char in s:
        if char.isdigit():
            num += char
        elif num:
            numbers.append(int(num))
            num = ""

    if num:
        numbers.append(int(num))

    return sum(numbers)


if __name__ == "__main__":
    records = [
        "no points scored in this game",
        "jake scored1point, john scored2points",
        "lena scored 50 points and lee scored 50 points"
    ]

    for record in records:
        print(solution(record))