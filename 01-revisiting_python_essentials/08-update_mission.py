# Given mission name
mission_name = "Sort"

# Print the first and the last character of the mission name
print(mission_name[0])
print(mission_name[-1])

# The mission needs a minor update. We aim to change its first letter to 'P' and
# the last letter to `k`, obtaining the word "Pork".
# Remember, strings in Python are immutable, so you cannot alter them directly.
new_mission = 'P' + mission_name[1:-1] + 'k'

# Print the updated mission name
print(new_mission)