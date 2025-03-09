# List of temperatures with mixed weather conditions
temperatures = [32, 18, 21, 28, 35, 19, 22]

for temp in temperatures:
    # Print "It's really hot." and exit the loop if temperature is above 30
    if temp > 30:
        print("It's really hot.")
        break
    # Print "It's quite chilly." and skip to the next iteration if temperature is below 20
    if temp < 20:
        print("It's quite chilly.")
        continue
    print("Lovely weather.")