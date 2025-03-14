def solution(n: int)  -> int:
    reversed_digits = 0

    while n > 0:
        # Get the least significant digit
        digit = n % 10

        # Update reversed digits
        reversed_digits = digit \
            if reversed_digits == 0 \
            else reversed_digits * 10 + digit

        # Remove the least significant digit
        n //= 10

    return reversed_digits


if __name__ == "__main__":
    d1 = 4567890
    d2 = 12345

    print(solution(d1))
    print(solution(d2))