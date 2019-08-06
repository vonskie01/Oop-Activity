class employment:
 def __init__(self,name,department,job,rate):
        self.name = name
        self.department = department
        self.position = position
        self.rate = rate
     
emp = True

employees = []

while emp:
    print("""
        ****************************
        [1] Add an employee
        [2] Enter employee's hours
        [3] Show information of Employees
        [4] Stop
        """)

    slctn = input("Enter your selection: ")
 
    if slctn == "1":
        name = (input("Enter name of  new Employee: \n"))
        department = (input("Enter a department for new Employee: \n"))
        position = (input("Enter position of new Employee: \n"))
        rate = int (input("Enter rates for new Employee: \n"))
        employees.append(employment(name,department,position,rate))
        print("Done!")

    elif slctn == "2":
        index = int (input("Enter index number of Employee: \n "))
        print(employees[index].name,"is selected!\n")
        hourly = int (input("Enter employee's hour: \n "))
        print("Employee's Salary: " , employees[index].rate * hourly)

    elif slctn == "3":
        for e in employees:
          print("*********************************")
          print(employees.index(e),"\n","Name:", e.name,"\n","Department:", e.department,"\n","Job:", e.position,"\n","Rate:", e.rate,"\n")
    
    elif slctn == "4":
        emp = False
        print("Stopping...")

    else:
        print("Invalid selection!")