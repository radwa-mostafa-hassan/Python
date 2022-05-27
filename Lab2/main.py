#! /usr/bin/python3
import re
import db
class Person:
    def __init__(self,full_name, money, sleepmood, healthRate):
        self.full_name = full_name
        self.money = money
        self.sleepmood = sleepmood
        self.healthRate = healthRate

    def sleep(self,hours):
        if(hours==7):
            print("Happy")
        elif(hours<7):
            print("Tired")
        else:
            print("Lazy")

    def eat(self,meals):
        if(meals==3):
            print("Health rate is 100%")
        elif(meals==2):
            print("Health rate is 75%")
        elif(meals==1):
            print("Health rate is 50%")

    def buy(self,items):
        if(items==1):
            return self.money*0.1

class Employee(Person):
    def __init__(self,emp_id, email, workmood, salary,is_manager):
        self.emp_id = emp_id
        self.email = email
        self.workmood = workmood
        self.salary = salary
        self.is_manager = is_manager

    def get_salary(self):
        if(self.salary>=1000):
            return self.salary
    
    def get_health_rate(self):
        x = range(0,100)
        if(self.healthRate in x):
            return self.healthRate

    def check_email(self,email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return email
        else:
            print("Invalid Email")
    
    def work(self,hours):
        if(hours==8):
            print("Happy")
        elif(hours<8):
            print("Tired")
        else:
            print("Lazy")

    def send_email(self,to,subject,body,receiver_name):
        try:
            f = open("email.txt", "w")
            f.write("to : "+to+"\nsubject : "+subject+"\nbody : "+body+"\nreceiver_name : "+receiver_name)
        except Exception:
            print("Something went wrong when writing to the file")
        finally:
            f.close()

class Office:
    def get_all_employees(self):
        print(db.get_all_employees())

    def get_employee(self,emp_id):
        print(db.get_employee(emp_id))
    
    def hire(self,employee):
        print(db.hire(employee))
    
    def fire(self,emp_id):
        print(db.fire(emp_id))

def main():
    value=int(input("1-Add a new Employee \n2-Add a new Manager \n3-Fire an Employee \n4-Get All Employees \n5-Search by ID for an Employee \n6-Quit\n"))
    if(value==1):
        name = input("Enter Employee's Name : ")
        email = input("Enter Employee's Email : ")
        emp = Employee(name,0,0,0,0)
        emp.name = name
        emp.email = email
        office = Office()
        office.hire(vars(emp))

    elif(value==2):
        name = input("Enter Manager's Name : ")
        email = input("Enter Manager's Email : ")
        emp = Employee(name,0,0,0,0)
        emp.name = name
        emp.email = email
        emp.is_manager = True
        office = Office()
        office.hire(vars(emp))

    elif(value==3):
        office = Office()
        office.get_all_employees()

    elif(value==4):
        e_id = int(input("Enter Employee's ID : "))
        office = Office()
        office.get_employee(e_id)

    elif(value==5):
        e_id = int(input("Enter Employee's ID : "))
        office = Office()
        office.fire(e_id)

    elif(value==6):
        return
    else:
        print("Please enter a valid value")

main()