# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest_score = 0
for high in student_scores:
  if high > highest_score:
    highest_score = high

print(f"The highest score in the class is: {highest_score}")