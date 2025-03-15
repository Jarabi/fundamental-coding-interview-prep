def solution(numbers):
    n = len(numbers)

    mid = n // 2
    left = mid - 1
    right = mid
    pairs = []

    if n % 2 != 0:
        right += 1
        pairs.append((numbers[mid], 0))

    while left >= 0 and right < n:
        pairs.append((numbers[left], numbers[right]))
        left -= 1
        right += 1

    return pairs


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [5, 11, 4, 16, 24, 9]

    print(solution(nums1))  # [(3, 0), (2, 4), (1, 5)]
    print(solution(nums2))  # [(4, 16), (11, 24), (5, 9)]