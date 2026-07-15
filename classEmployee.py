class Employee:
    def __init__(self, employee_id, employee_name, employee_position, employee_salary ):
        self.emp_id = employee_id
        self.emp_name =employee_name
        self.emp_pos = employee_position
        self.emp_sal = employee_salary

    def get_empinfo(self):
        print(f"{self.emp_id} {self.emp_name} {self.emp_pos} {self.emp_sal}")
        
def main():
    emp_1 = Employee("01", "Dheeraj L", "MechE Intern", 12000)
    emp_2 = Employee("02", "Rachit", "Business Intern", 15000)
    emp_3 = Employee("03", "Messi", "Marketing Head" , 1400)
    emp_1.get_empinfo()
    emp_2.get_empinfo()
    emp_3.get_empinfo()
    
    
main()