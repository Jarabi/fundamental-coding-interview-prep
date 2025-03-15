from typing import List

def solution(numbers: List) -> List:
    n = len(numbers)
    result = []

    # Get the middle index
    mid = n // 2

    # Get left and right pointers
    left = mid - 1
    right = mid

    # Check if the length of integers is odd
    if n % 2:
        right += 1
        result.append(numbers[mid])

    while left >= 0 and right < n:
        # Append the product of left and right
        result.append(numbers[left] * numbers[right])
        left -= 1
        right += 1
    return result

if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [5, 3, 7, 1, 8, 4]
    nums3 = [10, 11]
    nums4 = [15]

    print(solution(nums1))  # [3, 8, 5
    print(solution(nums2))  # [7, 24, 20]
    print(solution(nums3))  # [110]
    print(solution(nums4))  # [15]
