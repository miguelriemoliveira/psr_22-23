maximum_number = 100

def isPerfect(value):
    if value == 0 or value == 1:
        return False

    divisors = [1]

    for i in range(2, int(value / 2) + 1):
        if value % i == 0:
            divisors.append(i)
            divisors.append(value/i)

    if sum(list(set(divisors))) == value:
        return True

    return False

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()