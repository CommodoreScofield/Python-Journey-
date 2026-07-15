class Student:

    def __init__(self, stuID, name, major, GPA):
        self.stuID = stuID
        self.name = name
        self.major = major
        self.GPA = GPA

    def get_stuinfo(self):
        print(f"{self.stuID} {self.name} {self.major} {self.GPA }")

    def set_stuinfo(self):
        attr = str(input("What attribute do you want to chnage"))
        if attr == "major":
            mjr = input("What MAjor do you want to change to")
            self.major = mjr
            print(f"{self.stuID} {self.name} {self.major} {self.GPA }")
        else:
            gpa = input("What MAjor do you want to change to")
            self.GPA = gpa
            print(f"{self.stuID} {self.name} {self.major} {self.GPA }")

def main():

    stu_01 = Student(1,"Dheeraj L", "MechE", 8.1)
    stu_01.get_stuinfo()
    stu_01.set_stuinfo()


main()



