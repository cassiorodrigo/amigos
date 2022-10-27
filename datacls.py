from dataclasses import dataclass


# @dataclass
class MyCars:
    car1: str
    car2: str

MyCars.car1 = 'Ferrari'
MyCars.car2 = 'Lambo'

print(MyCars.car1)

