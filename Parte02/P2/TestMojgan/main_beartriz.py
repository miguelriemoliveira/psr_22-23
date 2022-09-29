#!/usr/bin/env python3


def somar(p1,p2):
    
    print('Vou somar p1=' + str(p1) + ' + ' + str(p2))
    total = p1 + p2
    print('Resultado = ' + str(total))
    return total

def main():
    print('Hello')

    print('5+4 = ' + str(somar(5,4)))
    print('7+1 = ' + str(somar(7,1)))

    # somar(...)

if __name__ == "__main__":
    main()
