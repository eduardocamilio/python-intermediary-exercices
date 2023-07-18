import json

from class207_a import ARCHIVE_PATCH, Person, do_dump

do_dump()

with open(ARCHIVE_PATCH, 'r') as archive:
    people = json.load(archive)
    p1 = Person(**people[0])
    p2 = Person(**people[1])
    p3 = Person(**people[2])

    print(p1.name, p1.age)
    print(p2.name, p2.age)
    print(p3.name, p3.age)

print(__name__)
