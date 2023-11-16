class Student:
    def __init__(self):
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
        self.age = int(input("Enter age: "))
        self.math_score = float(input("Enter math score: "))
        self.physics_score = float(input("Enter physics score: "))
        self.python_score = float(input("Enter python score: "))

    def check_status(self):
        average_score = (self.math_score + self.physics_score + self.python_score) / 3
        if average_score >= 17:
            print(f"{self.first_name} {self.last_name} accepted")
        else:
            print(f"{self.first_name} {self.last_name} failed")


student = Student()


student.check_status()
