def solution(n):
    odd_product = 0

    while n > 0:
        # Get the least significant digit
        digit = n % 10

        # Check if digit is odd
        if digit % 2 != 0:
            # Update odd product
            odd_product = digit if odd_product == 0 else odd_product * digit

        # Remove the least significant digit from n
        n //= 10

    return odd_product


if __name__ == "__main__":
    num1 = 2468
    num2 = 43172

    print(solution(num1))
    print(solution(num2))