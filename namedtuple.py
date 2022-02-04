from collections import namedtuple

class Person:
    def __init__(self, name, rase, health, mana, strength):
        self.name = name
        self.rase = rase
        self.health = health
        self.mana = mana
        self.strength = strength

hero_1 = Person('Aaz', 'Isverq', 100, 0.0, 250)
print(hero_1.health)

New_Person = namedtuple('New_Person', 'name, rase, health, mana, strength')
hero_2 = New_Person('Aaz', 'Isverq', 100, 0.0, 250)
print(hero_2.name)

prop = ['name', '2rase', 'health', 'mana', '_strength']
New_Person_2 = namedtuple('New_Person_2', prop, rename=True)
hero_3 = New_Person_2('Aaz', 'Isverq', 100, 0.0, 250)
print(hero_3)
print('*' * 50)


Point = namedtuple('Point', 'x, y, z')
p1 = Point(2, z=7, y=4)
print(p1)

t = [22, 17, 14]
p2 = Point._make(t)
print(p2)

d2 = p2._asdict()
print(d2)

# p2.y = 1
p3 = p2._replace(y=1)
print(p3)

print(p2._fields)
print('*' * 50)

New_Point = namedtuple('New_Point', 'x, y, z', defaults=[0, 0])
p4 = New_Point(5, 3)
print(p4)

print(p4._field_defaults)

dic = {'x': 7, 'y': 0, 'z': 11}
p5 = New_Point(**dic)
print(p5)