def add_days(date: str, n: int) -> str:
    # Define days in each month (will adjust for leap years)
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Parse date
    year, month, day = [int(part) for part in date.split("-")]

    # Add days
    remaining_days = n

    while remaining_days > 0:
        # Check if current year is a leap year and update February days
        if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            days_in_current_month = 29
        else:
            days_in_current_month = days_in_month[month]

        # Calculate days left in current month
        days_left_in_month = days_in_current_month - day + 1

        if remaining_days < days_left_in_month:
            # If remaining days fit within current month
            day += remaining_days
            remaining_days = 0
        else:
            # Move to the next month
            remaining_days -= days_left_in_month
            day = 1

            if month < 12:
                month += 1
            else:
                month = 1
                year += 1

    return f"{year}-{month:02d}-{day:02d}"


if __name__ == "__main__":
    tests = [
        {'initial_date': '1999-01-01', 'num_days': 365},  # 2000-01-01
        {'initial_date': '2000-01-01', 'num_days': 365},  # 2000-12-31
        {'initial_date': '2000-01-01', 'num_days': 366},  # 2001-01-01
        {'initial_date': '2001-12-31', 'num_days': 1},  # 2002-01-01
        {'initial_date': '2000-12-31', 'num_days': 1},  # 2001-01-01
        {'initial_date': '2004-01-01', 'num_days': 1461},  # 2008-01-01
        {'initial_date': '1899-12-31', 'num_days': 50000},  # 2036-11-22
        {'initial_date': '2099-12-31', 'num_days': 50000}  # 2236-11-23
    ]

    for test in tests:
        initial_date, num_days = test.values()
        print(add_days(initial_date, num_days))