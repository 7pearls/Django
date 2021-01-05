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
    def from_str(cls,emp_str):
        """
        New constructor created using class method - receiving a string instead of 3 args
        """
        f,l,s=emp_str.split("-")
        s=int(s)
        return cls(f,l,s)

    def __del__(self):
        print("Calling destructor")



#Main
e1=Employee("Steve","Jobs", 28000)
e1.show_emp()
e3_str="Sam-Joe-90000"
e4_str="Tom-Mills-50000"

e3=Employee.from_str(e3_str)
e3.show_emp()
