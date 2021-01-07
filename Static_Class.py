class Employee:
    '''
    Employee class covering all the concepts
    '''

    pay_raise=1.10 # Class variable

    def __init__(self,f,l,s):
        print("Employee constructor")
        self.first=f
        self.last=l
        self.pay=s

    def show_emp(self):
        "Normal function"
        print("\n{} {} gets the pay of {}".format(self.first,self.last,self.pay))

    @classmethod
    def from_str(cls,emp_str): # cls here is class
        """
        New constructor created using class method - receiving a string instead of 3 args
        """
        f,l,s=emp_str.split("-")
        s=int(s)
        #cls.s=10000 # I can assign the value of class member
        return cls(f,l,s)

    @classmethod
    def ask_user(cls):
        """One more constructor using class method - Input from user"""
        f=input("Enter the first name:")
        l=input("Enter the last name :")
        s=int(input("Enter the salary : "))
        #Employee(first, last, pay) instead of Employe class, I will use cls(f,l,s)...same way of Employee class
        return cls(f,l,s)

    @classmethod
    def set_raise_pay(cls, amount):
        cls.pay_raise=amount



    def __del__(self):
        print("Calling destructor")

#Main
#--------------------------------------------------------------------------------------
# Normal Object
e1=Employee("Steve","Jobs", 28000)
e2=Employee("Bill","Gates",85000)

e1.show_emp()
#--------------------------------------------------------------------------------
e3_str="Sam-Joe-90000"
e4_str="Tom-Mills-50000"
# If I need to achieve above, I need to do as following
# first, last, pay = e4_str.split("-")
#new_e1=Employee(first, last, pay ) --- we can use same as cls(first, last, pay) in static class
e3=Employee.from_str(e3_str) # Class method, which called cls (Class) itself to initialize data(Constructor)
e3.show_emp()                 # static class is an alternative constructor which create object
#------------------------------------------------------------------------------------------
#e5=Employee.ask_user() # Static Class to intitialize the class memeber from user input
#e5.show_emp()
#-----------------------------------------------------------------------------------------

print("-"*60)
e1.show_emp()
# Employee.set_raise_pay(10) # Static class - Update class data member Using class name
#Class method can be called using object
e1.set_raise_pay(2000) # Static class - Update

print(Employee.pay_raise)
print(e1.pay_raise)
print(e1.pay_raise)
print("-"*60)
# #-------------------------------------------------------------------------------------------