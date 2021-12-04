
def add(*args):

    count = 0
    for n in args:

        count +=n

    print(f"Add function result: {count}")

    return count



def multiply(*args):

    count = 1
    for n in args:

        count *=n
    print(f"Multiply function result: {count}")
    return count


