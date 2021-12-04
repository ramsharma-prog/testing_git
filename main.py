
def add(*args):

    count = 0
    for n in args:

        count +=n
    print(f"Add results: {count}")
    return count

add(2,3,4,5,6,7)


def multiply(*args):
    count= 1
    for n in args:
        count*=n
    print(f"Multiply results: {count}")

    return count

multiply(2,3,4,5,6,7)