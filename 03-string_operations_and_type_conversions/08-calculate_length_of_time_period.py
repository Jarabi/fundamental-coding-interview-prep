def time_period_length(time_period: str) -> int:
    # Split the time period
    start, stop = time_period.split(" - ")

    # Get the hours and minutes. Don't worry about the seconds
    start_hour, start_min, _ = [int(part) for part in start.split(":")]
    stop_hour, stop_min, _ = [int(part) for part in stop.split(":")]

    # Calculate start and stop duration in minutes
    start_minutes = start_hour * 60 + start_min
    stop_minutes = stop_hour * 60 + stop_min

    return stop_minutes - start_minutes


if __name__ == "__main__":
    time_periods = [
        "00:00:00 - 00:00:01",
        "00:00:00 - 00:01:00",
        "00:59:59 - 01:00:00",
        "00:00:00 - 23:59:59",
        "01:05:05 - 16:30:50",
        "12:15:30 - 14:00:00",
        "02:45:20 - 06:37:35"
    ]

    for tp in time_periods:
        print(time_period_length(tp))