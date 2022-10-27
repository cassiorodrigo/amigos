

class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def is_a_good_budy(self):
        return '{self.name} is a good budy'

class Dev(Person):
    
    def __init__(self, name, dob, job):
        super().__init__(name, dob)
        self.name = name
        self.dob = dob 
        self.job = job
    
    @property
    def jobtitle(self):
        return self.job

if __name__ == "__main__":
    p1 = Person.is_a_good_budy()
    print(p1)
    #dev1 = Dev("Cassio", "10051985", "Bum")
    # d ev2 = Dev("Alejandro", "10051985", "network engineer")

    # good = dev2.is_a_good_budy()
    # print(good)

