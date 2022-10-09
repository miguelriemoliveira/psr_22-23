#!/usr/bin/env python3


def main():

    age = 33

    v = "this is a string " + str(age)
    print(v)
    print(type(v))

    v = f"this is a string {age}"
    print(v)
    print(type(v))



if __name__ == "__main__":
    main()
