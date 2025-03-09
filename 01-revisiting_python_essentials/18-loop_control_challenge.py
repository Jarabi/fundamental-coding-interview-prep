# Define a list of temperatures
temperatures = [20, 18, 22, 35, 32]

# A loop to go through each temperature in the list
for temp in temperatures:
    # Add an 'if' statement to check if the temperature is over a really hot threshold
    if temp > 30:
        # Print a message for being really hot and then exit the loop
        print("It's too hot!")
        break
    # Add an 'elif' condition before the general temperature message to check if it's too cold
    elif temp < 20:
        # For temperatures that are too cold, print a specific message and skip to the next one
        print("It's too cold!")
        continue
    # Print a message saying the temperature is nice for all other cases
    print("Temperature is really nice!")