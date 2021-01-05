class Employee:
    """
    Employee class covering all the concepts
    """
    pay_raise=1.10 #Class variable

    def __init__(self,f,l,s): #Normal constuctor
        print("Employee constructor")
        self.first=f #obj variable
        self.last=l
        self.pay=s

    def show_emp(self):
        """Normal method to display the objects contents"""
        print("\n{} {} gets the pay of {}".format(self.first,self.last,self.pay))
    def __del__(self):
        """Destructor"""
        print("Destructor")


e1=Employee("Steve","Jobs",280000)
e1.show_emp()
print(e1.first," ",e1.last) # Class Memeber access

