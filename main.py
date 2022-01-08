def add(*args):
    """ Add function"""
    count = 0
    for n in args:
        count += n
    print(f"Find add function results: {count}")
    return count


def multiply(*args):
    """ Multiply function"""
    count = 1
    for n in args:
        count *= n
    print(f"Find Multiply function results: {count}")
    return count


def calculate(fun, *args):
    """ Takes functions"""
    return fun(*args)


# Call calculate function #
calculate(add, 1, 2, 3, 4, 5, )
