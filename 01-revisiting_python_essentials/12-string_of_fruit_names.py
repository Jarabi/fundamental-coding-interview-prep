# This code will create a simplified fruit salad with the provided fruits
fruits = ['apple', 'banana', 'cherry', 'date']
fruits_in_salad = ""

index = 0
# A while loop that assembles a string of fruit names separated by spaces, without adding a space after the last fruit
while index < len(fruits):
    if index != 0:
        fruits_in_salad += ", "
    fruits_in_salad += fruits[index]
    index += 1

print(fruits_in_salad)  # Output the fruits in the salad