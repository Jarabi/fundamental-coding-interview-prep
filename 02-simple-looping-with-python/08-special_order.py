def special_order(inputString: str) -> str:
    # Get the middle index
    mid = len(inputString) // 2

    # Get end to mid reversed
    end_rev = inputString[mid:][::-1]

    # Get start to mid
    start = inputString[:mid]

    return end_rev + start


if __name__ == "__main__":
    str1 = "abcdefg"
    str2 = 'abcddcba'

    print(special_order(str1))  # gfedabc
    print(special_order(str2))  # abcdabcd