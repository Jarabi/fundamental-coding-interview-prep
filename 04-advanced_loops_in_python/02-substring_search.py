from typing import List, Tuple

def string_search(source_array: List, search_array: List) -> List[Tuple]:
    result = []

    for i in range(len(source_array)):
        source_id, source_str = source_array[i]
        for j in range(len(search_array)):
            search_id, search_str = search_array[j]
            if source_id <= search_id and source_str in search_str:
                result.append(source_array[i])
                break

    return result


if __name__ == "__main__":
    tests = [
        ([(1, 'abc'), (2, 'def'), (3, 'xyz')], [(1, 'abcdef'), (5, 'uvwxy')]),  # [(1, 'abc')]
        ([(1, 'abc')], [(2, 'def')]),  # []
        ([(1, 'abc'), (2, 'def')], [(3, 'abc'), (4, 'def')]),  # [(1, 'abc'), (2, 'def')]
        ([(1, 'abc'), (2, 'def'), (3, 'ghi'), (4, 'jkl')], [(5, 'mnopqr')]),  # []
        ([(1, 'abc'), (2, 'def'), (3, 'ghi')], [(4, 'abcdefghi'), (5, 'defghiabc')]),  # [(1, 'abc'), (2, 'def'), (3, 'ghi')]
        ([(1, 'var'), (2, 'ans'), (3, 'tes')], [(4, 'variant'), (5, 'answertest'), (6, 'tesla')]),  # [(1, 'var'), (2, 'ans'), (3, 'tes')]
        ([(1, 'ab'), (2, 'bc'), (3, 'cd')], [(4, 'abcd'), (5, 'bcda')]),  # [(1, 'ab'), (2, 'bc'), (3, 'cd')]
    ]

    for test in tests:
        source_arr, search_arr = test
        print(string_search(source_arr, search_arr))