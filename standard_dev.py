
import math
from random import randint

def mk_random():
    random_list = []
    for x in range(1,101):
     z = randint(0,100)
     random_list.append(z)
    return random_list

print(mk_random())
'\n'

def calc_total():
    total_mark = 0
    for mark in mk_random():
        total_mark += mark
    return total_mark
        
print(calc_total())
'\n'

def calc_mean(x):
    mark_mean =  x / 100
    return mark_mean

tot = calc_total()
my_mean = (calc_mean(tot))
print(my_mean)

# Calculate standard Deviation

def sdev():
    tot_sdev_sum = 0
    for item in mk_random():
        tot_sdev_sum += (item - my_mean) ** 2
        #print(tot_sdev_sum)
    tot_root = tot_sdev_sum / len(mk_random())
    return math.sqrt(tot_root)

print(sdev())


