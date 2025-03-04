# 2. Write a Python function student_data () that will print the ID of a student (student_id).
# If the user passes an argument student_name or student_class 
# the function will print the student name and class. use kwargs.

# a = [1,2,3,4]
# b = {"a":"1", "b":"2", "c":"3"}
# b1 = {**b,**b}
# print(b1)

def student_data(student_id, **kwargs):
    print(f"Student ID: {student_id}")
    if "student_name" in kwargs:
        print(f"Student name: {kwargs["student_name"]}")
    
    if "student_class" in kwargs:
        print(f"Student class: {kwargs["student_class"]}")

    student_data(101)
    student_data(102, student_name = "Ramesh")
    student_data(103,student_name = "Suresh", student_class = "10th grade")