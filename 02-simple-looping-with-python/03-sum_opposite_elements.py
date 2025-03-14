def solution(numbers):
    left = 0
    right = len(numbers) - 1
    sum_of_pairs = []

    while left <= right:
        # Get current and opposite elements
        current = numbers[left]
        opposite = numbers[right]

        # Add sum of elements to list
        sum_of_pairs.append(current + opposite)

        # Adjust left and right pointers
        left += 1
        right -= 1

    return sum_of_pairs


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 4, 5, 6]
    print(solution(arr1))
    print(solution(arr2))