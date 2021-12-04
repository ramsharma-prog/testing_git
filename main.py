def add(*args):
    """ Add function"""
    count = 0
    for n in args:
        count += n
    print(f"Add function result: {count}")
    return count


def multiply(*args):
    """ Multiply function"""
    count = 1
    for n in args:
        count *= n
    print(f"Multiply function result: {count}")
    return count


def calculate(fun, *args):
    """ Takes functions"""
    return fun(*args)


# Call calculate function #
calculate(add, 1, 2, 3, 4, 5, )
