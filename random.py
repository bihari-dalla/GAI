#11. random AI style name for a virtual character

import random

first_name = ["neo", "ari", "zara", "leo", "nova"]
powers = ["mind", "fire", "tech", "star", "cyber"]

name = random.choice(first_name) + random.choice(powers)

print("Generated AI Character Name:", name)

----------------------------------------------------------------------
#12. unique color combination for AI generated digital artwork
import random

colours = ["Blue", "Green", "Red", "Black", "Orange", "Pink"]

colour1 = random.choice(colours)
colour2 = random.choice(colours)
colour3 = random.choice(colours)

print("AI Generated Colour Menu")
print("------------------------")
print("Colour 1:", colour1)
print("Colour 2:", colour2)
print("Colour 3:", colour3)
print("\nYour digital art work is ready")

-----------------------------------------------------------------------
#13. random poem using random module

import random

subjects = ["The moon", "A little bird", "The Ocean", "The star"]
verbs = ["shine", "sing", "dance", "glows"]
places = ["in the night", "in the sky", "near the sea", "in the garden"]

for i in range(4):
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    place = random.choice(places)
    print(subject, verb, place)

----------------------------------------------------------------------------
#14. random food mmenu for customer

import random

foods = ["Pizza", "Burger", "Pasta", "Vadapav", "Sandwich"]
drinks = ["Coffee", "Juice", "Milkshake", "Cold drink", "Tea"]
desserts = ["Ice Cream", "Cake", "Brownie", "Gulabjamun", "Kheer"]

print("Random Food Menu")
print("Main dish:", random.choice(foods))
print("Drink:", random.choice(drinks))
print("Dessert:", random.choice(desserts))
