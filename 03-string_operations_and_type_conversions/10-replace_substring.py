def replace_substring(text: str, old: str, new: str) -> str:
    return text.replace(old, new)


if __name__ == "__main__":
    tests = [
        ["hello world", "world", "friend"],  # "hello friend"
        ["i love coding", "code", "craft"],  # "i love coding"
        ["it is a beautiful day", "beautiful", "gloomy"],  # "it is a gloomy day"
        ["practice makes perfect", "perfect", "better"],  # "practice makes better"
        ["keep calm and carry on", "carry on", "code on"],  # "keep calm and code on"
        ["long text long text", "long", "short"],  # "short text short text"
        ["lower case", "lower", ""],  # " case"
        ["a quick brown fox jumps over a lazy dog", "jumps", "skips"],  # "a quick brown fox skips over a lazy dog"
        ["this is a test", "this", "that"],  # "that is a test"
        ["final test case", "case", "example"],  # "final test example"
    ]

    for test in tests:
        t, o, n = test
        print(replace_substring(t, o, n))