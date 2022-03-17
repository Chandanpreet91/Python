import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
total = len(names)
random_number = random.randint(0,total)
print(names[random_number])
