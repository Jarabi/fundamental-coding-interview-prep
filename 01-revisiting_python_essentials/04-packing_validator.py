# Creating a list representing suitcase items
suitcase = ["shirt", "shorts", "toothbrush", "shoes"]

# Let's add "sunglasses" at the end of our suitcase
suitcase.append("sunglasses")

# Oops! We forgot socks. Let's insert socks at index 2
suitcase.insert(2, "socks")
print("Updated suitcase: " + str(suitcase))

# Now, let's get the first and last item from the suitcase
first_item = suitcase[1]
last_item = suitcase[-2]
print(first_item, last_item)

# Finally, let's remove "toothbrush" as we prefer to buy a new one at our destination
suitcase.remove("toothbrush")
print(suitcase)