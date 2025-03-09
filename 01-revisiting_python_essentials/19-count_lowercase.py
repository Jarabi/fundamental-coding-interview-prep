text = "Python is fun!"
count_lowercase = 0

for char in text:
    if char.islower():
        count_lowercase += 1

print(count_lowercase)