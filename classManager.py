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

    manager_registry = {}

    while True:

        task = int(input("Enter 1 if you want to add Managers \n" 
                "Enter 2 if you want to seach for managers \n"
                "Enter 3 to exit \n" ))
    
        if task == 1:
        
            Manager = input("Enter the name of the manager ")
            Manager_id = str(input("Enter the Manager ID "))
            Department_name = input("Enter the name of the department ")
            No_employees = str(input("Enter the No of Employees "))

            dept_manager = DepartmentManager(Manager, Manager_id, Department_name, No_employees)

            manager_registry[Manager_id] = dept_manager
            print(f"\nSuccessfully saved Manager {Manager_id} to the dictionary!")

            

        elif task == 2:
            search_id = input("Enter the Manager ID to be searched ")


            if search_id in manager_registry:

                retrieved_manager = manager_registry[search_id]

                print("\n--- Match Found ---")
                print(f"Name:        {retrieved_manager.get_man_name()}")
                print(f"Department:  {retrieved_manager.get_dep_name()}")
                print(f"No of Empployees: {retrieved_manager.get_no_emp()}")
            else:
                print("Manager ID not found in the dictionary.")

        elif task == 3:
            break

                

    


    

if __name__ == "__main__":
    main()





          