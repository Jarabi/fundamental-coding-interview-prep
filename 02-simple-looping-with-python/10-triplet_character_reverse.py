def reversed_triple_chars(s: str) -> str:
    triplets = ""

    for i in range(0, len(s), 3):
        # Get subset of 3 characters
        subset = s[i:i + 3]

        if len(subset) == 3:
            # Place reversed string in original position
            triplets += subset[::-1]
        else:
            # Subset shorter than 3 characters. Leave as is
            triplets += subset

    return triplets


if __name__ == "__main__":
    str1 = "abcdefgh"
    print(reversed_triple_chars(str1))  # cbafedgh