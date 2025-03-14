def solution(s: str) -> str:
    current_pair = None
    pair_count = 0
    pairs_stats = ""

    for i in range(0, len(s), 2):
        # Get current pair
        pair = f"{s[i]}{s[i+1]}"

        if pair == current_pair:
            # Increment count for current pair
            pair_count += 1
        else:
            if current_pair is not None:
                # Update pair stats
                pairs_stats += f"{current_pair}{pair_count}"
            # Restart count for new pair
            current_pair = pair
            pair_count = 1

    # Update stats for last pair
    pairs_stats += f"{current_pair}{pair_count}"

    return pairs_stats


if __name__ == "__main__":
    str1 = "aaabbabbababacab"
    str2 = "aaababbababaca"

    print(solution(str1))  # aa1ab1ba1bb1ab2ac1ab1
    print(solution(str2))  # aa1ab2ba3ca1