from math import sqrt

def solution(numbers):
    n = len(numbers)
    i = 0
    result = []

    while i < n:
        # Get current and opposite values
        current = numbers[i]
        opposite = numbers[n - i - 1]

        # Obtain geometric mean
        geometrical_mean = round(sqrt(current * opposite), 2)

        # Append to result list
        result.append((current, geometrical_mean))

        # Increment pointer
        i += 1

    return result

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(solution(arr))