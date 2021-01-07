class Employee:
    """
    Employee class covering all the concepts
    """
    pay_raise=1.10 #Normal constructor

    def __init__(self, f,l,s):
        print("Employee class constructor")
        self.first=f
        self.last=l
        self.pay=s


    def show_emp(self):
        #Normal method to display xlass memebr
        print("\nFirst Name = {} \nLast Name = {} \nSlalary = {}".format(self.first,self.last, self.pay))

    @property #This is getter
    def full_name(self):
        # Telling python - This is not a method - treat it like a object variable/object property when you call this
        # no need to give ()
        return "{} {}".format(self.last, self.first)

    @full_name.setter
    def full_name(self,n):
        """
        Check the method name is same as @property
        we sould allow assignment operator =
        Syntax - @property-name.setter
        """
        self.first, self.last=n.split(" ")

    def apply_raise(self):
        """
        Normal class method to make changes to object attribute using class varible to make you understand the concept
        not only normal calculation but more
        """
        self.pay *=Employee.pay_raise
        self.pay=int(self.pay)


    def __str__(self):
        "Special method"
        return self.first+","+self.last

    def __del__(self):
        print("-"*60)
        print("Calling Destructor")

#Main
e1=Employee("Zach","Jones",20000)
e1.show_emp()
e2=Employee("Charles","Mo",20000)
print("-"*60)
print(e2.full_name)

#--------------------------------------------------
# To update the value of @property method

print(e2.full_name)

e2.full_name="Jitendra Barik"

print(e2.full_name)

print(e2)
#or
print("Using the special method __str__",e2.__str__())

e1.apply_raise()
print(e1.show_emp())
print(e1.pay)

#del e1
#print("After delete",e1.first) # it will give error




