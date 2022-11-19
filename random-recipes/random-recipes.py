import random

day_of_week = ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI"]
day = ""

print("Dans quelle livre")
book = random.randint(1, 5)
print(book)
if book == 1:
	recipe = random.randint(8, 56)
elif book == 2:
	recipe = random.randint(9, 73)
elif book == 3:
	recipe = random.randint(9, 68)
elif book == 4:
	recipe = random.randint(8, 73)
else:
	recipe_page = [31,44,59,73,89,102,117,131,147,161,175,186,205,219,233,247]
	recipe = recipe_page[random.randrange(0, len(recipe_page))]
	day = random.randint(1, 5)

print("Quelle recette ?")
print(recipe)
if day:
	print("Quelle jour de la semaine")
	print(day_of_week[day])
