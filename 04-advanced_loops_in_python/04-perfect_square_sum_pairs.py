from typing import List, Tuple


def is_perfect_square(num: int) -> bool:
    if num < 0:
        return False

    # Find the square root and check if it's an integer
    root = int(num ** 0.5)
    return root * root == num


def solution(arr1: List, arr2: List) -> List[Tuple]:
    result = []

    if not arr1 or not arr1:
        return result

    for x in arr1:
        for y in arr2:
            if is_perfect_square(x + y):
                result.append((x, y))

    return result


if __name__ == "__main__":
    tests = [
        ([2, 3, 16], [1, 9, 10]),  # [(3, 1), (16, 9)]
        ([0], [0]),  # [(0, 0)]
        ([4, 13, 23], [-4, -3, -24]),  # [(4, -4), (4, -3), (13, -4)]
        ([100, 75, 36, 9, -25, -64, -100], [-1, 1, 24, 0, -1, -24]),  # [(100, 0), (36, 0), (9, 0)]
        ([], [1, 2, 3, 4]),  # []
        ([1, 2, 3, 4], []),  # []
        ([], []),  # []
    ]

    for test in tests:
        a1, a2 = test
        print(solution(a1, a2))