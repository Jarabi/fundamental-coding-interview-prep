def solution(n: int) -> int:
    duplicates = 0
    significance = 1

    while n > 0:
        # Get the least significant digit
        digit = n % 10

        # Update the duplicates value
        duplicates += digit * 11 * significance

        # Increase the significance by a factor of 100
        significance *= 100

        # Remove the least significant digit from n
        n //= 10

    return duplicates

if __name__ == "__main__":
    d1 = 9876
    d2 = 10000

    print(solution(d1))
    print(solution(d2))