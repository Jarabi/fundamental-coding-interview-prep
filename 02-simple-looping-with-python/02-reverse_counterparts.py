def solution(numbers):
    result = []

    for i in range(len(numbers)):
        num = numbers[i]
        rev_num = int(str(numbers[i])[::-1])

        if rev_num in numbers:
            result.append((num, rev_num))
    return result