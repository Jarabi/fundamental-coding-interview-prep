# Define a string named 'word' to represent the phrase we'll work with
word = 'FRUIT Salad'

# Initialize a counter to hold the number of non-vowel characters
counter = 0

# Use a 'for' loop to iterate over each character in the string
for character in word:
    # Inside the loop, write a condition to check if it's not a vowel or a space
    # Don't forget that letters can be lowercase and uppercase
    if character not in 'aeiouAEIOU':
        # If the condition is true, increase the counter for non-vowel characters
        counter += 1

# Finally, print out the count of non-vowel characters
print(counter)