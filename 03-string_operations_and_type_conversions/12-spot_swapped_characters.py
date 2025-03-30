from typing import List, Tuple

def spot_swaps(source: str, target: str) -> List[Tuple[int, str, str]]:
    result = []

    for i in range(len(source) - 1):
        if source[i] != target[i] \
            and source[i+1] == target[i] \
            and source[i] == target[i+1]:
            result.append((i, source[i], target[i]))
    return result

if __name__ == "__main__":
    pairs = [
        ["hello", "hlelo"],
        ["abcdef", "abcfed"],
        ["goodbye", "godobye"],
        ["firsttest", "firtestst"],
        ["pythonista", "pyhtonista"],
        ["qwertyuiop", "qewrtyuiop"],
        ["hellothereworld", "helotlehreworld"]
    ]

    for pair in pairs:
        s, t = pair
        print(spot_swaps(s, t))