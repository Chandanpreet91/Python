#. Write a Python program to solve (x + y) * (x + y)
# x = int(input("Enter the value of x:"))
# y= int(input("Enter the value of y:"))
# print((x + y) * (x + y))

# Write a Python program to parse a string to Float or Integer.
# num = input("Enter any number")
# num = float(num)
# print(num)

# Write a python program to find the sum of the first n positive integers
numbers = input("Enter a list of numbers").split()
sum = 0
for num in range(0, len(numbers)):
    numbers[num] = int(numbers[num])
    if(numbers[num] >0):
        sum += numbers[num]
print(numbers)
print(sum)
