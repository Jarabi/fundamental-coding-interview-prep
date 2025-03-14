from http.cookiejar import cut_port_re
from typing import List

def solution(s: str) -> List:
    consecutive_groups = []
    current_char = None
    char_count = 0

    # Iterate through the string in reverse
    for char in s[::-1]:
        if char == current_char:
            # Increment count for consecutive identical characters
            char_count += 1
        else:
            if current_char is not None:
                # Update character statistics
                consecutive_groups.append((current_char, char_count))
            # Refresh count for new character
            current_char = char
            char_count = 1

    # Update statistics for final character
    consecutive_groups.append((current_char, char_count))

    return consecutive_groups


if __name__ == "__main__":
    str1 = "aaabbcccdde"
    print(solution(str1))  # [('e', 1), ('d', 2), ('c', 3), ('b', 2), ('a', 3)]