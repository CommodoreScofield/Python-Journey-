class Manager:

    def __init__(self, man_name, man_id):
        self.manager_name = man_name
        self.manager_id = man_id

    def set_man_name(self,name):
        self.manager_name = name 

    def set_man_id(self,id):
        self.manager_id = id

    def get_man_name(self):
        return f"{self.manager_name}"
    
    def get_man_id(self):
        return f"{self.manager_id}"
    
class DepartmentManager (Manager):

    def __init__(self, man_name, man_id, dep_name, no_emp):
        super().__init__(man_name, man_id )
        self.dep_name = dep_name
        self.no_emp = no_emp

    def set_dep_name(self,name):
        self.dep_name = name

    def set_no_emp(self,no):
        self.no_emp = no

    def get_dep_name(self):
        return f"{self.dep_name}"
    
    def get_no_emp(self):
        return f"{self.no_emp}"



def main():
    Manager = input("Enter the name of the manager ")
    Manager_id = str(input("Enter the Manager ID "))
    Department_name = input("Enter the name of the department ")
    No_employees = str(input("Enter the No of Employees "))

    info = DepartmentManager(Manager, Manager_id, Department_name, No_employees)

    print(info.get_man_name())
    print(info.get_man_id())
    print(info.get_dep_name())

if __name__ == "__main__":
    main()





          