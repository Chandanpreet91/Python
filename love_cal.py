# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name_one = name1.lower()
name_two = name2.lower()
t = name_one.count("t") + name_two.count("t")
print(f"T occurs {t} times")
r = name_one.count("r")+name_two.count("r")
print(f"R occurs {r} times")
u = name_one.count("u")+name_two.count("u")
print(f"U occurs {u} times")
e = name_one.count("e")+name_two.count("e")
print(f"E occurs {e} times")
total1 = t+r+u+e
print(f"Total = {total1}")
   


l = name_one.count("l")+name_two.count("l") 
print(f"L occurs {l} times")
o = name_one.count("o")+name_two.count("o")
print(f"O occurs {o} times")
v = name_one.count("v")+name_two.count("v")
print(f"V occurs {v} times")
e = name_one.count("e")+name_two.count("e")
print(f"E occurs {e} times")
total2 = l+o+v+e

print(f"Total = {total2}")
score1 = str(total1)
score2 = str(total2)
grand_total = score1+score2
total = int(grand_total)
print (f"Your Love Score is {total1}{total2}")
print(total)
if total < 10 and total>90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total<50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")