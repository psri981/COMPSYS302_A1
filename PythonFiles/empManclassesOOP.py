class Person:
    def __init__(self,name,age,height,weight,gender):
        self.name = name

        ## if the type of input is no correct then raise an Error. For example age should be 12 not "twelve"
        if not type(age) is int:
            raise TypeError
        else:
            self.age = age

        if not type(height) is float:
            raise TypeError
        else:
            self.height = height

        if not type(weight) is float:
            raise TypeError
        else:
            self.weight = weight
        
        self.gender = gender
 
        ##function to get initials and format into A.B    
        def get_initials(name):
            n = (name)
            split_name = n.split()
            initials = ""
            count = 0

            for name in split_name:  # go through each name
                initials += name[0].upper()  # append the initial
                count = count + 1
                if count == 1:
                    initials = initials + "."

            return initials
        
        self.initials = get_initials(name)
        
class Employee(Person):
    def __init__(self, name, age, height, weight, gender):
        super().__init__(name, age, height, weight, gender)
        
    def setManager(self,manager):
        self.manager = manager
        
class Manager(Employee):
    def __init__(self, name, age, height, weight, gender, employees = None):
        super().__init__(name, age, height, weight, gender)
        
        self.employees = employees
        
        if self.employees is None:
            self.employees = []
        else:
            self.employees = employees
        
    def addEmployee(self,employees):
        if employees not in self.employees:
            self.employees.append(employees)
          
#test
def printClassInfo(person):
      print("{} is {}, {}cm tall, weighs {}kg and is {} with the initials {}".format(person.name, person.age, person.height, person.weight, person.gender, person.initials))

michael = Employee("Michael Maxwell", 43, 179.4, 73.9, "Male")
jenna = Employee("Jenna Smith", 35, 168.4, 66.1, "Female")
krys = Manager("Krys Rogers", 26, 175.0, 70.0, "Non-binary")

printClassInfo(michael)
printClassInfo(jenna)
printClassInfo(krys)