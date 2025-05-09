class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self

    pass

    def set_wife_husband(self, wife: str, husband: str) -> None:
        if wife in Person.people:
            wife = Person.people[wife]
            wife.husband = self
        if husband in Person.people:
            husband = Person.people[husband]
            husband.wife = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person["name"]
        if name in Person.people:
            person_list.append(Person.people[name])
        else:
            person_list.append(Person(person.get("name"), person.get("age")))
    for person in people:
        wife = person.get("wife")
        husband = person.get("husband")
        if wife in Person.people or husband in Person.people:
            Person.people[person["name"]].set_wife_husband(wife, husband)
    return person_list
