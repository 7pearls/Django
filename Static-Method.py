class Employee:
    """
    Employee class covering all concepts
    """

    pay_raise=1.10 #Class data memeber

    def __init__(self,f,l,s):
        print("Employee class constructor")
        self.first=f #obj variable
        self.last=l
        self.pay=s


    def show_emp(self):
        print("\n{} {} get the pay {}".format(self.first,self.last,self.pay))


    @staticmethod
    def change_raise(new_r):
        "Static method does not require self in arg"
        Employee.pay_raise=new_r
       # print(new_r)

    @staticmethod
    def is_workday(d):
        if d.weekday() == 5 or d.weekday() == 6:
            return False
        return True


    def __del__(self):
        """
        Desctructor
        """
        print("Object Desctor get called")


e1=Employee("Steve", "Zack", 200000)
#e2=Employee("Steve", "Zack", 200000)
e1.show_emp()
#e1.first=100 # Update class data member
print(e1.first)
print(Employee.pay_raise)

Employee.change_raise(100)

print(Employee.pay_raise)

#del e1

#---------------------------------------------------------------
import datetime
my_date=datetime.date(2016,7,8)
print(Employee.is_workday(my_date))

my_date=datetime.date(2021,1,9)
print(Employee.is_workday(my_date))

