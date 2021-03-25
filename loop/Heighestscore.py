    #student_scores=[90,70,80,45,67]
student_scores = input("Enter the student scores that need to be added in the list").split()
for n in range(0,len(student_scores)):
    student_scores [n]= int(student_scores[n])
heighest_Score=0
for score in student_scores:
   if score >heighest_Score:
       heighest_Score=score
print(heighest_Score)
    