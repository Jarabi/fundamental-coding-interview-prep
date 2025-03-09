# Sequence of temperatures throughout the day
temperatures = [16, 14, 20, 22, 19, 13]

# Loop through temperatures to suggest clothing
for temp in temperatures:
    if temp < 15:
        print("Wear warm clothes.")
        # If it's cold outside, we stop checking the temperatures. Add the needed line to interrupt the loop.
        break
    elif temp >= 20:
        # Add a line here that will skip the final print statement when it's warm enough for light clothes.
        continue
    print("Consider a light jacket.")  # Suggestion for in-between temperatures