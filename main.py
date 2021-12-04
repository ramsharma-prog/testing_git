import pandas as pd
import numpy as np



def add(*args):

    count = 0
    for n in args:

        count +=n
    print(count)
    return count

add(2,3,4,5,6,7)



