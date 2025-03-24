def solution(s: str) -> str:
    rotated = [f'{word[-1:]}{word[:-1]}' for word in s.split()]
    return " ".join(rotated)


if __name__ == "__main__":
    str1 = "abc 123 def ghi"
    print(solution(str1))