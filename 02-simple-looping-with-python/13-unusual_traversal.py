def unusual_traversal(array):
    n = len(array)

    mid = n // 2
    left = mid - 2
    right = mid + 2
    result = [array[mid]]

    while left >= 0 and right < n:
        result.extend(array[left:left + 2])
        result.extend(array[right - 1:right + 1])

        if left - 2 < 0 or right + 2 >= n:
            # Handle remaining elements
            if left - 1 >= 0:
                result.append(array[left - 1])
            if right + 1 < n:
                result.append(array[right + 1])
        left -= 2
        right += 2
    return result


if __name__ == "__main__":
    num1 = [1, 2, 3, 4, 5, 6, 7]
    num2 = [1, 2, 3, 4, 5]

    print(unusual_traversal(num1))  # [4, 2, 3, 5, 6, 1, 7]
    print(unusual_traversal(num2))  # [3, 1, 2, 4, 5]