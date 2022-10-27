

class Person:
    '''Declare a person Object.'''
    is_ceo = False
    
    def __new__(cls, name:str, dob:str, profession:str):
        '''Prevent a creation of another CEO.'''
        if not Person.is_ceo:
            if profession == 'CEO':
                Person.is_ceo = True
                return super(Person, cls).__new__(cls)
        else:
            if profession == 'CEO':
                raise Exception("This company already has a CEO. '-- ")
        return super(Person, cls).__new__(cls)
    
    def __init__(self, name, dob, profession, *args, **kwargs):
        self.name = name
        self.dob = dob
        self.profession = profession

    def __str__(self):
        return f'''{self.name} is a {self.profession} and was born at {self.dob}'''

    def __repr__(self):
        return f'''Person({self.name},{self.dob},{self.profession}, {args})'''


class Developer(Person):
    '''Construct a Developer with a language associate with.'''
    def __init__(self, name, dob, profession, language: str = 'Python'):
        super().__init__(Person, name, dob, profession)
        self.name = name
        self.dob = dob
        self.profession = profession
        self.language = language

    def language(self):
        return self.language

    def __gt__(self, other):
        if len(self.profession) > len(other.profession):
            return True
        else:
            return False


class CEO(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def good_ceo(self):
        return True

if __name__ == "__main__":

    dev1 = Developer("Cassio", "10/05/1985", "Pilot")
    dev2 = Developer("Javier", "10/05/1985", "Cat carer")
    dev3 = Developer("Alejandro", "10/05/1985", "Full time network father")

    print(f'{len(dev1.profession) < len(dev3.profession)=}')
    ceo1 = CEO("Ciaran", "A long time ago", "CEO")
    ceo2 = CEO("Warren Buffet", "A really long time ago", "CEO")



