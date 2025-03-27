from typing import List

def add_seconds_to_times(time_points: List, added_seconds: int) -> List:
    output = []
    seconds_in_day = 24 * 3600

    for parts in time_points:
        # Split the hours, minutes and seconds
        hours, minutes, _seconds = [int(part) for part in parts.split(":")]

        # Convert all parts into seconds
        seconds_from_start = hours * 3600 + minutes * 60 + _seconds

        # Add the seconds
        total_seconds = (seconds_from_start + added_seconds) % seconds_in_day

        # Extract the hours after adding seconds
        new_hours, remainder = divmod(total_seconds, 3600)

        # Extract minutes and seconds from the remaining seconds
        new_minutes, new_seconds = divmod(remainder, 60)

        # Join the new hours, minutes and seconds into time representation
        output.append(f"{new_hours:02d}:{new_minutes:02d}:{new_seconds:02d}")

    return output


if __name__ == "__main__":
    tests = [
        {'tp': ['10:00:00', '23:30:00'], 's': 3600},
        {'tp': ['01:00:00', '02:00:00', '03:00:00'], 's': 7200},
        {'tp': ['12:00:00'], 's': 43200},
        {'tp': ['00:00:00'], 's': 86399}
    ]

    for test in tests:
        tp, s = test.values()
        print(add_seconds_to_times(tp, s))