gpa = float(input("What was the applicant's grade point average? \n"))

if gpa <= 3.7:
    inst_app = input("Is the student going to be educated at an approved institution? \n")

    if inst_app == "yes":
        print("The applicant qualifies for a low APR student loan")
    else:
        print("The applicant does not qualify for a low APR student loan")
else:
    print("The applicant did not have good enough grades to qualify")
