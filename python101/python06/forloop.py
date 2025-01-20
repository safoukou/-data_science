def student_grade(grades)
    for i in range(len(grades)-1, 2): # skip in selection of any element in the list
        grades -=5

def student_grade(grades):
    for i in range(len(grades)):
        grades[i] = grades[i]-5 # remove -5 in every element in the array
        grades[i] -=5
    

    for i, grade in enumerate(grades): # enumerate atribut every grade to each students
        if grade <50:
            print(f"student {i} has failled with grade {grade}")
        else:
            print(f"student {i} has passed with grade {grade}")
    return grades


grades = [91, 88, 75, 95, 80, 85,23, 100, 10, 11,76, 54, 32, 65, 43, 76, 
          87, 98, 99,45, 67, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
          
          
          
student_grade(grades)