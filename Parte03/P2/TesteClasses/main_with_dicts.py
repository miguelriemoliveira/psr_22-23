#!/usr/bin/env python3

def congratulate(person):
    print('Congratulations ' + person['name'] + '!!!')
    person['age'] = person['age'] + 1

    return person

def main():


    # name = 'Miguel'
    # age = 25
    # civil_state = 'Married'
    # 
    # name1 = 'João'
    # age1 = 45
    # civil_state1 = 'Single'
    # 
    # name2 = 'Maria'
    # age2 = 34
    # civil_state2 = 'Single'

    persons = [{'name': 'Miguel', 'age': 25, 'civil_state': 'Married'},
               {'name': 'João', 'age': 45, 'civil_state': 'Single'},
               {'name': 'Maria', 'age': 34, 'civil_state': 'Single'} ]

    print(persons)
    persons[0] = congratulate(persons[0])

    print(persons)

if __name__ == "__main__":
    main()
