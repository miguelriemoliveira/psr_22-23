#!/usr/bin/env python3

class Animal():
    def __init__(self, name, age): # constructor
        self.name = name
        self.age = age

    def congratulate(self):
        print('Congratulations ' + self.name + '!!!')
        self.age += 1


class Dog(Animal):
    def __init__(self, name, age): # constructor
        super().__init__(name=name, age=age)

    def __str__(self):
        text = 'I am a DOG named ' + self.name + ' and I am ' + str(self.age) + ' years old.'
        return text

    def congratulate(self):
        print('auauauauaau ' + self.name + '!!!')
        self.age += 1


class Person(Animal):
    def __init__(self, name, age, civil_state): # constructor
       super().__init__(name=name, age=age)
       self.civil_state = civil_state
       self.dog = Dog(name='boby', age=0) # NOT inheritance, this is composition

    def __str__(self):
        text = 'I am ' + self.name + ' and I am ' + str(self.age) + ' years old.'
        text += 'I am ' + self.civil_state
        return text

    def marry(self, partner):

        if self.civil_state == 'Married':
            print('I am not sure this a good idea.')
            return
            
        if partner.civil_state == 'Married':
            print('Are you sure your trust ' + partner.name)
            return

        print(self.name + ' and ' + partner.name + ' are married!!!')

        self.spouse = partner.name
        self.civil_state = 'Married'

        partner.spouse = self.name
        partner.civil_state = 'Married'
        
        
def doNothing(a1,a2,a3=33):
    print('a1 = ' + str(a1))
    print('a2 = ' + str(a2))
    print('a3 = ' + str(a3))
    print()
    return


def main():

    # Alternatives to calling a function
    doNothing(1,2,3) # using the order of the arguments (positional arguments)

    doNothing(a1=1, a2=2, a3=3) # using the names of the arguments (keyword argument)
    doNothing(a2=2, a3=3, a1=1) # using the names of the arguments (keyword argument)

    doNothing(1, a3=3, a2=2) # hybrid version
    # doNothing(a3=3, a2=2, 1) # hybrid version

    doNothing(1,2)

    # default values

#     p1 = Person(name='João', age=33, civil_state='Divorced')
#     p2 = Person(name='Maria', age=34, civil_state='Single')
#     d1 = Dog(name='Lassie', age=2)
# 
#     print('\n\nBEFORE')
#     print(p1)
#     print(p2)
#     p1.congratulate()
#     d1.congratulate()
#     p2.marry(p1)
# 
# 
#     print('\n\nAFTER')
#     print(p1)
#     print(p2)
# 
#     print(d1)


if __name__ == "__main__":
    main()
