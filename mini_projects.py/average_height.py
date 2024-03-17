# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

t_height = 0
for height in student_heights:
  t_height+=height
print(f"total height = {t_height}")

t_stu=0
for no in range(0,len(student_heights)):
  t_stu+=1

print(f"number of students = {t_stu}")

average_height = round(t_height/t_stu)#round the value
print(f"average height = {average_height}")
