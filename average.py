#One way to calculate average
student_heights = input('Enter a list of student heights:').split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total = 0
num_of_el = 0
for height in student_heights:
    total += int(height)
for element in student_heights:
    num_of_el += 1
print(total/num_of_el)
print("---------------------------------------")
#otherway
total_heights = sum(student_heights)
total_length = len(student_heights)
average = total_heights/total_length
print(total_heights/total_length)
