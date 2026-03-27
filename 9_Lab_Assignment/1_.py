class Employee:
    def get_input(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    def get_manager_input(self):
        self.get_input()
        self.department = input("Enter Department: ")

    def display_manager(self):
        self.display()
        print("Department:", self.department)
        print("----------------------")


# Main Program
managers = []

for i in range(10):
    print(f"\nEnter details for Manager {i+1}")
    m = Manager()
    m.get_manager_input()
    managers.append(m)

print("\n--- Manager Details ---")
for m in managers:
    m.display_manager()