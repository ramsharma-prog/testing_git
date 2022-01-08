def add(*args):
    """ Add function"""
    count = 0
    for n in args:
        count += n
    print(f"Add function results: {count}")
    return count


def multiply(*args):
    """ Multiply function"""
    count = 1
    for n in args:
        count *= n
    print(f"Multiply function results: {count}")
    return count


def square(*args):
    for n in args:
        count = n**2
        print(f"Square root results: {count}")

def calculate(fun, *args):
    """ Takes functions"""
    return fun(*args)


# Call calculate function #
calculate(square, 1, 2, 3, 4, 5, )
