from typing import List, Any, Optional, Dict

class Person:
    def __init__(self, *args: Optional[List[str]], **kwargs):
        # self.name = kwargs.get('name') or 'Cassio'
        if not kwargs.get('name'):
            kwargs['name'] = 'Cassio'
        self.name = kwargs['name']
    
        # self.cars: List[str] = ['Ferrari', 'Lamborgini']  # self.cars is a list of strings
        self.cars: List[str] =  args # self.cars is a list of strings

        
if __name__ == '__main__':
    p1 = Person()
    p2 = Person(*['Ferrari', 'Lamborgini'], name='Javier')

    print(p1.name)
    print(p2.name)
    print(p2.cars)
