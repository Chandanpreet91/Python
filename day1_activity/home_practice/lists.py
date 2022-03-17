import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# total = len(names)
# random_number = random.randint(0,total-1)
# print(names[random_number])


#OR
#choice method is also used to select a random number
random_name = random.choice(names)
print(random_name)
