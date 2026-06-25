class Student:
    name = "Maguang"
    age = 32
    nationality = "South Sudanese"


    def __init__(self, studentID,stage,hostel):
        self.studentID = studentID
        self.stage = stage
        self.hostel= hostel

student1 = Student("24/E/21480/PS", "Year 3", "Mish")
print(student1.name)
print(student1.age)
print(student1.nationality)
print(student1.studentID)
print(student1.stage)
print(student1.hostel)