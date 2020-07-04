"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""
import math


def binary_search(iarray, value):
    index = int(math.floor(len(iarray) / 2))
    length = len(iarray)
    last = length - 1
    start = 0
    while start <= last:
        #   print("index: {}, start: {}, end: {}, value:{}, length={}, current={}".format(index, start, last, value, length, iarray[index]))
        current_value = iarray[index]
        if(current_value == value):
            return index
        elif value < current_value:
            last = index - 1
        elif value > current_value:
            start = index + 1
      #   print("1. index: {}, start: {}, end: {}, value:{}, length={}, current={}".format(index, start, last, value, length, iarray[index]))
        index = int(math.floor(start + last) / 2)

    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
