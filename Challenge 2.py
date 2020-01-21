import pandas as pd 
import numpy as np 
from functools import reduce

x = [1,2,3,4,5]

def partial_prod (user_array):
    product_list = []
    for i in range(len(user_array)):
        product_list.append(reduce(lambda x,y: x*y, (user_array[:i] + user_array[i+1:])))
    return product_list

partial_prod(x)