''' Question Number # 3::A teacher maintains a list of students in a class. The list is ["Alice", "Bob", "Chacha", 
"David", "Elon"..]. Write a Python program to print the names of students whose names start 
with "C" or "H" or "K". '''

Students = ["Alice", "Bob", "Chacha", "David", "Elon" ,"Fahim", "George", "Hena", "Inoovative", "Jhon","Kothai?","Lahiru", "Mithun"]
 

def filter_students(students):
    for student in students:
        if student.startswith("C") or student.startswith("H") or student.startswith("K"):
            print(student)

filter_students(Students)

