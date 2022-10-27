from abc import ABC, abstractmethod  # , abstractclass


class Person(ABC):

    @abstractmethod
    def name(self):
        ...

    def dob(self):
        ...

    @abstractmethod
    def profession(self):
        ...

class Developer(Person):
    def __init__(self, name, dob, profession):
        print(f'{name=}, {dob=}, {profession=}')
        self.name = name
        self.dob = dob
        self.profession = profession

    
    def name(self):  # when this is commented out, it will look for the name on the ABC class Person and raise an error
        return self.name  # to make it work, just coment it out and it will override the abstractmethod. All good.

    def dob(self):
        return self.dob

    #def profession(self):
    #    return self.profession

if __name__ == "__main__":

    dev1 = Developer("Cassio", "10051985", "Pilot")
    print(dev1.name)
    print(dev1.profession)
    print(dev1.dob)


