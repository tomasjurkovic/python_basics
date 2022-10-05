student_score = int(input("Insert student's score from the exam: "))

if 60 >= student_score <= 100:
    if 70 > student_score >= 60:
        print("The student will receive an D grade.")
    if 80 > student_score >= 70:
        print("The student will receive an C grade.")
    if 90 > student_score >= 80:
        print("The student will receive an B grade.")
    if 90 >= student_score:
        print("The student will receive an A grade.")
else:
    if student_score < 0 or student_score > 100:
        print("You inserted invalid value. Students' grades can be only from 0 to 100.")
    else:
        print("The student will receive an F grade.")

