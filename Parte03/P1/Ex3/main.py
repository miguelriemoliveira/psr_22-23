#!/usr/bin/env python3
from colorama import Fore, Style, Back


class Animal():
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def congratulations(self):
        print('Congratulations ' + self.name)
        self.age += 1

class Dog(Animal):
    def __init__(self, name, age): 
        super().__init__(name=name, age=age) 

    def congratulations(self):
        print('Congratulations ' + self.name + ' Here is a Bone for you!!!')
        self.age += 1

    def __str__(self, prefix=''):
        text = prefix + 'I am a dog called ' + Fore.BLUE + self.name + Style.RESET_ALL + ' ' + str(self.age) + ' years old. Auaauau!'
        return text

class Person(Animal):
    def __init__(self, name, age, civil_state): # o construtor que é chamado sempre que se instancia um objeto da classe

        super().__init__(name=name, age=age) 
        # copy the arguments to properties of the class
        self.civil_state = civil_state
        self.spouse = None

        # Example of composition
        self.dog = Dog(name='boby', age=0)

    def marry(self, partner):

        if not self.civil_state == 'Single':
            print('Perhaps this is not a good idea!')
            return 

        if not partner.civil_state == 'Single':
            print('There are better options out there!')
            return 

        self.spouse = partner.name
        self.civil_state = 'Married'
        partner.spouse = self.name
        partner.civil_state = 'Married'


    def __str__(self):
        text = 'I am  a ' + Fore.BLUE + self.name + Style.RESET_ALL + ' ' + str(self.age) + ' years old.'

        if self.civil_state == 'Single':
            text += Fore.GREEN + ' I am free as a bird!' + Style.RESET_ALL
        else:
            text += Fore.RED + 'I am married to ' + self.spouse + Style.RESET_ALL
            
        return text


def main():
    
    p1 = Person(name='João', age=33, civil_state='Single')
    p2 = Person(name='Maria', age=34, civil_state='Single')
    c1 = Dog(name='Lassie', age=3)

#     print(p1)
#     print(p2)
#     p1.congratulations()
# 
#     p1.marry(p2)
#     print(p1)
#     print(p2)

    print(c1.__str__(prefix='Primeira chamada \n'))
    print(c1.__str__(prefix='Outra tentativa\n'))
    print(c1.__str__())
    print(c1.__str__())
    # c1.congratulations()
    # print(c1)

if __name__ == "__main__":
    main()

