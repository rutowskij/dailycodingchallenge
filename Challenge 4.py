import pandas as pd 
import numpy as np 

#Problem Given an array of integers, 
# find the first missing positive integer in linear time and constant space. In other words, 
# find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

#Should return 2
x = [3,4,-1,1]
def array_search(x):
    x_min = min(x)
    x_max = max(x)
    true_arr = np.arange(x_min, x_max)

    for i in range(len(true_arr)):
        if((true_arr[i] not in x ) & (true_arr[i] > 0)):
            return true_arr[i]
array_search(x)


