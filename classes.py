
class A:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def emp_name(self):
        return self.name

    def emp_age(self):
        return self.age
    def incr_age(self):
        self.age += 1


class B(A):
    def __init__(self, name, age, sal):
        A.__init__(self,name, age)
        #super(B,self).(name,age)
        self.sal = sal
    def emp_sal(self):
        return self.sal


emp1 = B("John", 25, 50000)
print emp1.emp_name()
print emp1.emp_age()
emp1.incr_age()
print emp1.emp_age()
print emp1.emp_sal()
