def solution(n: int) -> int:
    consecutive_count = 0
    current = None

    while n > 0:
        digit = n % 10;

        if digit == current:
            consecutive_count += 1
        else:
            current = digit
        n //= 10

    return consecutive_count


if __name__ == "__main__":
    d1 = 113224
    d2 = 10000

    print(solution(d1))  # 2
    print(solution(d2))  # 3
