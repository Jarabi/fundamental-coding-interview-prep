from typing import List, Tuple


def solution(list_a: List, list_b: List) -> List[Tuple]:
    result = []

    for a in list_a:
        for b in list_b:
            if a > b and (a, b) not in result:
                result.append((a, b))
    return result


if __name__ == "__main__":
    tests = [
        ([5, 1, 8, -2, 0], [3, 2, 7, 10, -1]),  # [(5, 3), (5, 2), (5, -1), (1, -1), (8, 3), (8, 2), (8, 7), (8, -1), (0, -1)]
        ([3, 2, 1], [1, 2, 3]),  # [(3, 1), (3, 2), (2, 1)]
        ([-1000] * 50, [1000] * 50),  # []
        ([0], [0]),  # []
        ([1000] * 50, [-1000] * 50),  # [(1000, -1000)]
    ]

    for test in tests:
        lst_a, lst_b = test
        print(solution(lst_a, lst_b))