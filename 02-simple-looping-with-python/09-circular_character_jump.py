def repeat_char_jump(inputString, k):
    n = len(inputString)
    result = ""

    for i in range(n):
        result += inputString[(i * k) % n]
    return result


if __name__ == "__main__":
    str1 = "abcdefg"
    str2 = 'cgldxdv'

    print(repeat_char_jump(str1, 3))
    print(repeat_char_jump(str2, 4))