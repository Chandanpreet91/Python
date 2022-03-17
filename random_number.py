import random

# rand_value = int(random.random()*2)
rand_value = random.randint(0,1)
if(rand_value) == 0:
    print("Tails")
else:
    print("Heads")
