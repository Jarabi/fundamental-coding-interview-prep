from typing import List


def common_elements(listA: List, listB: List)-> List:
    result = []
    for i in range(len(listA)):
        for j in range(len(listB)):
            if listA[i] == listB[j]:
                result.append(listA[i])
    return result


if __name__ == "__main__":
    groups = [
        ([7, 2, 3, 9, 1], [2, 3, 7, 6]),  # [7, 2, 3]
        ([1, 2, 3, 4, 5], [-1, -2, -3, -4, -5]),  # []
        ([1, 2, 3], [2, 3, 4, 1]),  # [1, 2, 3]
        ([1, 2, 3], [3, 2, 1, 4, 5, 6]),  # [1, 2, 3]
        ([1, 2, 3], []),  # []
        ([-1, -2, -3, -4, -5], [-2, -4]),  # [-2, -4]
        ([1, 2, 3], [1, 3]),  # [1, 3]
    ]

    for group in groups:
        list_a, list_b = group
        print(common_elements(list_a, list_b))