#!/usr/bin/python3
import colorama

class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return 'Name: ' + self.name + ' address: ' + self.address + ' phone: ' + str(self.phone)

def main():

    jose = Person('Jose', 'Aveiro', 93)
    miguel = Person('Miguel', 'Ilhavo', 91)

    print(jose)

    miguel.name += jose.name
    print(miguel)

    x = miguel.name + jose.name
    print(x)

    # lst_persons = [jose, miguel]
    #
    # for person in lst_persons:
    #     print(person.name)


if __name__ == '__main__':
    main()
