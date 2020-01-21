from itertools import permutations
x = [10,15,3,7]
perm = list(permutations(x,2))

map(sum, perm)

#Final Function Pass#
def sum_func(x, n):
    perm = list(permutations(x,2))
    sum_tup = [x+y for (x,y) in perm]
    truth_table = [True if x == n else False for x in sum_tup]

    for i in range(len(truth_table)):
        if(truth_table[i]):
            print "True at pair: " , perm[i]
         
sum_func([10,15,3,7], 17)
sum_func([11,15,3,7], 17)
