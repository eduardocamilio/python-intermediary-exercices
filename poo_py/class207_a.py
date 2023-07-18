import json

ARCHIVE_PATCH = 'class207.json'

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person('John', 33)
p2 = Person('Thayna', 22)
p3 = Person('James', 11)
bd = [vars(p1),p2.__dict__, vars(p3)]

def do_dump():
    with open(ARCHIVE_PATCH, 'w') as archive:
        print('do dump')
        json.dump(bd, archive, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('Its __main__')
    do_dump()