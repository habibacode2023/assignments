students=[  {"Mahmizər Həsənova":{"degree": "IT", "courses":["analytics", "statistics"], "no": 1234}},
    {"Mədinə Abdulsəmədova":{"degree": "Business Informatics", "courses":["analytics", "statistics"], "no": 1234}},
    {"Adil Rəhimov":{"degree": "Automation", "courses":["analytics"], "no": 1234}},
    {"Rafiq Rafiqzadə":{"degree": "Automation", "courses":["analytics"], "no": 1234}},
    {"Anar Əhmədov":{"degree": "Data Science", "courses":["analytics"], "no": 1234}},
    {"Minəxanım Hacımuradova":{"degree": "Computer Engineering", "courses":["analytics"], "no": 1234}},
    {"Riyad Əhmədov":{"degree": "IT", "courses":["analytics"], "no": 1234}},
    {"Riyad Əbdürəhimov":{"degree": "IT", "courses":["analytics"], "no": 1234}},
    {"Lalə Məmmədli":{"degree": "Artificial Intelligence", "courses":["analytics"], "no": 1234}},
    {"İlyas Abbasov":{"degree": "Computer Science", "courses":["analytics"], "no": 1234}},
    {"Yusif Ağasalamlı ":{"degree": "Computer Science", "courses":["analytics"], "no": 1234}},
    {"Ləman Rəhimli":{"degree": "Maths", "courses":["analytics"], "no": 1234}},
    {"Həbibə Məmmədli":{"degree": "Maths", "courses":["analytics"], "no": 1234}},
    {"Lala Taghiyeva":{"degree": "Policy Analysis", "courses":["analytics"], "no": 1234}},
    {"Niyyət Rzayev":{"degree": "Automation", "courses":["analytics"], "no": 1234}}
]
#Create list for student's degree
def func():
    degree_students={}
#If degrees are equal add student name to degree_students list
    for student in students:
        degree=student[list(student.keys())[0]]["degree"]
        if degree in degree_students:
            degree_students[degree].append(student)
        else:
            degree_students[degree]=[student]
    return degree_students  
    #Create degree column with ":" for student name and surname         
for degree, students in func().items():
    print(degree+":")
    for student in students:
        print(list(student.keys())[0])
pass




