import random

appetizers = ["spinach dip", "mozerella sticks", "nachos", "chicken wings", "cheese platter"]
main = ["chicken nuggets", "grilled cheese", "mac and cheese", "pasta", "pizza", "burger", "taco"]
sides = ["fries", "salad", "mashed potatoes", "onion rings", "guacamole", "veggies", "cheese"]
dessert = ["ice cream", "cheesecake", "cookies", "pie", "lava cake", "truffles"]

randomApp = random.randint(0,4)
randomMain = random.randint(0,6)
randomSide = random.randint(0,6)
randomDessert = random.randint(0,5)

print("Menu:")
print(appetizers[randomApp])
print(main[randomMain])
print(sides[randomSide])
print(dessert[randomDessert])
